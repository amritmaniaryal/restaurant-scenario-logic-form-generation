# Reconstruction Guide: ROCStories-derived records

## Why this document exists

Part of the dataset used in this work is derived from the **ROCStories** corpus
(Mostafazadeh et al., *A Corpus and Evaluation Framework for Deeper Understanding
of Commonsense Stories*, NAACL-HLT 2016).

The raw ROCStories text is **not** redistributed in this repository. ROCStories is
obtained via a registration form on the official website and its distribution terms
are not explicitly specified, so we deliberately publish only:

- the original `storyid` and `storytitle` of every ROCStories-derived record
  (see [`manifest_roc.json`](manifest_roc.json)), and
- all of our own derived annotations, model outputs, and evaluation scores.

Every raw story text field that originally came from ROCStories is replaced in this
repository by a placeholder of the form:

```
[REDACTED — original ROCStories text; storyid=<uuid>]
```

## Obtaining the original corpus

1. Go to the official ROCStories page: <https://www.cs.rochester.edu/nlp/rocstories/>
2. Complete the access request form (the dataset is free to everyone).
3. You will receive the corpus as a CSV with columns
   `storyid, storytitle, sentence1, sentence2, sentence3, sentence4, sentence5`.

The release of the corpus used in this work was downloaded in 2025
(`other_data/ROCStories.csv` in the private repository, 52,665 rows). To reproduce
the exact records, use the same release.

## Reconstructing a single story

For any `storyid` listed in [`manifest_roc.json`](manifest_roc.json):

1. Look up the row in the corpus CSV by `storyid`.
2. Concatenate `sentence1` .. `sentence5` in order, joined by spaces.
3. The result is the story text that appears (redacted) in this repository.

Example (illustrative, fictional — not an actual ROCStories record):

```text
storyid:       00000000-0000-0000-0000-000000000000
storytitle:    A Sample Visit
sentence1:     Pat walked into the coffee shop at noon.
sentence2:     Pat ordered a large latte and a pastry.
sentence3:     The cashier handed over the order quickly.
sentence4:     Pat drank the latte and ate the pastry.
sentence5:     Pat left the shop feeling refreshed.
```

## Automated reconstruction and re-masking

Two helper scripts automate the round-trip so the redacted texts can be restored
for re-running experiments and re-redacted before any commit:

```bash
# 1) Restore the redacted texts using a locally-obtained official corpus:
python code/reconstruct_roc_texts.py --csv other_data/ROCStories.csv

# 2) ... run the experiments ...

# 3) Re-mask the ROCStories texts before committing (no CSV needed):
python code/mask_roc_texts.py
```

- `reconstruct_roc_texts.py` replaces every `[REDACTED — …storyid=<uuid>]`
  placeholder with the story text joined from `sentence1..5` for that `storyid`.
  It refuses to run if any placeholder or manifest `storyid` is missing from the
  supplied CSV. Add `--check` to validate without modifying files.
- `mask_roc_texts.py` redacts the story text of every ROCStories-derived record
  (sids 75–99) back to the placeholder, using `manifest_roc.json`. It only touches
  dataset-family files (`encodedForm/`, `experiments/FewShot/inputs/`,
  `experiments/FewShot/Results/`) and the evaluated output files. Add `--check`
  for a dry run.

## How these records became part of the dataset

The full pipeline (see `code/load_ROC_strs.py` and the notebooks in `code/`):

1. **Non-ROC records**: sids `0–39` are taken from the restaurant narrative corpus of
   Inclezan et al. (Inclezan et al., 2017; Zhang et al., 2019), which provides
   ground-truth ASP logic forms for these scenarios.
2. **Filter**: `load_ROC_strs.py` reads the ROCStories corpus CSV and keeps only
   stories whose title matches restaurant-related keywords.
3. **Manual selection**: 25 restaurant stories were manually selected from that
   filtered subset for inclusion in the evaluation dataset.
4. **Annotation**: each selected story was manually encoded into a structured logic
   form (`logic_form`) and assigned a `scenario_type` (`Normal`, `Exception`, or
   `Variation`). These annotations are ours and are included in full.
5. **SID assignment**: records were combined with the non-ROC stories and the combined
   list was sorted and re-indexed to continuous `sid` values `0..99`. The 25
   ROCStories-derived records occupy **sids 75–99** (see `manifest_roc.json`).

The six ROCStories-derived records that appear in the manual evaluation are
sids **75, 77, 86, 90, 91, 95**.

## Verification

To confirm the placeholder text matches the original, reconstruct the story from the
corpus as described above and compare it to the `storytitle` / logic-form content in
this repository. The `storyid` is the authoritative join key.

## References

- Daniela Inclezan, Qinglin Zhang, Marcello Balduccini, and Ankush Israney.
  *Understanding Restaurant Stories Using an ASP Theory of Intentions*. International
  Conference on Logic Programming (ICLP), 2017.
- Qinglin Zhang, Chris Benton, and Daniela Inclezan. *An Application of ASP Theories
  of Intentions to Understanding Restaurant Scenarios: Insights and Narrative Corpus*.
  Theory and Practice of Logic Programming, 19(2):273–293, 2019.
