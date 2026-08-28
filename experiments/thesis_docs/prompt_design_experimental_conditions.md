### 3.3.2 Common Prompt Architecture

Before describing the individual experimental conditions, we first establish the prompt
architecture that was shared across all conditions in this study. This common framework
ensured that any differences in model output could be attributed to the specific variables
under investigation rather than to incidental differences in prompt construction.

#### System Persona

Every API request across all conditions began with a static system persona assignment:
*"You are a precise ASP logic translator. You never skip data."* This instruction served
two purposes. First, it established the model's role as a translator of natural language
into a formal logical notation, signalling that the task required structured, rule-governed
output rather than creative or conversational text. Second, the directive *"You never skip
data"* was included as a countermeasure against the tendency of some models to omit
or summarise inputs, a behavioural failure mode we discuss further in Section 3.3.3.

#### Supplementary Instructional Document

The majority of experimental conditions included a supplementary instructional document
located at `FewShot/docs/output_expectations.md`. This document defined the complete
predicate inventory available for translation, including entity predicates (`customer/1`,
`waiter/1`, `food/1`, `beverage/1`, etc.), the full set of fluents for state observations
(via `st_obs/3`), and the complete inventory of actions for event occurrences (via
`st_hpd/3`). It also specified critical formatting rules---most notably the requirement
that all entity names be enclosed in double quotes, e.g., `"John"` or `"miso soup"`---and
defined reserved constants (`t`, `b`, `r`, `w`, `f`, `tip`) and special predicates such as
`st_next/2` for consecutive time steps in complaint scenarios. The full specification is
reproduced in Appendix A. The presence or absence of this document was one of the
independent variables manipulated across conditions.

#### Structural Constraints and Formatting Rules

In addition to the system persona and instructional document, every prompt included a
repeated set of structural constraints, defined in the code as `JSON_FORMATTING_RULES`
and placed immediately before the task instructions:

```
CRITICAL RULES:
1. Return ONLY a valid JSON object.
2. The 'logic_form' field MUST be a list of strings.
3. ESCAPE quotes: \"person(\\\"John\\\")\".
4. MANDATORY COMPLETENESS: You MUST process EVERY story provided
   in the 'TARGET TASK' section.
5. If I give you 10 stories, you must return exactly 10 logic forms.
```

These rules addressed the most common syntax failures observed during pilot testing.
Rule 3 (quote escaping) was particularly important: JSON requires internal double quotes
to be escaped with backslashes, but ASP predicates frequently contain quoted entity names
(e.g., `person("John")`), creating a nested-quoting problem that models consistently
struggled with. Rules 4 and 5 served as countermeasures against the tendency of some
models to silently omit or summarise input stories, a failure mode we discuss further in
Section 3.3.3.

#### Input Data Injection

Rather than paraphrasing or reformatting the story data, the complete input JSON
structure was injected verbatim into the prompt. This design choice preserved the exact
field names, nesting, and original text of every story, ensuring that the model received
the same data representation that the evaluation pipeline would later use. The input was
placed in a clearly delimited section of the prompt with a direct instruction to generate or
replace the `logic_form` field for each entry.

#### Inference Configuration

All model queries across all conditions shared the following inference parameters:

- **Temperature:** 0.0, ensuring deterministic output and facilitating reproducibility.
- **Response format:** Enforced as a JSON object via the API parameter
  `{"type": "json_object"}`, which instructs the model to constrain its generation to
  valid JSON syntax.
- **Token limit:** Set to 32,000 tokens per request, sufficient to accommodate both the
  prompt and the expected output for a single batch.

#### Batch Processing Strategy

A practical constraint emerged from the models' output token limits: generating logic
forms for all 90 or 95 target stories in a single API call would exceed the maximum
output token allowance of every model tested. To address this, we adopted a batched
inference strategy.

For each experiment, the input stories were first separated into two groups at the data
level: **examples**, which already possessed populated `logic_form` fields and served
as reference material, and **targets**, which were marked `["N/A"]` and required encoding.
Only the targets were divided into batches. Each batch's API request then contained:

1. The system persona and task instructions.
2. The full set of reference examples (identical across all batches for a given
   experiment).
3. The supplementary instructional document, if applicable.
4. A subset of target stories---typically 10 per batch---for which the model was
   instructed to produce logic forms.

The prompt structure for each batch was as follows:

```
### REFERENCE EXAMPLES:
[example stories with populated logic forms]

### DOCUMENTATION:
[instructional document, if applicable]

### TARGET TASK:
STORIES TO PROCESS:
[batch-specific target stories with "N/A"]
```

After all batches for a given model completed, their outputs were reassembled in the
original story order to produce the complete result set. Because each batch's request
included the full set of reference examples, the model had the same few-shot context
available in every batch, ensuring consistency across the full dataset.

#### Retry and Error Handling

Each batch request was configured with up to two automatic retries upon failure. If all
retries were exhausted, the raw model response (or the error message) was persisted to
disk for diagnostic purposes. Additionally, a JSON repair layer using the `json-repair`
library was applied to handle common formatting issues such as unescaped quotes within
predicate strings, which occurred frequently given the nested quotation structure of the
ASP predicates within JSON fields.

---

### 3.3.3 Condition: ZeroShot-V1

#### Motivation

The ZeroShot-V1 condition establishes the baseline for the study. In this configuration,
the models were given no worked examples of story-to-ASP translations. Their only
guidance was the two supplementary instructional documents. This condition answers
the question: can LLMs produce valid ASP logic forms from narrative text using only a
predicate specification, without any exemplar translations to learn from?

#### Input Data

The input file `FewShot/inputs/0_input.json` contained 100 stories, all of which were
marked `["N/A"]` for their `logic_form` fields. Because there were no pre-populated
examples, the batching strategy divided the full set of 100 target stories into batches of
10, with each batch receiving the two instructional documents as context but no reference
translations.

#### Variable Parameters

| Parameter | Value |
|---|---|
| Few-shot examples | 0 |
| Example selection strategy | N/A |
| Instructional document (`output_expectations.md`) | Present |
| Additional encoding guide (`additional_info.md`) | Present |
| Target stories | 100 |
| Batch size | 10 |

---

### 3.3.4 Condition: FewShot-5-Random-V1

With the common architecture established, we now describe the first few-shot
configuration employed in our study. The **FewShot-5-Random-V1** condition represents
the initial few-shot configuration employed in our study.

#### Objective

The objective of this condition was to determine whether providing five randomly
selected exemplar translations, in conjunction with the supplementary instructional
document, would enable LLMs to generalise to the remaining unseen stories. This
represents the minimal prompt augmentation beyond a baseline zero-shot configuration.

#### Input Data

The input file `FewShot/inputs/5_random_input.json` contained 100 stories, of which
five possessed fully populated `logic_form` fields and 95 were marked `["N/A"]`. The
five examples were selected at random from the pool of manually verified translations and
covered a range of narrative structures:

- **sid 1 (Abdul, Normal):** A straightforward sequence of sitting, ordering, and
  receiving food.
- **sid 59 (Lucy, Normal):** A health-food visit involving two distinct order items,
  illustrating separate encoding of food and beverage predicates.
- **sid 78 (Betsy, Normal):** A diner scenario with a group food order using
  `member/2` and a tip payment.
- **sid 93 (Me and my mother, Exception):** An unavailability narrative requiring a
  negated fluent and a location transfer between restaurants.
- **sid 98 (Joe, Normal):** A hunger-to-satiety state change across time steps.

Four of these were `Normal`-type stories and one was an `Exception`-type story.

#### Variable Parameters

This condition was configured with the following experiment-specific parameters, which
distinguish it from other conditions:

| Parameter | Value |
|---|---|
| Few-shot examples | 5 |
| Example selection strategy | Random |
| Instructional document (`output_expectations.md`) | Present |
| Additional encoding guide (`additional_info.md`) | Absent |
| Target stories | 95 |
| Batch size | 10 |

The master configuration entry for this condition (`experiment_id: "FewShot_5_Random_V1"`
in `Scripts/master_config.yaml`) also specified the input data path and the set of models
to evaluate, which matched the three primary models described in Section 3.3.1.

---

### 3.3.5 Condition: FewShot-5-Random-V2

#### Motivation

FewShot-5-Random-V2 was designed to isolate the effect of providing additional
encoding guidance beyond the basic predicate inventory. Whereas V1 supplied only the
output expectations document, V2 introduced a second supplementary document containing
explicit heuristics for handling edge cases and encoding ambiguities.

#### Changes from V1

The sole difference from the V1 condition was the inclusion of a second instructional
document, `FewShot/docs/additional_info.md`. This document, reproduced in Appendix A,
addressed several specific encoding challenges that were not covered in the output
expectations file:

- **Action inference rule:** If a story does not explicitly mention an action (e.g.,
  entering, ordering, eating), the model must not infer it.
- **Negation format:** Negated actions must be encoded as `st_hpd(Action, false)`
  without a time step, distinguishing them from observed false fluents.
- **Role compression:** Characters who perform waiter duties but are not explicitly
  called "waiters" should be encoded as `waiter(X)`, unless a separate waiter is also
  mentioned, in which case they become `person(X)`.
- **Unspecified food items:** Generic terms like "food" or "meal" should be encoded
  as `food("food")`; if even a generic term is absent, the constant `f` should be used.
- **Inconsistency resolution:** Where the provided examples are inconsistent, the model
  should follow the encoding method that appears most frequently.
- **Prohibition of `story_step()`:** The `story_step/1` predicate is unnecessary and
  should not be used.

#### Variable Parameters

| Parameter | Value |
|---|---|
| Few-shot examples | 5 |
| Example selection strategy | Random |
| Instructional document (`output_expectations.md`) | Present |
| Additional encoding guide (`additional_info.md`) | Present |
| Target stories | 95 |
| Batch size | 10 |

All other parameters---system persona, inference configuration, batch processing
strategy, and retry logic---were identical to those described in Section 3.3.2. The
input file and the set of five example stories were the same as in V1, ensuring that any
differences in output quality could be attributed solely to the presence of the additional
encoding guide.

---

### 3.3.6 Condition: FewShot-10-Random-V1

#### Motivation

This condition doubled the number of few-shot examples from five to ten while keeping
the same documentation configuration as the five-shot V1 condition (output expectations
document only). The objective was to assess whether additional exemplars alone---without
supplementary encoding heuristics---would improve the models' ability to generalise to
unseen stories.

#### Changes from the Five-Shot Condition

The input file was changed to `FewShot/inputs/10_random_input.json`, which contained
ten stories with populated logic forms and 90 marked `["N/A"]`. The ten examples
provided broader coverage of both `Normal` and `Exception` scenario types and
introduced additional encoding patterns not present in the five-shot set:

- **sid 5 (Normal):** A waiter-led seating sequence without a separate entry event,
  relying on `lead_to/3` from the initial state.
- **sid 6 (Exception):** An order substitution narrative (ordered baked potato,
  received French fries), demonstrating the encoding of expectation violations.
- **sid 7 (Exception):** A "decides not to order" story using `st_hpd(order(P), false)`
  for a negated action.
- **sid 15 (Normal):** A villager dining alone with explicit menu-reading (`pick_up/3`,
  `read_menu/1`) encoded via `menu_read/1`.
- **sid 35 (Exception):** An unavailability narrative involving a full restaurant,
  requiring `st_obs/3` with a negated fluent for table availability.
- **sid 43 (Normal):** A bar-seating scenario with a solo diner ordering a beverage,
  demonstrating the use of `drink/2` without a corresponding `eat/2`.
- **sid 50 (Exception):** A "ran out of soup" narrative requiring the `available/2`
  fluent with a subsequent re-order.
- **sid 59 (Normal):** A health-food visit with two distinct order items (food and
  beverage predicates encoded separately).
- **sid 74 (Normal):** A couple dining together, using the `member/2` predicate for
  group membership alongside individual eating and drinking actions.
- **sid 92 (Exception):** A first-person narrative ("I") where the salad served
  was smaller than ordered, requiring an implicit expectation violation.

Three of these stories were also present as examples in the five-shot condition (sids 6,
50, and 59), while the remaining seven were new. The examples thus represented a more
diverse set of narrative structures, including first-person perspective, group dining, and
a broader range of exceptional scenarios.

#### Variable Parameters

| Parameter | Value |
|---|---|
| Few-shot examples | 10 |
| Example selection strategy | Random |
| Instructional document (`output_expectations.md`) | Present |
| Additional encoding guide (`additional_info.md`) | Absent |
| Target stories | 90 |
| Batch size | 10 |

All other parameters remained as specified in Section 3.3.2.

---

### 3.3.7 Condition: FewShot-10-Random-V2

#### Motivation

This condition replicated the documentation configuration of the five-shot V2
condition (both `output_expectations.md` and `additional_info.md` present) while
maintaining the ten-example setup of the preceding condition. It serves as the 10-shot
analogue of the V1-to-V2 transition.

#### Changes from the 10-Shot V1 Condition

Relative to FewShot-10-Random-V1, the sole difference was the inclusion of the
`additional_info.md` document. The same encoding heuristics described in Section 3.3.5
(action inference prohibition, negation formatting, role compression, unspecified food
handling, inconsistency resolution, and prohibition of `story_step()`) were appended to
the prompt for every batch.

All other parameters---input file, example set, number of targets, batch size, and
inference configuration---remained identical to FewShot-10-Random-V1.

#### Variable Parameters

| Parameter | Value |
|---|---|
| Few-shot examples | 10 |
| Example selection strategy | Random |
| Instructional document (`output_expectations.md`) | Present |
| Additional encoding guide (`additional_info.md`) | Present |
| Target stories | 90 |
| Batch size | 10 |

---

### 3.3.8 Condition: Manual-Prompting (Web Interface, Latest Model Versions)

As noted in Section 3.3.1, an exploratory supplementary trial was conducted using the
official web interfaces of each vendor rather than the OpenRouter API. This condition
was motivated by the difficulties encountered during the API-based 10-shot experiments,
where GPT-5 and Gemini 2.5 Pro frequently failed to produce complete output sets due
to token limits and batch laziness. We wanted to determine whether the same limitations
would persist when interacting with the models through their native web interfaces, where
conversational context management and output handling differ from the programmatic API.

By the time these trials were conducted, the model versions available through the web
interfaces had advanced beyond those accessible via the OpenRouter API during our
primary experiments. The versions available were GPT-5.1, Gemini 3.0 Pro, and DeepSeek
V3.2. While this introduced a confound---newer models may perform differently for
reasons unrelated to the delivery mechanism---it also provided an opportunity to assess
whether the latest releases had improved on the limitations observed in their predecessors.

#### Prompt Design

Unlike the API-based experiments, which used a structured batched prompt with separate
sections for reference examples, documentation, and batch-specific targets, the web-based
trial used a single continuous prompt that was pasted directly into the chat interface:

```
You are a precise ASP logic translator. You never skip data.
Translate all the narrative text provided in the json file
(10_random_input.json) to their ASP logic form. Out of 100 stories
in the input data, 10 of those stories will have their valid logic
form for you to get a reference from. Apart from those examples,
there will be two markdown files shared in this prompt, with one
file (output_expectations.md) covering the type of predicates that
we are looking for, and other important information, and the other
file (additional_info.md) covering other important information
regarding the translation from natural language stories to valid
ASP logic form. The latter file also contains some information
about possible edge cases.

For output, output should follow the same json format as input,
but the fields like 'text', and 'scenario_type' can be discarded.
```

The input JSON file, the output expectations document, and the additional encoding
guide were attached or pasted alongside this instruction. The prompt differed from the
API-based equivalents in two notable ways. First, the output format requirement was
relaxed: rather than reproducing the full input JSON structure (including `text`,
`scenario_type`, and `storyid` fields), the model was instructed to return only the `sid`
and `logic_form` fields for each story. Second, there was no programmatic batching---the
intent was for the model to translate all 100 stories in a single interaction.

In practice, however, the models handled this request differently. ChatGPT (GPT-5.1)
proactively refused to generate all 100 outputs at once, responding that producing the
entire translated JSON in one response "would exceed the model's output limits and
risks truncation or corruption of the result." After several exchanges negotiating the
approach, it was agreed to split the task into three chunks---sid 0--33, sid 34--66, and
sid 67--99---with each chunk requested sequentially through the conversation. This
behaviour was unique to ChatGPT; both Gemini 3.0 Pro and DeepSeek V3.2 generated
their full outputs in a single response without suggesting or requiring chunking.

#### Relationship to API-Based Conditions

This condition is most directly comparable to FewShot-10-Random-V2 (Section 3.3.7),
as both used ten random examples and both supplementary documents. The key variables
that differed were:

- **Model versions:** GPT-5.1, Gemini 3.0 Pro, and DeepSeek V3.2 (newer than the
  API-based primary models).
- **Delivery mechanism:** Web chat interface rather than OpenRouter API, with no
  automated batching or retry logic.
- **Output format:** The model was permitted to omit `text` and `scenario_type`
  fields from the output, simplifying the required JSON structure.
- **No automatic JSON repair:** Because the interaction was manual, any output
  malformations were handled on a case-by-case basis rather than through the automated
  `json-repair` pipeline.

#### Variable Parameters

| Parameter | Value |
|---|---|
| Few-shot examples | 10 |
| Example selection strategy | Random |
| Instructional document (`output_expectations.md`) | Present |
| Additional encoding guide (`additional_info.md`) | Present |
| Target stories | 100 (single pass, no batching) |
| Delivery method | Web chat interface |
| Models | GPT-5.1, Gemini 3.0 Pro, DeepSeek V3.2 |
