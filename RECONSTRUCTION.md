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

Example (row from the official corpus):

```text
storyid:       99d073a9-375a-45ad-a070-0fdfbbf73f69
storytitle:    Going out for Sushi.
sentence1:     Today I had a dinner date with my husband.
sentence2:     We decided to try out a new Sushi place near our home.
sentence3:     It was very crowded but we had a reservation.
sentence4:     We ordered spicy tuna rolls and eel and enjoyed some time alone.
sentence5:     The food great, we both agreed we would go back again.
```

## How these records became part of the dataset

The full pipeline (see `code/load_ROC_strs.py` and the notebooks in `code/`):

1. **Filter**: `load_ROC_strs.py` reads the corpus CSV and keeps only stories whose
   title matches restaurant-related keywords.
2. **Manual selection**: 25 restaurant stories were manually selected from that
   filtered subset for inclusion in the evaluation dataset.
3. **Annotation**: each selected story was manually encoded into a structured logic
   form (`logic_form`) and assigned a `scenario_type` (`Normal`, `Exception`, or
   `Variation`). These annotations are ours and are included in full.
4. **SID assignment**: records were combined with non-ROC stories and the combined
   list was sorted and re-indexed to continuous `sid` values `0..99`. The 25
   ROCStories-derived records occupy **sids 75–99** (see `manifest_roc.json`).

The six ROCStories-derived records that appear in the manual evaluation are
sids **75, 77, 86, 90, 91, 95**.

## Verification

To confirm the placeholder text matches the original, reconstruct the story from the
corpus as described above and compare it to the `storytitle` / logic-form content in
this repository. The `storyid` is the authoritative join key.
