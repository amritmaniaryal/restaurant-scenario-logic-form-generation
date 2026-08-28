"""Convert the restaurant narrative corpus from XML to JSON.

Reads ``restaurant_data/restaurant_corpus.xml.htm`` and writes
``restaurant_data/restaurant_corpus_initial.json`` — the 40 Inclezan et al.
scenarios behind sids 0-39 in ``encodedForm/fixed_all_combined.json``.
"""
import xml.etree.ElementTree as ET
import json
import re

def clean_text(text):
    """Clean whitespace and newlines from text content."""
    if text is None:
        return ""
    return re.sub(r'\s+', ' ', text.strip())

def parse_logic_form(logic_text):
    """Parse logic_form into a list of statements."""
    if not logic_text:
        return []
    # Split by newline and clean each line
    lines = [line.strip() for line in logic_text.split('\n') if line.strip()]
    return lines

def xml_to_json(xml_file, json_file):
    # Parse XML
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    stories = []
    
    for story_elem in root.findall('story'):
        story = {}
        
        # Extract sid
        sid_elem = story_elem.find('sid')
        story['sid'] = int(clean_text(sid_elem.text)) if sid_elem is not None else None
        
        # Extract text
        text_elem = story_elem.find('text')
        story['text'] = clean_text(text_elem.text) if text_elem is not None else ""
        
        # Extract source
        source_elem = story_elem.find('source')
        story['source'] = clean_text(source_elem.text) if source_elem is not None else ""
        
        # Extract logic_form
        logic_elem = story_elem.find('logic_form')
        logic_text = clean_text(logic_elem.text) if logic_elem is not None else ""
        story['logic_form'] = parse_logic_form(logic_text)
        
        # Extract scenario_type
        scenario_elem = story_elem.find('scenario_type')
        story['scenario_type'] = clean_text(scenario_elem.text) if scenario_elem is not None else ""
        
        stories.append(story)
    
    # Write to JSON file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(stories, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    xml_file = '../restaurant_data/restaurant_corpus.xml.htm'
    json_file = '../restaurant_data/restaurant_corpus_initial.json'
    
    xml_to_json(xml_file, json_file)
    print(f"Converted {xml_file} to {json_file}")