"""Evaluate model-predicted logic forms against ground truth.

Compares predicted logic forms (from ``experiments/FewShot/Results/``) with the
ground-truth annotations in ``encodedForm/fixed_all_combined.json`` using
semantic similarity, and writes per-model evaluation reports (JSON + Markdown)
under ``experiments/Evaluation/``.
"""
import json
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher

def load_json(filepath):
    """Load JSON file and return the data."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    # Handle different JSON structures
    if isinstance(content, dict) and 'data' in content:
        return content['data']
    return content

def has_capitalized_predicates(logic_form_str):
    """Check if logic form contains any capitalized predicate names.
    
    ASP requires lowercase predicate names, so capitalized ones indicate an error.
    
    Returns:
        tuple: (has_caps: bool, capitalized_predicates: list)
    """
    import re
    
    if not logic_form_str:
        return False, []
    
    # Find all predicate names (word followed by open paren)
    # Predicate names should be lowercase, so any with uppercase letters are violations
    capitalized = []
    
    # Match pattern: word( where word contains at least one uppercase letter
    matches = re.findall(r'\b([A-Z][a-zA-Z0-9_]*)\(', logic_form_str)
    
    if matches:
        capitalized = sorted(list(set(matches)))
        return True, capitalized
    
    return False, []

def normalize_predicate(predicate):
    """Normalize a predicate by handling synonyms and removing articles.
    
    NOTE: Only normalizes lowercase predicate names (ASP requirement).
    Capitalized predicate names are considered invalid and should fail validation.
    
    Examples:
        'customer("a customer")' -> 'person("customer")'
        'customer(nicole)' -> 'person("nicole")'  (adds quotes for consistency)
        'likes(john, mary)' -> 'likes("john", "mary")'  (adds quotes to all args)
        'person("The Person")' -> 'person("person")'
        'restaurant("A RESTAURANT")' -> 'restaurant("restaurant")'
        'Customer(...)' remains unchanged (invalid ASP syntax)
    """
    import re
    
    # Replace LOWERCASE 'customer' predicate with 'person' for interchangeability
    # Note: Does NOT match 'Customer' or other capitalizations
    normalized = predicate.replace('customer(', 'person(')
    
    # Trim leading and trailing whitespace inside quoted strings first
    normalized = re.sub(r'(\")\s+(.+?)\s+(\")', r'\1\2\3', normalized)
    
    # Remove articles (a, an, the) followed by space from inside quoted strings (case-insensitive)
    # Pattern matches: (")(a |an |the )(rest)("")
    normalized = re.sub(r'(")(?:a |an |the )(.+?)(")', r'\1\2\3', normalized, flags=re.IGNORECASE)
    
    # Clean up any extra spaces that may have been left behind (multiple spaces)
    normalized = re.sub(r'(\")\s+', r'\1', normalized)
    
    # Normalize quotes consistency and underscore handling:
    # Add quotes around unquoted identifiers/atoms (including converting underscores to spaces)
    
    # After opening paren: no space before quoted arg
    # Match unquoted identifier and convert underscores to spaces
    def add_quotes_after_paren(match):
        ident = match.group(1)
        ident_normalized = ident.replace('_', ' ')
        return '("' + ident_normalized + '"'
    normalized = re.sub(r'\(\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*(?=[,\)])', add_quotes_after_paren, normalized)
    
    # After comma: space before quoted arg
    # Match unquoted identifier and convert underscores to spaces
    def add_quotes_after_comma(match):
        ident = match.group(1)
        ident_normalized = ident.replace('_', ' ')
        return ', "' + ident_normalized + '"'
    normalized = re.sub(r',\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*(?=[,\)])', add_quotes_after_comma, normalized)
    
    # Lowercase argument values inside quotes (case-insensitive argument comparison)
    # Pattern: (")(any content)("")
    def lowercase_quoted_content(match):
        quote = match.group(1)
        content = match.group(2).lower()
        return quote + content + quote
    
    normalized = re.sub(r'(\")(.*?)(")', lowercase_quoted_content, normalized)
    
    return normalized

def exact_match(pred_logic_form, ground_truth_logic_form):
    """Check if logic forms match exactly after normalization.
    Compares all predicates after normalizing each one.
    
    NOTE: Fails immediately if predicted form contains capitalized predicates (invalid ASP).
    
    Returns True if:
    - No capitalized predicates in predicted form
    - All predicates match (100% similarity)
    """
    if not pred_logic_form or not ground_truth_logic_form:
        return False
    
    # Handle both single string and list of strings
    if isinstance(pred_logic_form, list):
        pred_str = ' '.join(pred_logic_form)
    else:
        pred_str = pred_logic_form
    
    if isinstance(ground_truth_logic_form, list):
        gt_str = ' '.join(ground_truth_logic_form)
    else:
        gt_str = ground_truth_logic_form
    
    # Check for capitalized predicates in predicted form (invalid ASP syntax)
    # We still detect and report them elsewhere, but do not block exact matching here.
    has_caps, cap_preds = has_capitalized_predicates(pred_str)

    # Use similarity score to determine exact match (semantic equality)
    # similarity_score returns (similarity, ...). Treat similarity == 1.0 as exact match.
    sim, _, _, _, _, _ = similarity_score(pred_str, gt_str)
    return sim == 1.0

def extract_predicates_raw(logic_form_str):
    """Extract individual predicates from logic form string WITHOUT normalization.
    Returns predicates exactly as they appear in the raw logic form.
    
    Returns:
        set: Set of raw predicate strings
    """
    if not logic_form_str:
        return set()
    
    predicates = set()
    import re
    
    # Use regex to extract complete predicates with balanced parentheses
    # Pattern: word followed by balanced parentheses
    # This matches: predicate_name(...) including nested predicates
    pattern = r'([a-z_][a-zA-Z0-9_]*)\s*\([^)]*(?:\([^)]*\)[^)]*)*\)'
    
    matches = re.findall(pattern, logic_form_str)
    # The above pattern only captures the predicate name, so we need a different approach
    
    # Better approach: Find all predicate(...) by looking for word( and finding matching )
    current_pos = 0
    while current_pos < len(logic_form_str):
        # Find next predicate name
        match = re.search(r'[a-z_][a-zA-Z0-9_]*\s*\(', logic_form_str[current_pos:])
        if not match:
            break
        
        start = current_pos + match.start()
        paren_start = current_pos + match.end() - 1  # Position of opening (
        
        # Find matching closing parenthesis
        paren_count = 1
        pos = paren_start + 1
        while pos < len(logic_form_str) and paren_count > 0:
            if logic_form_str[pos] == '(':
                paren_count += 1
            elif logic_form_str[pos] == ')':
                paren_count -= 1
            pos += 1
        
        if paren_count == 0:
            # Found complete predicate
            predicate = logic_form_str[start:pos]
            if not predicate.startswith("story_step("):
                predicates.add(predicate)
            current_pos = pos
        else:
            # Malformed, move to next character
            current_pos += 1
    
    return predicates

def extract_predicates(logic_form_str):
    """Extract individual predicates from logic form string.
    Ignores story_step(0..N) declarations as they can be inferred.
    Normalizes predicates for comparison (handles synonyms and articles).
    
    Returns:
        set: Set of normalized predicate strings
    """
    if not logic_form_str:
        return set()
    
    predicates = set()
    import re
    
    # Use the raw extraction first to get complete predicates
    raw_predicates = extract_predicates_raw(logic_form_str)
    
    # Normalize each predicate
    for predicate in raw_predicates:
        normalized = normalize_predicate(predicate)
        if normalized:
            predicates.add(normalized)
    
    return predicates

def similarity_score(pred_logic_form, ground_truth_logic_form):
    """Calculate similarity score by comparing predicates.
    
    Returns:
        tuple: (similarity_score, matching_predicates_normalized, pred_only_normalized, gt_only_normalized,
                pred_only_raw, gt_only_raw)
                Note: raw versions preserve the original predicate text for better transparency
    """
    if not pred_logic_form or not ground_truth_logic_form:
        return 0.0, [], [], [], [], []
    
    # Handle both single string and list of strings
    if isinstance(pred_logic_form, list):
        pred_str = ' '.join(pred_logic_form)
    else:
        pred_str = pred_logic_form
    
    if isinstance(ground_truth_logic_form, list):
        gt_str = ' '.join(ground_truth_logic_form)
    else:
        gt_str = ground_truth_logic_form
    
    # Get both raw and normalized predicates
    pred_predicates_raw = extract_predicates_raw(pred_str)
    gt_predicates_raw = extract_predicates_raw(gt_str)
    pred_predicates = extract_predicates(pred_str)
    gt_predicates = extract_predicates(gt_str)
    
    # Create a mapping from normalized to raw for better transparency
    # For predicates that differ between raw and normalized
    pred_norm_to_raw = {}
    gt_norm_to_raw = {}
    
    for raw_pred in pred_predicates_raw:
        norm_pred = normalize_predicate(raw_pred)
        pred_norm_to_raw[norm_pred] = raw_pred
    
    for raw_pred in gt_predicates_raw:
        norm_pred = normalize_predicate(raw_pred)
        gt_norm_to_raw[norm_pred] = raw_pred
    
    # Find matching predicates (using normalized forms)
    matching = pred_predicates & gt_predicates
    pred_only_normalized = pred_predicates - gt_predicates
    gt_only_normalized = gt_predicates - pred_predicates
    
    # Get raw versions for display
    pred_only_raw = {pred_norm_to_raw.get(p, p) for p in pred_only_normalized}
    gt_only_raw = {gt_norm_to_raw.get(p, p) for p in gt_only_normalized}
    
    # Calculate similarity as: matching / total unique predicates
    total_unique = len(pred_predicates | gt_predicates)
    
    if total_unique == 0:
        similarity = 0.0
    else:
        similarity = len(matching) / total_unique
    
    return similarity, matching, pred_only_normalized, gt_only_normalized, pred_only_raw, gt_only_raw

def evaluate_logic_forms(predicted_file, ground_truth_file):
    """
    Evaluate predicted logic forms against ground truth.
    
    Args:
        predicted_file: Path to predicted JSON file
        ground_truth_file: Path to ground truth JSON file
    
    Returns:
        dict: Evaluation results
    """
    pred_data = load_json(predicted_file)
    gt_data = load_json(ground_truth_file)
    
    # Create dictionaries keyed by sid for easier lookup
    # Filter out any entries that don't have a 'sid' and record them
    pred_missing_sid = []
    pred_with_sid = []
    pred_capitalized_predicates = {}  # Track capitalized predicates in predictions
    
    for i, item in enumerate(pred_data):
        if isinstance(item, dict) and 'sid' in item:
            pred_with_sid.append(item)
            # Check for capitalized predicates
            logic_form = item.get('logic_form')
            if logic_form:
                lf_str = ' '.join(logic_form) if isinstance(logic_form, list) else logic_form
                has_caps, cap_preds = has_capitalized_predicates(lf_str)
                if has_caps:
                    pred_capitalized_predicates[item['sid']] = cap_preds
        else:
            pred_missing_sid.append({'index': i, 'item': item})

    gt_missing_sid = []
    gt_with_sid = []
    gt_capitalized_predicates = {}  # Check GT for issues too
    
    for i, item in enumerate(gt_data):
        if isinstance(item, dict) and 'sid' in item:
            gt_with_sid.append(item)
            # Check for capitalized predicates (shouldn't happen but good to know)
            logic_form = item.get('logic_form')
            if logic_form:
                lf_str = ' '.join(logic_form) if isinstance(logic_form, list) else logic_form
                has_caps, cap_preds = has_capitalized_predicates(lf_str)
                if has_caps:
                    gt_capitalized_predicates[item['sid']] = cap_preds
        else:
            gt_missing_sid.append({'index': i, 'item': item})

    pred_by_sid = {item['sid']: item for item in pred_with_sid}
    gt_by_sid = {item['sid']: item for item in gt_with_sid}
    
    # Find common sids
    common_sids = set(pred_by_sid.keys()) & set(gt_by_sid.keys())
    pred_only_sids = set(pred_by_sid.keys()) - set(gt_by_sid.keys())
    gt_only_sids = set(gt_by_sid.keys()) - set(pred_by_sid.keys())
    
    # Evaluation metrics
    exact_matches = 0
    exact_match_sids = []
    exact_match_entries = []
    partial_matches = []
    mismatches = []
    
    # Compare logic forms for common sids
    for sid in sorted(common_sids):
        pred_logic = pred_by_sid[sid].get('logic_form')
        gt_logic = gt_by_sid[sid].get('logic_form')
        
        if exact_match(pred_logic, gt_logic):
            exact_matches += 1
            exact_match_sids.append(sid)
            # Build a full entry for exact matches mirroring partial_matches structure
            pred_str = ' '.join(pred_logic) if isinstance(pred_logic, list) else pred_logic
            gt_str = ' '.join(gt_logic) if isinstance(gt_logic, list) else gt_logic
            norm_predicates = extract_predicates(pred_str if pred_str else "")
            exact_match_entries.append({
                'sid': sid,
                'similarity': 1.0,
                'story': gt_by_sid[sid].get('text'),
                'predicted': pred_str,
                'ground_truth': gt_str,
                'matching_predicates': sorted(list(norm_predicates)),
                'predicted_only_predicates': [],
                'ground_truth_only_predicates': [],
                'pred_predicate_count': len(norm_predicates),
                'gt_predicate_count': len(extract_predicates(gt_str if gt_str else ""))
            })
        else:
            similarity, matching, pred_only_norm, gt_only_norm, pred_only_raw, gt_only_raw = similarity_score(pred_logic, gt_logic)
            partial_matches.append({
                'sid': sid,
                'similarity': similarity,
                'story': gt_by_sid[sid].get('text'),  # Original story text (use 'text' field)
                'predicted': ' '.join(pred_logic) if isinstance(pred_logic, list) else pred_logic,
                'ground_truth': ' '.join(gt_logic) if isinstance(gt_logic, list) else gt_logic,
                'matching_predicates': sorted(list(matching)),
                'predicted_only_predicates': sorted(list(pred_only_raw)),  # Use raw versions for clarity
                'ground_truth_only_predicates': sorted(list(gt_only_raw)),  # Use raw versions for clarity
                'pred_predicate_count': len(extract_predicates(' '.join(pred_logic) if isinstance(pred_logic, list) else pred_logic if pred_logic else "")),
                'gt_predicate_count': len(extract_predicates(' '.join(gt_logic) if isinstance(gt_logic, list) else gt_logic if gt_logic else ""))
            })
    
    # Sort partial matches by similarity (lowest first)
    partial_matches.sort(key=lambda x: x['similarity'])
    
    results = {
        'summary': {
            'total_common': len(common_sids),
            'exact_matches': exact_matches,
            'partial_matches': len(partial_matches),
            'predicted_only_count': len(pred_only_sids),
            'ground_truth_only_count': len(gt_only_sids),
            'accuracy': exact_matches / len(common_sids) if common_sids else 0
        },
        'exact_matches': exact_match_entries,
        'predicted_only_sids': sorted(list(pred_only_sids)),
        'ground_truth_only_sids': sorted(list(gt_only_sids)),
        'predicted_entries_missing_sid': pred_missing_sid,
        'ground_truth_entries_missing_sid': gt_missing_sid,
        'predicted_with_capitalized_predicates': pred_capitalized_predicates,
        'ground_truth_with_capitalized_predicates': gt_capitalized_predicates,
        'partial_matches': partial_matches,
        'mismatches': mismatches  # Details for partial matches are in partial_matches
    }
    
    return results

def print_results(results, output_file=None):
    """Print evaluation results in markdown format."""
    
    output_lines = []
    
    # Header
    output_lines.append("# Logic Form Evaluation Results")
    output_lines.append("")
    
    # Summary section
    summary = results['summary']
    output_lines.append("## Summary")
    output_lines.append("")
    output_lines.append("| Metric | Value |")
    output_lines.append("|--------|-------|")
    output_lines.append(f"| Total Common Stories | {summary['total_common']} |")
    output_lines.append(f"| Exact Matches | {summary['exact_matches']}/{summary['total_common']} |")
    output_lines.append(f"| Accuracy | {summary['accuracy']:.2%} |")
    output_lines.append(f"| Partial Matches | {summary['partial_matches']} |")
    output_lines.append(f"| Predicted-only SIDs | {summary['predicted_only_count']} |")
    output_lines.append(f"| Ground Truth-only SIDs | {summary['ground_truth_only_count']} |")
    output_lines.append("")

    # Exact matches (full entries) -- show as formatted blocks like partial matches
    if results.get('exact_matches'):
        output_lines.append("## Exact Matches")
        output_lines.append("")
        output_lines.append(f"Count: {len(results['exact_matches'])}")
        output_lines.append("")
        output_lines.append("**Note:** These entries matched 100% after normalization.")
        output_lines.append("")
        for i, match in enumerate(results['exact_matches'], 1):
            output_lines.append(f"### [{i}] SID: {match['sid']} | Similarity: {match['similarity']:.2%}")
            output_lines.append("")
            if match.get('story'):
                output_lines.append("**Original Story:**")
                output_lines.append("")
                output_lines.append(f"> {match['story']}")
                output_lines.append("")

            output_lines.append("| Metric | Count |")
            output_lines.append("|--------|-------|")
            output_lines.append(f"| Predicted Predicates | {match.get('pred_predicate_count', 0)} |")
            output_lines.append(f"| Ground Truth Predicates | {match.get('gt_predicate_count', 0)} |")
            output_lines.append(f"| Matching Predicates | {len(match.get('matching_predicates', []))} |")
            output_lines.append(f"| Predicted Only | {len(match.get('predicted_only_predicates', []))} |")
            output_lines.append(f"| Ground Truth Only | {len(match.get('ground_truth_only_predicates', []))} |")
            output_lines.append("")
            output_lines.append("---")
            output_lines.append("")
    
    # Capitalized predicates in predicted file (indicates invalid ASP syntax)
    if results.get('predicted_with_capitalized_predicates'):
        output_lines.append("## ⚠️ WARNING: Capitalized Predicates in Predicted File (Invalid ASP)")
        output_lines.append("")
        output_lines.append("The following SIDs have capitalized predicate names, which violates ASP syntax requirements.")
        output_lines.append("Predicates must be lowercase.")
        output_lines.append("")
        for sid, cap_preds in sorted(results['predicted_with_capitalized_predicates'].items()):
            output_lines.append(f"- **SID {sid}**: {', '.join(cap_preds)}")
        output_lines.append("")
    
    # Capitalized predicates in ground truth (shouldn't happen)
    if results.get('ground_truth_with_capitalized_predicates'):
        output_lines.append("## ⚠️ WARNING: Capitalized Predicates in Ground Truth (Needs Fix)")
        output_lines.append("")
        output_lines.append("The following SIDs in the ground truth have capitalized predicate names.")
        output_lines.append("This should not happen in a correct ground truth file.")
        output_lines.append("")
        for sid, cap_preds in sorted(results['ground_truth_with_capitalized_predicates'].items()):
            output_lines.append(f"- **SID {sid}**: {', '.join(cap_preds)}")
        output_lines.append("")
    
    # Predicted only
    if results['predicted_only_sids']:
        output_lines.append("## SIDs in Predicted File Only")
        output_lines.append("")
        output_lines.append(f"Count: {len(results['predicted_only_sids'])}")
        output_lines.append("")
        output_lines.append(f"```\n{results['predicted_only_sids']}\n```")
        output_lines.append("")
    
    # Ground truth only
    if results['ground_truth_only_sids']:
        output_lines.append("## SIDs in Ground Truth Only")
        output_lines.append("")
        output_lines.append(f"Count: {len(results['ground_truth_only_sids'])}")
        output_lines.append("")
        output_lines.append(f"```\n{results['ground_truth_only_sids']}\n```")
        output_lines.append("")
    
    # Partial matches (mismatches)
    if results['partial_matches']:
        output_lines.append("## Partial Matches (Sorted by Similarity)")
        output_lines.append("")
        output_lines.append("_Sorted from lowest to highest similarity_")
        output_lines.append("")
        output_lines.append("**Note:** Predicates shown are in their RAW form as they appear in the logic forms.")
        output_lines.append("The matching logic internally normalizes predicates (e.g., customer(x) becomes person(x),")
        output_lines.append("quotes added to unquoted args, articles removed, etc.) for semantic equivalence checking.")
        output_lines.append("")
        
        for i, match in enumerate(results['partial_matches'], 1):
            output_lines.append(f"### [{i}] SID: {match['sid']} | Similarity: {match['similarity']:.2%}")
            output_lines.append("")
            
            # Original story text
            if match.get('story'):
                output_lines.append("**Original Story:**")
                output_lines.append("")
                output_lines.append(f"> {match['story']}")
                output_lines.append("")
            
            # Metrics
            output_lines.append("| Metric | Count |")
            output_lines.append("|--------|-------|")
            output_lines.append(f"| Predicted Predicates | {match['pred_predicate_count']} |")
            output_lines.append(f"| Ground Truth Predicates | {match['gt_predicate_count']} |")
            output_lines.append(f"| Matching Predicates | {len(match['matching_predicates'])} |")
            output_lines.append(f"| Predicted Only | {len(match['predicted_only_predicates'])} |")
            output_lines.append(f"| Ground Truth Only | {len(match['ground_truth_only_predicates'])} |")
            output_lines.append("")
            
            if match['predicted_only_predicates']:
                output_lines.append("**In Predicted but NOT in GT:**")
                output_lines.append("")
                for pred in match['predicted_only_predicates'][:5]:
                    output_lines.append(f"- `{pred}`")
                if len(match['predicted_only_predicates']) > 5:
                    output_lines.append(f"- ... and {len(match['predicted_only_predicates']) - 5} more")
                output_lines.append("")
            
            if match['ground_truth_only_predicates']:
                output_lines.append("**In GT but NOT in Predicted:**")
                output_lines.append("")
                for pred in match['ground_truth_only_predicates'][:5]:
                    output_lines.append(f"- `{pred}`")
                if len(match['ground_truth_only_predicates']) > 5:
                    output_lines.append(f"- ... and {len(match['ground_truth_only_predicates']) - 5} more")
                output_lines.append("")
            
            output_lines.append("---")
            output_lines.append("")
    
    # Print to console
    output_text = "\n".join(output_lines)
    print(output_text)
    
    # Save to file if specified
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output_text)
        print(f"\nResults saved to: {output_file}")

def save_json_results(results, output_file):
    """Save results as JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"JSON results saved to: {output_file}")

if __name__ == "__main__":
    # Define paths
    project_root = Path(__file__).parent.parent
    
    # Input folder containing JSON files to evaluate
    input_folder = project_root / "experiments" / "FewShot" / "Results" / "FewShot_10_Random_V1"
    # input_folder = project_root / "experiments" / "FewShot" / "Results" / "FewShot_10_Random_V2"
    # input_folder = project_root / "experiments" / "FewShot" / "Results" / "Manual_Prompting"
    # input_folder = project_root / "experiments" / "FewShot" / "Results" / "ZeroShot_V1"
    
    
    # Ground truth file
    ground_truth_file = project_root / "encodedForm" / "fixed_all_combined.json"
    
    # Create output base directory
    evaluation_base = project_root / "experiments" / "Evaluation"
    evaluation_base.mkdir(parents=True, exist_ok=True)
    
    # Create output subdirectory named after the input folder
    parent_folder_name = input_folder.name.lower()
    output_dir = evaluation_base / parent_folder_name
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all JSON files in the input folder
    json_files = sorted(input_folder.glob("*.json"))
    
    if not json_files:
        print(f"No JSON files found in {input_folder}")
    else:
        print(f"Found {len(json_files)} JSON file(s) to evaluate")
        print(f"Input folder: {input_folder}")
        print(f"Output folder: {output_dir}")
        print(f"Ground truth: {ground_truth_file}")
        print("")
        
        # Evaluate each JSON file
        for predicted_file in json_files:
            print(f"\n{'='*70}")
            print(f"Evaluating: {predicted_file.name}")
            print(f"Against: {ground_truth_file.name}")
            print(f"{'='*70}\n")
            
            results = evaluate_logic_forms(predicted_file, ground_truth_file)
            
            # Print results to console
            print_results(results)
            
            # Save results with shorter names
            file_stem = predicted_file.stem
            json_output = output_dir / f"{file_stem}_evaluated.json"
            md_output = output_dir / f"{file_stem}_evaluated.md"
            
            save_json_results(results, json_output)
            print_results(results, md_output)
            print(f"[OK] {predicted_file.name} complete\n")
