# LLM-to-ASP: Translating Natural Language Narratives into Answer Set Programs

Amrit Aryal — Miami University

---

# Problem Statement

**Answer Set Programming (ASP)** is a powerful formalism for commonsense reasoning --- but requires formal logic expertise.

**Can Large Language Models (LLMs)** reliably translate unstructured restaurant-visit narratives into ASP-compatible logic forms?

- The barrier to entry for ASP is high
- If LLMs can bridge NL to logic, it would dramatically lower the barrier
- Non-specialists could create formal logic representations from plain text

---

# What is Answer Set Programming?

- Declarative logic programming paradigm for **knowledge representation and reasoning**
- Programs consist of rules of the form: `head :- body.`
- Solver (e.g., **clingo**) computes stable models (answer sets)
- Used for planning, diagnosis, configuration, commonsense reasoning

**Example:**
```
person(alice).  restaurant(r1).  sit(alice).
enter(alice, r1).  st_hpd(enter(alice, r1), 1).
```

---

# Research Questions

- **RQ1:** Is an LLM-based NL to ASP translation pipeline feasible?
- **RQ2:** How do ChatGPT, Gemini, and DeepSeek compare?
- **RQ3:** Which prompting strategy (few-shot count x documentation) yields best results?
- **RQ4:** What are the syntactic and semantic failure modes?

---

# Dataset

**100 restaurant-visit narratives** (1--5 sentences each), manually authored

| Category | Description | Example |
|----------|-------------|---------|
| Normal | Standard dining scenario | Alice enters, sits, orders a burger |
| Exception | Something goes wrong | Wrong dish, complaint, cancellation |

- Each story has a **manually verified ground-truth ASP encoding**
- Characters: groups, couples, solo diners, children
- Additional stories from **ROCStories** corpus

---

# ASP Predicate Ontology

**Entity Predicates:**
`restaurant/1, customer/1, person/1, food/1, waiter/1, cook/1, host/1`

**Fluents** --- observable states (`st_obs/3`):
`sitting/1, hungry/1, paid/1, served/1, menu_read/1, available/2`

**Actions** --- events (`st_hpd/3`):
`enter/2, sit/1, order/3, eat/2, drink/2, pay/2, leave/1, complain/2`

**Grouping:** `member/2` **Constants:** `t` (table), `b` (bill), `r` (restaurant), `w` (waiter), `f` (food)

---

# Models Tested

| Model | API Version | Web Version |
|-------|-------------|-------------|
| ChatGPT | GPT-5 (OpenRouter) | GPT-5.1 |
| Gemini | Gemini 2.5 Pro (OpenRouter) | Gemini 3.0 Pro |
| DeepSeek | DeepSeek V3.1 (OpenRouter) | DeepSeek V3.2 |

Auxiliary: GPT-4o, Gemini Flash 2.5, Gemini Flash 3.0

---

# Experimental Conditions

Six conditions crossing exemplar count with supplementary docs

| Condition | Shots | Doc A | Doc B | Targets |
|-----------|-------|-------|-------|---------|
| ZeroShot-V1 | 0 | Yes | Yes | 100 |
| FewShot-5-Random-V1 | 5 (random) | Yes | No | 95 |
| FewShot-5-Random-V2 | 5 (random) | Yes | Yes | 95 |
| FewShot-10-Random-V1 | 10 (random) | Yes | No | 90 |
| FewShot-10-Random-V2 | 10 (random) | Yes | Yes | 90 |
| Manual-Prompting (web) | 10 (random) | Yes | Yes | 100 |

Doc A: `output_expectations.md`, Doc B: `additional_info.md`

---

# Prompt Architecture

- **System persona:** "You are a precise ASP logic translator. You never skip data."
- **Output format:** Strict JSON with escaped quotes, mandatory completeness
- **Temperature:** 0.0 (deterministic)
- **max_tokens:** 32,000
- **Batch processing:** 10 stories per API call; examples re-injected in every batch
- **API:** OpenRouter (OpenAI-compatible) with json-repair library
- **Retry:** up to 2 automatic retries on failure

---

# Supplementary Docs

- **`output_expectations.md`** --- predicate inventory, constants, formatting rules
- **`additional_info.md`** --- encoding heuristics, negation formatting, edge cases

---

# Evaluation: Syntactic Validity

**Stage 1 (Automated)**
- Each generated encoding fed to clingo parser
- `clingo.Control.add()` + `.ground()` --- passes if no parse error
- Binary outcome: parsable or not parsable
- Enables large-scale automated screening

---

# Evaluation: Semantic Accuracy

**Stage 2 (Manual)**
- ~30 stories per condition scored 0--5 by the author

| Score | Meaning |
|:-----:|---------|
| 5 | Exact match to ground truth |
| 4.5 | Better than ground truth |
| 4 | Pass (functionally correct) |
| 3 | Partial (multiple substantive mistakes) |
| 2--0 | Failing |

**Pass threshold:** score greater than or equal to 4

---

# Syntactic Parsability Results

| Condition | ChatGPT 5.0 | DeepSeek V3.1 | Gemini 2.5 Pro |
|-----------|:-----------:|:-------------:|:--------------:|
| ZeroShot-V1 | 80.0% | 99.0% | 80.0% |
| FewShot-5-Random-V1 | 100.0% | 77.9% | 100.0% |
| FewShot-5-Random-V2 | 100.0% | 84.2% | 100.0% |
| FewShot-10-Random-V1 | 100.0% | 96.7% | 100.0% |
| FewShot-10-Random-V2 | 100.0% | 100.0% | 100.0% |
| Weighted Avg | 95.7% | 91.5% | 95.7% |

All three models achieved 100% in FewShot-10-Random-V2.

---

# Semantic Pass Rates (score >= 4)

| Condition | ChatGPT 5.0 | Gemini 2.5 Pro | DeepSeek V3.1 |
|-----------|:-----------:|:--------------:|:-------------:|
| ZeroShot-V1 | 20.0% | 0.0% | 20.0% |
| FewShot-5-Random-V1 | 63.3% | 53.3% | 50.0% |
| FewShot-5-Random-V2 | 60.0% | 90.0% | 43.3% |
| FewShot-10-Random-V1 | 75.9% | 72.4% | 37.9% |
| FewShot-10-Random-V2 | 82.8% | 79.3% | 48.3% |
| Manual-Prompting (web) | 30.0% | 80.0% | 60.0% |

ChatGPT peaks at 82.8%, Gemini at 90.0%, DeepSeek caps at 60.0%.

---

# Key Findings --- RQ1 and RQ2

**RQ1: Pipeline Feasibility** --- Yes. Under optimal conditions (10-shot + both docs), ChatGPT and Gemini exceed 79% semantic accuracy with 100% syntactic parsability.

**RQ2: Model Comparison** --- Condition-dependent:
- ChatGPT leads in high-exemplar API settings (83% in 10-shot V2)
- Gemini leads with strong documentation + moderate exemplars (90% in 5-shot V2)
- DeepSeek never surpassed 60% in API conditions

---

# Key Findings --- RQ3 and RQ4

**RQ3: Prompting Strategy** --- Combination matters most:
- Gemini: documentation over exemplars
- ChatGPT: exemplars over documentation
- DeepSeek: highly sensitive --- more examples sometimes degrade performance

**RQ4: Failure Modes**
Syntactic (6 modes): Missing periods, unsafe free variables, Chinese character corruption, incorrect predicates, stray punctuation, missing output
Semantic: Action omission, predicate invention, predicate confusion, timestep errors, missing member/2, missing st_next

---

# Notable Anomaly: Chinese Character Corruption

**DeepSeek --- Ji insertion**
- 12 of 95 outputs corrupted with Chinese character Ji
- Appeared in predicate names, string literals, numeric arguments
- Occurred only when additional_info.md was added to 5-shot prompt
- Token-level hallucination from prompt destabilization

---

# Notable Anomalies: Web and Doc Effects

**Web Hallucination (ChatGPT 5.1):** Catastrophically fabricated entirely unrelated stories in final conversational chunk. 30% pass rate vs Gemini 3.0's 80%.

**Gemini's 37-Point Jump:** 53% (5-shot V1) to 90% (5-shot V2) from adding additional_info.md --- single largest improvement across all conditions.

---

# U-Shaped DeepSeek Trajectory

```
ZeroShot       to  99%  (no examples, most reliable)
5-Shot V1      to  78%  (examples destabilize output)
5-Shot V2      to  84%  (docs help partially)
10-Shot V1     to  97%  (more examples stabilize)
10-Shot V2     to 100%  (examples + docs converge)
```

More examples sometimes hurt performance --- counterintuitive.

---

# Best Configuration

## FewShot-10-Random-V2
10 random examples + both supplementary docs

| Metric | ChatGPT | Gemini | DeepSeek |
|--------|:-------:|:------:|:--------:|
| Syntactic | 100% | 100% | 100% |
| Semantic | 82.8% | 79.3% | 48.3% |

Only condition where all 3 models achieved 100% syntactic parsability.

---

# Conclusions

1. LLMs can reliably translate NL into ASP-compatible logic forms under optimal prompting conditions
2. No single best model --- performance is condition-dependent
3. Prompt engineering matters: both exemplar count and documentation design
4. Syntactic 100% is achievable; semantic over 79% for top models
5. Web interfaces are unreliable vs batched API pipelines
6. Failure modes are systematic and potentially correctable

---

# Future Work

- Expand domains beyond restaurant narratives
- Larger-scale evaluation with more annotators
- Automated semantic checking to reduce manual annotation burden
- Failure mitigation --- targeted post-processing for known error patterns
- Chain-of-thought and other advanced prompting strategies
- Fine-tuning specialized models for NL to ASP translation

---

# Thank You

**Questions?**

Amrit Aryal --- Miami University
