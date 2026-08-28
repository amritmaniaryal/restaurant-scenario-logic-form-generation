---
marp: true
theme: uncover
class: invert
paginate: true
---

<!-- _class: lead invert -->

# **LLM-to-ASP**
## Translating Natural Language Narratives into Answer Set Programs

**Amrit Aryal**
Miami University

---

<!-- _class: default -->

# **Human Narratives**

People tell stories every day — in conversations, reviews, news, reports.

**Example (sid 2):**
> "John enters the restaurant. The waiter escorts him to a table. John orders steak. The waiter brings the steak to the table. John asks for the bill, and the waiter brings it to the table. John pays the bill and leaves the restaurant."

Narratives are **natural**, **unstructured**, and **rich with meaning** — who did what, when, where, and why.

But computers can't reason over raw text alone.

---

# **From Text to Understanding**

To reason about a story, we need to extract:

| Question | Information |
|----------|-------------|
| Who is involved? | John, waiter |
| What happened? | Enter, escort, order, bring, request, pay, leave |
| What did they order? | Steak |
| What's the order? | Enter → seat → order → bring → request bill → pay → leave |

This structure enables a computer to **answer questions**, **detect anomalies**, and **draw conclusions** — but it requires a **formal representation**.

---

# **What is Answer Set Programming?**

- Declarative logic programming paradigm for **knowledge representation & reasoning**
- Programs consist of rules of the form: `head :- body.`
- Solver (e.g., **clingo**) computes stable models (answer sets)
- Used for planning, diagnosis, configuration, commonsense reasoning

**John's story in ASP:**
```prolog
restaurant("the restaurant"). customer("John"). food("steak").
waiter("the waiter"). story_step(0..7).
st_hpd(enter("John", "the restaurant"), true, 0).
st_hpd(lead_to("the waiter", "John", t), true, 1).
st_hpd(order("John", "steak", "the waiter"), true, 2).
st_hpd(put_down("the waiter", "steak", t), true, 3).
st_hpd(request("John", b, "the waiter"), true, 4).
st_hpd(put_down("the waiter", b, t), true, 5).
st_hpd(pay("John", b), true, 6).
st_hpd(leave("John"), true, 7).
```

Combined with ASP reasoning rules, these logic forms serve as input for **executable programs** — a computer can reason with them.

---

# **The Knowledge Acquisition Bottleneck**

ASP is powerful — but **writing it requires formal logic expertise**.

```
"John enters the restaurant.
The waiter escorts him to a table..."
```

<span style="color: #888">⇓</span>

```prolog
customer("John"). waiter("the waiter").
story_step(0..1).
st_hpd(enter("John", "the restaurant"), true, 0).
st_hpd(lead_to("the waiter", "John", t), true, 1).
```

This gap — **natural language → structured formal representation** — is the **knowledge acquisition bottleneck**.

- Domain experts don't know ASP
- ASP experts don't know every domain
- Manual encoding does not scale

---

# **LLMs: A Bridge from Text to Logic**

Large Language Models have shown remarkable ability to translate natural language into structured outputs — code, SQL, JSON.

**Can they bridge the NL → ASP gap?**

If successful:
- Non-specialists could describe scenarios in plain English
- LLMs would automatically convert narratives into ASP-compatible logic forms
- Dramatically lowers the barrier to formal commonsense reasoning

This is the central question of our work.

---

# **Research Questions**

| # | Question |
|---|----------|
| **RQ1** | Is an LLM-based NL→ASP translation pipeline feasible? |
| **RQ2** | How do ChatGPT, Gemini, and DeepSeek compare? |
| **RQ3** | Which prompting strategy (few-shot count × documentation) yields best results? |
| **RQ4** | What are the syntactic and semantic failure modes? |

---

# **Dataset**

**100 restaurant-visit narratives** (1–5 sentences each), manually authored

| Category | Description | Example |
|----------|-------------|---------|
| **Normal** | Standard dining scenario | "Alice enters, sits, orders a burger." |
| **Exception** | Something goes wrong | Wrong dish, complaint, cancellation |

- Each story has a **manually verified ground-truth ASP encoding**
- Characters with varied properties: groups, couples, solo diners, children
- Additional stories from **ROCStories** corpus (filtered for restaurant keywords)

---

# **ASP Predicate Ontology**

**Entity Predicates**
```
restaurant/1, customer/1, person/1, food/1, waiter/1, cook/1, host/1
```

**Fluents** — observable states (`st_obs/3`)
```
sitting/1, hungry/1, paid/1, served/1, menu_read/1, available/2
```

**Actions** — events (`st_hpd/3`)
```
enter/2, sit/1, order/3, eat/2, drink/2, pay/2, leave/1, complain/2
```

**Grouping:** `member/2` for customers sharing an order
**Constants:** `t` (table), `b` (bill), `r` (restaurant), `w` (waiter), `f` (food)

---

# **Models Tested**

| Model | API Version | Web Version |
|-------|-------------|-------------|
| **ChatGPT** | GPT-5 (OpenRouter) | GPT-5.1 |
| **Gemini** | Gemini 2.5 Pro (OpenRouter) | Gemini 3.0 Pro |
| **DeepSeek** | DeepSeek V3.1 (OpenRouter) | DeepSeek V3.2 |

*Auxiliary:* GPT-4o, Gemini Flash 2.5, Gemini Flash 3.0

---

# **Experimental Conditions**

6 conditions crossing **exemplar count** × **supplementary docs**

| Condition | Shots | `output_expectations.md` | `additional_info.md` | Targets |
|-----------|-------|--------------------------|----------------------|---------|
| ZeroShot-V1 | 0 | ✓ | ✓ | 100 |
| FewShot-5-Random-V1 | 5 (random) | ✓ | ✗ | 95 |
| FewShot-5-Random-V2 | 5 (random) | ✓ | ✓ | 95 |
| FewShot-10-Random-V1 | 10 (random) | ✓ | ✗ | 90 |
| FewShot-10-Random-V2 | 10 (random) | ✓ | ✓ | 90 |
| Manual-Prompting (web) | 10 (random) | ✓ | ✓ | 100 |

---

# **Prompt Architecture**

- **System persona:** *"You are a precise ASP logic translator. You never skip data."*
- **Output format:** Strict JSON with escaped quotes, mandatory completeness
- **Temperature:** `0.0` (deterministic)
- **max_tokens:** 32,000
- **Batch processing:** 10 stories per API call; examples re-injected in every batch
- **API:** OpenRouter (OpenAI-compatible)
- **JSON repair layer** using `json-repair` library
- **Retry:** up to 2 automatic retries on failure

---

# **Supplementary Docs**

Two documents embedded in every prompt:

### `output_expectations.md`
- Complete predicate inventory with arities
- All valid constants (`t`, `b`, `r`, `w`, `f`, `tip`)
- Full fluent and action lists
- JSON formatting rules & examples

### `additional_info.md`
- No inferred actions
- Correct negation formatting (`not` vs `-`)
- Role compression rules
- Unspecified-food handling (`f` constant)
- Prohibition of `story_step/1`

---

# **Evaluation: Syntactic Validity**

### Stage 1 (Automated)
- Each generated encoding is fed to the **clingo parser**
- `clingo.Control.add()` + `.ground()` — passes if no parse error
- Binary outcome: **parsable** or **not parsable**
- Enables large-scale automated screening

This stage filters out malformed outputs before semantic evaluation.

---

# **Evaluation: Semantic Accuracy**

### Stage 2 (Manual)
- ~30 stories per condition scored 0–5 by the author

| Score | Meaning |
|-------|---------|
| **5** | Exact match to ground truth |
| **4.5** | Better than ground truth |
| **4** | Pass (functionally correct) |
| **3** | Partial (multiple substantive mistakes) |
| **2–0** | Failing |

**Pass threshold:** score ≥ **4**

---

# **Semantic Evaluation Sampling**

**Why sample?**
- Manual scoring (0–5 rubric) is labor-intensive
- ~90–100 outputs per condition × 3 models × 6 conditions = ~1,700+ possible — infeasible to score all

**Method:**
- **30 stories sampled per condition** — stratified across an automated coarse-similarity score
- Each story scored separately for **all 3 models** → **30 scores per model** per condition
- Total: ~30 SIDs × 3 models × 6 conditions = **~540 manual annotations**

**Why stratified sampling?**
- A random sample could miss edge cases
- Stratifying by similarity scores ensures coverage of the **full quality spectrum** — from exact matches to complete failures
- Produces reliable pass rate estimates without exhaustive annotation

---

# **Syntactic Parsability Results**

| Condition | ChatGPT 5.0 | DeepSeek V3.1 | Gemini 2.5 Pro |
|-----------|:-----------:|:-------------:|:--------------:|
| ZeroShot-V1 | 80.0% | **99.0%** | 80.0% |
| FewShot-5-Random-V1 | **100.0%** | 77.9% | **100.0%** |
| FewShot-5-Random-V2 | **100.0%** | 84.2% | **100.0%** |
| FewShot-10-Random-V1 | **100.0%** | 96.7% | **100.0%** |
| FewShot-10-Random-V2 | **100.0%** | **100.0%** | **100.0%** |
| **Weighted Avg** | **95.7%** | **91.5%** | **95.7%** |

All three models achieved **100% syntactic parsability** in the FewShot-10-Random-V2 condition.

---

# **Semantic Pass Rates (score ≥ 4)**

| Condition | ChatGPT 5.0 | Gemini 2.5 Pro | DeepSeek V3.1 |
|-----------|:-----------:|:--------------:|:-------------:|
| ZeroShot-V1 | 20.0% | 0.0% | 20.0% |
| FewShot-5-Random-V1 | 63.3% | 53.3% | 50.0% |
| FewShot-5-Random-V2 | 60.0% | **90.0%** | 43.3% |
| FewShot-10-Random-V1 | **75.9%** | 72.4% | 37.9% |
| FewShot-10-Random-V2 | **82.8%** | 79.3% | 48.3% |
| Manual-Prompting (web) | 30.0% | 80.0% | 60.0% |

ChatGPT peaks at **82.8%**, Gemini at **90.0%**, DeepSeek caps at **60.0%**.

---

# **Key Findings — RQ1 & RQ2**

### RQ1: Pipeline Feasibility
**YES** — under the right conditions (10-shot + both docs), ChatGPT and Gemini both exceed **79% semantic accuracy** with **100% syntactic parsability**.

### RQ2: Model Comparison
**Condition-dependent:**
- **ChatGPT** leads in high-exemplar API settings (83% in 10-shot V2)
- **Gemini** leads when strong documentation + moderate exemplars (90% in 5-shot V2)
- **DeepSeek** never surpassed 60% in API conditions

---

# **Key Findings — RQ3 & RQ4**

### RQ3: Prompting Strategy
The **combination** of exemplar count **AND** documentation matters most:
- **Gemini:** documentation > exemplars
- **ChatGPT:** exemplars > documentation
- **DeepSeek:** highly sensitive — more examples sometimes degrade performance

### RQ4: Failure Modes

**Syntactic (6 modes):**
Missing periods · Unsafe free variables · Chinese character corruption
Incorrect predicates · Stray punctuation · Missing output

**Semantic:**
Action omission · Predicate invention · Predicate confusion
Timestep errors · Missing `member/2` · Missing `st_next`

---

# **Notable Anomaly: Chinese Character Corruption**

### DeepSeek — `极` Insertion

- **12 of 95** outputs corrupted with the Chinese character `极`
- Appeared in predicate names, string literals, and numeric arguments
- Occurred **only** when `additional_info.md` was added to the 5-shot prompt
- Bizarre **token-level hallucination** from prompt destabilization

A new doc was added without adequate exemplar stabilization.

---

# **Notable Anomalies: Web & Documentation Effects**

### Web Hallucination (ChatGPT 5.1)
- **Catastrophically fabricated** entirely unrelated stories in final conversational chunk
- 30% pass rate vs Gemini 3.0's robust **80%**
- Batched API pipeline proven far more reliable

### Gemini's 37-Point Jump
- 53% (5-shot V1) → **90%** (5-shot V2)
- Triggered by adding `additional_info.md`
- **Single largest improvement** across all conditions

---

# **U-Shaped DeepSeek Trajectory**

DeepSeek's syntactic parsability across conditions:

```
ZeroShot       →  99%  (no examples, most reliable)
5-Shot V1      →  78%  (examples destabilize output)
5-Shot V2      →  84%  (docs help partially)
10-Shot V1     →  97%  (more examples stabilize)
10-Shot V2     → 100%  (examples + docs converge)
```

**More examples sometimes hurt performance** — a counterintuitive finding.

---

# **Best Configuration**

## FewShot-10-Random-V2
### 10 random examples + both supplementary docs

| Metric | ChatGPT | Gemini | DeepSeek |
|--------|:-------:|:------:|:--------:|
| Syntactic | **100%** | **100%** | **100%** |
| Semantic | **82.8%** | **79.3%** | 48.3% |

- Only condition where **all 3 models** achieved 100% syntactic parsability
- Represents the **proven reliable pipeline configuration**

---

# **Conclusions**

1. LLMs **can** reliably translate NL into ASP-compatible logic forms under optimal prompting conditions
2. No single "best" model — performance is **condition-dependent**
3. **Prompt engineering matters**: both exemplar count and documentation design
4. The **knowledge acquisition bottleneck** can be significantly reduced
5. Web interfaces are **unreliable** vs batched API pipelines
6. Failure modes are **systematic** and potentially correctable

---

# **Future Work**

- **Expand domains** beyond restaurant narratives
- **Larger-scale evaluation** with more annotators
- **Automated semantic checking** to reduce manual annotation burden
- **Failure mitigation** — targeted post-processing for known error patterns
- **Chain-of-thought** and other advanced prompting strategies
- **Fine-tuning** specialized models for NL→ASP translation

---

<!-- _class: lead invert -->

# **Thank You**

**Questions?**

Amrit Maniam — University of Miami

---

<!-- _class: default -->

# **Appendix: Related Work**

- **NL→Code translation** (Codex, StarCoder, etc.)
- **LLMs for formal logic** (Theorem proving, SAT solving)
- **ASP in NLP** (Event parsing, temporal reasoning)
- **Prompt engineering** (Few-shot learning, chain-of-thought)

---

# **Appendix: Evaluation Criteria Details**

**Score** | **Criteria**
:-------:|-------------
5 | Perfect match to ground truth
4.5 | Better than ground truth (catches author omission)
4 | Functionally correct — all key predicates present
3 | Partial — multiple substantive errors
2 | Major errors — story not captured
1 | Mostly unrelated output
0 | Empty / unparseable

**Pass threshold: ≥ 4**
