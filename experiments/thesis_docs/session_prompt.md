# Session Prompt for opencode

Copy the text below into a new opencode session.

---

You are helping me write a conference paper condensed from my Master's thesis (MSCS).
The paper is titled **"From Narratives to Reasoning: Assessing LLMs on Logic Form Generation"**
and targets **IJCLR 2026** (deadline: June 15, 2026; 15 pages including references).

## Authoritative sources
- **Paper (ground truth):** `thesis_docs/ijclr2026.tex` -- the LaTeX file we are actively writing.
- **Thesis (reference):** `thesis_docs/Amrit_thesis_draft.pdf` -- the full thesis; consult for detail when needed.
- **Experiment code:** `Scripts/exp.ipynb` and `Scripts/master_config.yaml`.
- **Experiment results:** `Evaluation/` folder (syntactic parsability, semantic scores, figures).
- **Dataset/Prompts:** `FewShot/` folder (inputs, docs, results).

## Experiment summary
Three LLMs (GPT-5, Gemini 2.5 Pro, DeepSeek V3.1 via OpenRouter API) are evaluated on translating
100 English restaurant-visit narratives into ASP logic forms. Six conditions cross shot count
(0/5/10) with presence/absence of an encoding guide (`additional_info.md`), plus one web-based trial.

## Paper structure and status
- **Section 1 (Introduction):** Daniela will write. Do not touch.
- **Section 2 (Related Work):** Daniela will write. Do not touch.
- **Section 3 (Methodology):** Drafted. 3.1 Model Selection, 3.2 Data Sets, 3.3 Experiment Details.
- **Section 4 (Evaluation and Results):** Drafted in .tex but may need review/revision.
- **Section 5 (Conclusions and Future Work):** Drafted.
- **References:** `thesis_docs/ijclr2026.bib`.

## Style rules
- Avoid em dashes (associated with AI writing).
- Be concise; this is a conference paper with a page limit.
- Use the LaTeX template (`llncs` document class).
- Follow existing conventions in `ijclr2026.tex` for table/figure formatting, citation style, etc.
