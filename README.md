# Restaurant Scenario → Logic Form Generation and Evaluation

This repository contains the data, code, and experiment artifacts for generating and
evaluating **structured logic forms** from restaurant-visit story scenarios using
several large language models (LLMs), including few-shot and zero-shot prompting.

It is a fresh public release created to address **reproducibility** requests for the
corresponding paper.

## Note on this repository

This is a fresh public release created to address reproducibility requests for the
paper. To comply with the distribution terms of the **ROCStories** corpus
(Mostafazadeh et al., 2016), which is gated behind a registration form and does not
specify redistribution terms, the raw ROCStories text used in this work is **not**
included in this repository. Records derived from ROCStories are instead referenced
by their original `storyid`; [`RECONSTRUCTION.md`](RECONSTRUCTION.md) documents how to
obtain the corpus and regenerate the identical inputs. All derived annotations (logic
forms), model outputs, evaluation scores, and non-ROC data are included in full.

## Repository layout

```
code/                          Scripts and notebooks (dataset loading, annotation, evaluation)
encodedForm/fixed_all_combined.json   The 100-record evaluation dataset (sid 0..99)
expReadyData/                  Dataset variants ready for experiments
experiments/FewShot/inputs/    Few-shot experiment inputs
experiments/FewShot/Results/   Few-shot model outputs
experiments/Evaluation/        Manual and automated evaluation artifacts
experiments/StoryGeneration/   LLM-generated stories
experiments/ZeroShot/          Zero-shot outputs
experiments/thesis_docs/       Paper / writing sources
restaurant_data/               Synthetic restaurant-scenario corpus (non-ROC)
manifest_roc.json              storyid mapping for ROCStories-derived records
RECONSTRUCTION.md              How to obtain/reconstruct ROCStories-derived records
```

## Dataset

The canonical evaluation dataset is `encodedForm/fixed_all_combined.json`, containing
100 records:

| sid range   | Origin                                   | Included in this repo |
|-------------|------------------------------------------|-----------------------|
| 0–39        | Restaurant narrative corpus of Inclezan et al. | Yes (full text)       |
| 40–74       | Synthetic / LLM-derived scenarios        | Yes (full text)       |
| 75–99       | ROCStories (via `storyid`)               | Text redacted, `storyid` kept |

Each record has:

- `sid` — dataset index
- `text` — the story (redacted for ROCStories-derived records)
- `logic_form` — the structured logic-form annotation
- `scenario_type` — `Normal`, `Exception`, or `Variation`
- `storyid` / `storytitle` — present only for ROCStories-derived records

The 40 stories with sids `0–39` come from the restaurant narrative corpus of Inclezan
et al. [1][2], which already provides ground-truth ASP logic forms for these
scenarios. Their full text is included in this repository.

See [`RECONSTRUCTION.md`](RECONSTRUCTION.md) and [`manifest_roc.json`](manifest_roc.json)
for how to recover the redacted texts from the official ROCStories corpus.

## Reproducing the experiments

1. Obtain the ROCStories corpus and reconstruct the redacted texts as described in
   [`RECONSTRUCTION.md`](RECONSTRUCTION.md).
2. Reassemble the records into `encodedForm/fixed_all_combined.json` using the
   pipeline in `code/` (keyword filter → manual selection → SID reindex).
3. Re-run the few-shot / zero-shot pipelines under `experiments/` using the prompts
   and model outputs included there.

Aggregate results and per-story model outputs are included under
`experiments/Evaluation/` and `experiments/FewShot/Results/`.

## References

[1] Daniela Inclezan, Qinglin Zhang, Marcello Balduccini, and Ankush Israney.
*Understanding Restaurant Stories Using an ASP Theory of Intentions*. International
Conference on Logic Programming (ICLP), 2017.

[2] Qinglin Zhang, Chris Benton, and Daniela Inclezan. *An Application of ASP Theories
of Intentions to Understanding Restaurant Scenarios: Insights and Narrative Corpus*.
Theory and Practice of Logic Programming, 19(2):273–293, 2019.

[3] Nasrin Mostafazadeh, Nathanael Chambers, Xiaodong He, Devi Parikh, Dhruv Batra,
Lucy Vanderwende, Pushmeet Kohli, James Allen. *A Corpus and Evaluation Framework for
Deeper Understanding of Commonsense Stories*. NAACL-HLT 2016.

If you use this work, please cite the paper (see `experiments/thesis_docs/`) and, where
applicable, the corpora listed above.
