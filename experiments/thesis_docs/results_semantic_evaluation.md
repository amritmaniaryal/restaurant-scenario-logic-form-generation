4.4 Semantic Evaluation Results

While the syntactic evaluation in Section 4.2 established whether the generated encodings
were parsable, it revealed nothing about whether they were *correct*---that is, whether
the logical content of the encoding faithfully represented the narrative it was meant to
capture. To assess semantic accuracy, we conducted a manual annotation of sampled
outputs using the rubric defined in Section 4.1.2 (Table 4.1). Each encoding was assigned
a score from 0 to 5, with scores of 4 or higher considered passing.

For each experimental condition, we selected approximately 30 stories spanning the
full range of similarity scores produced by the automated coarse-similarity filter
described in Section 4.1.2. This sampling strategy ensured that the manual evaluation
covered outputs of varying quality rather than focusing only on the best or worst cases.
The resulting scores, pass rates, and qualitative patterns are reported below for each
condition.

4.4.1 ZeroShot-V1

The zero-shot condition represents the most challenging configuration: no exemplar
translations were provided, and the only guidance came from the two supplementary
instructional documents. We manually annotated 10 stories per model (30 annotations
total). Only 4 of the 30 annotations received a passing score of 4. Even these passing
encodings were considered acceptable solely because they would produce valid answer
sets in a downstream solver, not because they reflected the encoding conventions a
domain expert would follow.

Table 4.3 presents the score distribution.

| Score | ChatGPT 5.0 | Gemini 2.5 Pro | DeepSeek V3.1 |
|---|---|---|---|
| 4 (pass) | 2 | 0 | 2 |
| 3 | 6 | 6 | 1 |
| 2 | 2 | 4 | 7 |
| **Pass Rate** | **20.0%** | **0.0%** | **20.0%** |

Table 4.3: ZeroShot-V1 semantic score distribution and pass rates.

ChatGPT 5.0 and DeepSeek V3.1 each achieved a 20% pass rate, while Gemini 2.5 Pro
failed all 10 evaluated outputs. Scores were concentrated in the 2--3 range across
all models, indicating encodings that captured some narrative elements correctly but
contained multiple substantive mistakes.

Despite the varied score distributions, the qualitative nature of the errors was
remarkably consistent. We identified the following systematic patterns:

**Verbose and redundant predicates.** All three models routinely used both `person/1`
and `customer/1` to refer to the same individual, rather than selecting a single
canonical predicate. Similarly, several encodings contained both `pay/2` (an action)
and `paid/1` (a fluent) to describe the same payment event. This redundancy produces
encodings that are significantly more verbose than the ground truth, with unnecessary
predicates that add noise without contributing information.

**Action--fluent confusion.** The most systematic semantic error was the preference for
the fluent `served/1` (via `st_obs`) over the action `put_down/3` (via `st_hpd`)
when encoding a waiter delivering food to a table. While `served/1` is part of the
target domain ontology, it captures only the customer's state, losing information about
the agent, the food item, and the location that `put_down/3` encodes. Almost every
encoding that described food delivery used the fluent form, indicating that the models
default to passive-state predicates rather than the multi-argument action predicates
that the ground truth requires.

**Hallucinated predicate names.** Models occasionally invented predicate names that
have no counterpart in the established ontology. DeepSeek generated predicates such as
`bring`, `choose`, `invite`, `join`, and `pour`, none of which appear in the
instructional documents. Gemini invented `group`, `location`, and `table` as standalone
predicates. ChatGPT, in contrast, did not produce any predicate names outside the target
inventory---its errors were confined to using existing predicates inappropriately.

**Inferred actions.** A recurrent pattern was the encoding of actions that were not
explicitly described in the narrative. Models inferred `sit/1` when the character was
already seated, added `prepare/3` when the story mentioned a chef but not the act of
cooking, and inserted `request/2` interactions absent from the source text. These
inferences, while narratively plausible, violate the explicit-extraction principle:
the models were instructed to encode only what the story states, not what can be
reasonably assumed.

The overall pass rate of 13.3% (4 of 30) establishes a low baseline for semantic
accuracy. The multifaceted error patterns---redundant entity encoding, action--fluent
confusion, hallucinated predicate names, and inferred actions---indicate that the
instructional documents alone were insufficient to teach the models the precise
encoding conventions required for the ASP translation task.

4.4.2 FewShot-5-Random-V1

The introduction of five worked examples alongside the instructional documents produced
a substantial improvement across all three models. Pass rates rose sharply from the
zero-shot baseline, and the range of scores broadened to include the 4.5 category
(better than ground truth) and occasional exact matches.

| Score | ChatGPT 5.0 | Gemini 2.5 Pro | DeepSeek V3.1 |
|---|---|---|---|
| 5 (exact match) | 1 | 1 | 1 |
| 4.5 (better than GT) | 2 | 8 | 5 |
| 4 (pass) | 16 | 7 | 9 |
| 3 | 9 | 13 | 11 |
| 2 | 2 | 1 | 2 |
| 0 | 0 | 0 | 2 |
| **Pass Rate** | **63.3%** | **53.3%** | **50.0%** |

Table 4.4: FewShot-5-Random-V1 semantic score distribution and pass rates.

ChatGPT 5.0 recorded the highest pass rate at 63.3% (19 of 30). Most of its passing
encodings scored a 4, indicating correct but not flawless translations. The most common
point of tension was the encoding of actions whose presence in the story was open to
interpretation. In the ground truth, we sometimes encoded actions that were suggested
but not explicitly stated---for instance, reading "visited" as an `enter` action. When
the model did not encode such actions, the outcome depended on how clearly the action
was conveyed. If the wording was genuinely ambiguous, the omission was considered
acceptable and the encoding could still receive a passing score. If the action was
reasonably clear and the model still omitted it, the encoding received a failing score.
This grey area was the single most common reason for scores of 3 rather than 4. Other
failures included using the `informed` predicate in scenarios that required `cancel_bill`,
encoding the wrong person as the subject of an ordering action, and one incomplete
encoding. On the lenient side, ChatGPT sometimes used the constant `r` for the
restaurant and used `pick_up` in addition to or instead of `read_menu` for menu
reading. Neither was penalised.

Gemini 2.5 Pro achieved a 53.3% pass rate (16 of 30). While its pass rate was lower
than ChatGPT's, the quality of its passing encodings was notably higher: 8 of its 16
passing samples received a 4.5 score, meaning they were judged to be better than the
ground truth. This was the highest rate of 4.5 scores across all three models in this
condition. One distinctive behaviour noticed only with Gemini was its use of the
constant `g` to group people in multi-character stories. The ground truth typically
referred to such groups using a meaningful constant derived from the story narrative---
for instance, `member("David", they)` and `member("his wife", they)` followed by
`st_hpd(order(they, ...), true, ...)`. Gemini's use of `g` instead was unconventional
but functionally equivalent, and encodings that did this were still able to produce
correct answer sets. It was not penalised.
Like ChatGPT, Gemini occasionally used `r` and `restaurant` interchangeably. Among
the failing samples, the most common issue was missing actions---most frequently
`put_down`, followed by `lead_to` and `leave`. In two stories, Gemini assigned
incorrect timesteps, including one where it gave the same timestep to a `put_down`
and a `pay` action. One encoding received a score of 2 due to incorrect arity on
the `order` predicate.

DeepSeek V3.1 achieved a 50.0% pass rate (15 of 30), the lowest of the three. Like
Gemini, it produced several encodings that outperformed the ground truth (5 scored
4.5). Its passing encodings shared the same flexibility as the other models---it used
`r` and `restaurant` interchangeably, and used `w` for the waiter even when the
story named the waiter explicitly. Two observations were unique to DeepSeek. First,
it tended to encode each food item in a shared order separately rather than grouping
them under the constant `f` using `member/2`. This is not the optimal encoding but
does not break the program. Second, it sometimes used the fluent `sitting` via
`st_obs` instead of the action `sit` via `st_hpd`---again, functionally acceptable.
Among the failing samples, a common pattern was DeepSeek using group references like
"we" or "they" in its predicates without first declaring them using `member/2`. In
two exceptional stories involving complaints, it missed the `st_next` predicate
entirely. In one cancellation scenario it used `informed` instead of `cancel_bill`.
Two encodings were missing entirely (scored 0)---one was absent from the response and
one was null. Notably, a single encoding contained a Chinese character embedded in a
string literal: `st_hpd(drink("Sarah", "极coffee"), true, 4)`.

Across all three models, the five-shot configuration marked a clear improvement over
the zero-shot baseline. Pass rates of 50--63% demonstrate that even a small set of
exemplars meaningfully improved semantic accuracy, and the appearance of 4.5 and 5
scores---absent entirely from the zero-shot condition---shows that the models were
capable of producing high-quality translations. The most persistent challenges were
the omission of non-explicit actions and occasional confusion between related
predicates in the ontology.

4.4.3 FewShot-5-Random-V2

This condition replicated the five-shot random configuration but with the addition of
`additional_info.md`, a supplementary document containing explicit heuristics for
encoding edge cases, negation formatting, role compression, and unspecified-entity
handling. The effect of this addition was not uniform across models. Gemini showed a
dramatic improvement; ChatGPT showed no change; DeepSeek showed a slight decline,
though not large enough to be conclusive.

| Score | ChatGPT 5.0 | Gemini 2.5 Pro | DeepSeek V3.1 |
|---|---|---|---|
| 5 (exact match) | 2 | 1 | 0 |
| 4.5 (better than GT) | 3 | 10 | 1 |
| 4 (pass) | 13 | 16 | 12 |
| 3 | 11 | 3 | 16 |
| 2 | 1 | 0 | 1 |
| **Pass Rate** | **60.0%** | **90.0%** | **43.3%** |

Table 4.5: FewShot-5-Random-V2 semantic score distribution and pass rates.

ChatGPT 5.0 achieved a 60.0% pass rate (18 of 30), essentially unchanged from the
63.3% it recorded in the V1 configuration. The addition of the supplementary encoding
guide had no measurable effect on its output. The types of errors were also unchanged
from the previous experiment. The most common issue was again the omission of actions
when the story wording was not explicit---particularly `enter` and `leave`. Other
recurring issues included timestep errors (such as assigning different timesteps to
the `put_down` of two dishes that arrived together), not grouping related people using
`member/2`, and one instance where the encoding included only one member of a group.
One encoding inferred a `sit` action and another missed `st_next` in an exceptional
story. On the acceptable side, ChatGPT sometimes declared food predicates after
actions or fluents rather than before them, used `restaurant` when `r` would have
sufficed, and omitted false actions when they were not explicit. None of these were
penalised.

Gemini 2.5 Pro achieved a 90.0% pass rate (27 of 30), a remarkable increase from
53.3% in V1. The inclusion of the supplementary document produced a ~37 point
improvement, the largest single jump observed across any condition in this study.
Of the 27 passing encodings, 10 received a 4.5 score, meaning they were judged better
than the ground truth. The reasons for the 4.5 scores included: encoding an `enter`
action that the ground truth had missed, making better choices between `sit` (action)
and `sitting` (fluent) depending on the narrative context, more accurate timestep
assignments, and encoding drinks and drink actions that the ground truth had omitted
for convenience. In several cases, Gemini's encodings of complex stories simply
looked cleaner and more coherent than the ground truth, and in some instances Gemini
helped us catch errors in the ground truth itself. Among the score 4 encodings,
common issues were the same as in other experiments---using `r` and `restaurant`
interchangeably. A novel behaviour specific to this experiment was Gemini's use of
the string `c_group` to group customers, rather than a pronoun like "we" or "they"
that would have been more aligned with the examples. This was unconventional but not
penalised. Only 3 encodings failed, each for a distinct reason: one missed `st_next`,
one inferred a `sit` action, and one assigned different timesteps to eating actions
that should have been simultaneous.

DeepSeek V3.1 achieved a 43.3% pass rate (13 of 30), a decrease from 50.0% in V1.
The decline is modest enough that it is not possible to attribute it definitively to
the addition of the supplementary document. The error profile remained similar to
the previous experiment. The most frequent issue in failing encodings was the
inference of actions not present in the story, particularly `put_down` (the most
common), followed by `eat`, `sit`, and `order`. DeepSeek also failed to declare
`waiter/1` when the story explicitly mentioned a waiter but then used `"waiter"` in
subsequent actions without the declaration, used `informed` where `cancel_bill` or
`complain` was required, and missed `st_next`
in exceptional stories. Among the passing encodings, common non-critical issues
included not grouping people or food items where it made sense, and using both
`pick_up` and `read_menu` when one would have sufficed. Chinese characters appeared
in random positions in several encodings. These were obvious enough to be easily
identified and removed, so they did not affect the semantic score, but they would
have caused a syntax failure in an automated pipeline.

The divergent response to `additional_info.md` is the central finding of this
condition. Gemini, which had been middle-ranked in V1, surged to the best performance
observed across all conditions up to this point. ChatGPT's output was essentially
indifferent to the added instruction, and DeepSeek's performance, if anything,
slightly declined. This suggests differences in how each model integrates
instructional text during generation: Gemini appears to prioritise explicit
guidance over example patterns, while ChatGPT relies more heavily on the examples
themselves. DeepSeek's sensitivity to prompt changes is consistent with the pattern
observed in the syntactic evaluation, where longer or more complex prompts could
both help and destabilise its output.

4.4.4 FewShot-10-Random-V1

This condition doubled the exemplar count to ten while keeping the same documentation
configuration as the 5-shot V1 condition. Only 29 of the 30 sampled stories were
evaluated, as one (SID 15) had been included as an example in the input file.

Initial attempts with ChatGPT 5.0 and Gemini 2.5 Pro produced only 7 and 21 of the
90 target outputs respectively, due to output-token limits. Supplementary trials were
conducted with GPT-4o and Gemini Flash 2.5, which completed the full set but achieved
pass rates of only 31% and 43%. After a later provider-side limit increase allowed the
primary models to be re-run successfully (max_tokens raised from 6,000 to 32,000),
their results improved substantially. The primary model results are reported below.

| Score | ChatGPT 5.0 | Gemini 2.5 Pro | DeepSeek V3.1 |
|---|---|---|---|
| 5 (exact match) | 2 | 1 | 1 |
| 4.5 (better than GT) | 7 | 9 | 6 |
| 4 (pass) | 13 | 11 | 4 |
| 3 | 6 | 8 | 15 |
| 2 | 1 | 0 | 3 |
| **Pass Rate** | **~76%** | **~72%** | **~38%** |

Table 4.6: FewShot-10-Random-V1 semantic score distribution and pass rates.

ChatGPT 5.0 achieved its best performance across any condition so far at approximately
76% (22 of 29), a clear improvement from 63% in the 5-shot V1 configuration. Seven
encodings received a 4.5 score, often for including actions or details that the ground
truth had omitted. The error types were consistent with earlier experiments---inferring
actions remained the most common reason for failing scores.

Gemini 2.5 Pro achieved approximately 72% (21 of 29), a meaningful improvement over
its 5-shot V1 score of 53% but notably lower than the 90% it recorded in the 5-shot V2
condition where `additional_info.md` was provided. This reinforces a pattern observed
across multiple conditions: for Gemini, high-quality instructions produce better results
than simply increasing the number of examples. Its error profile was similar to
ChatGPT's in this condition, with inferred actions being the dominant failure mode.

DeepSeek V3.1 achieved approximately 38% (11 of 29), a decline from 50% in the 5-shot
V1 configuration. This continues a pattern observed in both the syntactic and semantic
evaluations: increasing the exemplar count can degrade DeepSeek's output quality,
particularly when the additional examples introduce encoding patterns that differ from
the model's default output template. The error types were unchanged from previous
experiments.

4.4.5 FewShot-10-Random-V2

This condition combined the 10-example setup with `additional_info.md`, representing
the richest prompting configuration tested. It produced the best or near-best semantic
performance for all three models simultaneously, with an unusually high number of
encodings judged to be better than the ground truth.

| Score | ChatGPT 5.0 | Gemini 2.5 Pro | DeepSeek V3.1 |
|---|---|---|---|
| 5 (exact match) | 3 | 2 | 2 |
| 4.5 (better than GT) | 9 | 9 | 5 |
| 4 (pass) | 12 | 12 | 7 |
| 3 | 5 | 6 | 15 |
| **Pass Rate** | **82.8%** | **79.3%** | **48.3%** |

Table 4.7: FewShot-10-Random-V2 semantic score distribution and pass rates.

ChatGPT 5.0 achieved 82.8% (24 of 29), its best performance across all conditions.
Three encodings were exact matches and nine received a 4.5 score, often for encoding
details that the ground truth had omitted---drinks, the `in/2` fluent, read-menu
actions, and better noun-string representations. The remaining 12 passing encodings
scored 4, with only minor and now-familiar issues: using `r` instead of the full
restaurant name, not grouping people or food using `member/2`, and occasionally
using a less specific group reference. Only five encodings failed, each for narrow
reasons---confusing `informed/3` with `complain/3`, missing `st_next`, inferring a
single `put_down` action, declaring two waiters in one story, and omitting one
character's `eat/2` action.

Gemini 2.5 Pro achieved 79.3% (23 of 29), strong performance that trailed only its
own 90% in the 5-shot V2 condition. The distribution was nearly identical to
ChatGPT's: two exact matches, nine 4.5 scores for the same types of improvements
(better noun representation, encoding drinks, adding `in/2`), and 12 scores of 4.
The six failures were similarly narrow in scope---assigning the same timestep to
`enter` and `sit`, giving different timesteps for simultaneous eating, using `f`
inappropriately in an order action, and inferring a `sitting` fluent. The marginal
drop from 5-shot V2 to 10-shot V2 reinforces a pattern observed throughout this
study: Gemini achieves peak performance with high-quality documentation and a
moderate number of examples; doubling the example count adds little beyond what
the instructional document already provides.

DeepSeek V3.1 achieved 48.3% (14 of 29), an improvement from the 10-shot V1
configuration (38%) but still below its 5-shot V1 result of 50%. Two encodings
were exact matches and five received 4.5 scores. The 15 failures reflected
persistent challenges: inferring actions (`put_down`, `eat`, `order`, `drink`)
and inventing predicates outside the target ontology (`join/2` appeared across
multiple stories, along with `standing_by/1` and `claim_reservation/1`), as well
as the familiar `st_next` omission and `informed`-for-`complain` substitution.
The improvement from the V1 10-shot configuration suggests that `additional_info.md`
offers some stabilising effect when paired with a larger exemplar set, but the
gain was not sufficient to surpass its simpler 5-shot V1 result. DeepSeek's
sensitivity to prompt configuration---where more is not always better---remains
a limiting factor.

Taken together, the 10-shot V2 condition produced the best overall outcomes across
the three models considered jointly. ChatGPT and Gemini both exceeded 79% pass
rates with many outputs outperforming the ground truth, and DeepSeek improved
from its 10-shot V1 result, narrowing roughly a third of the gap between its V1
performance and the leading two models. This configuration---ten diverse exemplars combined with explicit encoding
heuristics---represents the most reliable prompting strategy for achieving both
syntactic and semantic quality in the ASP translation task.

4.4.6 Manual-Prompting (Web Interface)

As an exploratory supplement to the API-based experiments, we conducted a trial
using the official web chat interfaces of each model vendor. The model versions
available through these interfaces at the time were GPT-5.1, Gemini 3.0 Pro, and
DeepSeek V3.2---all newer releases than the versions used in the API experiments.
The prompt was pasted directly into the chat and requested all 100 stories in a
single response, with the output format simplified to only `sid` and `logic_form`
fields. There was no automated batching, no JSON repair layer, and no programmatic
retry logic.

ChatGPT 5.1 proactively refused to generate all 100 outputs in one response, stating
that doing so would exceed output limits. After negotiation, the task was divided
into three conversational chunks: SIDs 0--33, 34--66, and 67--99. Gemini 3.0 Pro
and DeepSeek V3.2 produced their full outputs in a single response without objection.

| Score | ChatGPT 5.1 | Gemini 3.0 Pro | DeepSeek V3.2 |
|---|---|---|---|
| 5 (exact match) | 1 | 3 | 1 |
| 4.5 (better than GT) | 1 | 6 | 2 |
| 4 (pass) | 7 | 15 | 15 |
| 3 | 6 | 5 | 11 |
| 2 | 3 | 1 | 1 |
| 1 | 11 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| **Pass Rate** | **30.0%** | **80.0%** | **60.0%** |

Table 4.8: Manual-prompting (web interface) semantic score distribution and pass rates.

ChatGPT 5.1 achieved only 30.0% (9 of 30), but the aggregate obscures a sharp
bifurcation within its output. In the first two conversational chunks (SIDs 0--66),
ChatGPT performed adequately, with 8 encodings receiving passing scores and errors
resembling those observed in earlier experiments. In the third chunk (SIDs 67--99),
however, ChatGPT completely abandoned the input data and generated encodings for
entirely fabricated stories that bore no relation to the target narratives. Eleven of these encodings received a score of 1, indicating entirely fabricated
content unrelated to the input narratives. One was missing entirely. This catastrophic
failure mode---full hallucination of new stories in place of input narratives---was
unique to this experiment and to this model. No other model in any condition
substituted invented stories for the provided text. A plausible contributing factor
is the cumulative conversational context of the chat interface: unlike the stateless
API experiments, where each batch received the full prompt and examples fresh, the
web-based interaction relied on the model maintaining coherence across multiple
conversational turns, which appears to have degraded generation quality in the final
chunk.

Gemini 3.0 Pro achieved 80.0% (24 of 30), the strongest performance in this
condition. Three encodings were exact matches and six received a 4.5 score for
improvements over the ground truth distributed across a variety of stories. Only
five encodings failed, each for narrow reasons---missing `st_next`, a false order
action, and misusing group references. No hallucinations were observed, and the
output was clean and consistent throughout all 100 stories despite being produced
in a single response. This continues the pattern observed across experiments:
Gemini's instruction-following mechanism appears robust to changes in delivery
modality, model version, and prompt format.

DeepSeek V3.2 achieved 60.0% (18 of 30), intermediate between the other two
models. The error profile was familiar from the API experiments: timestep errors,
using group references without declaring them via `member/2`, inferring actions
(particularly `put_down` and `sit`), redundant encoding of both `sit` and
`sitting` for the same action, and missing `st_next` in exceptional stories.
No hallucinations were observed. DeepSeek was the most consistent model across
delivery mechanisms; its error types and overall pass rate in the web-based trial
resembled its API results closely.

This trial revealed that the web chat interface introduces failure modes not
present in the stateless API experiments. ChatGPT's complete hallucination of
stories in later conversational turns suggests that the cumulative context of a
chat session can degrade output coherence for this model, whereas the stateless
API approach---where full context is re-injected into every request---maintained
consistency. For deployment scenarios requiring reliable structured output from
LLMs, stateless prompting with context re-injection appears preferable to
conversational interfaces.

4.4.7 Summary of Semantic Results

The six experimental conditions described above form a matrix across two dimensions:
exemplar count (0, 5, or 10) and the presence or absence of the supplementary
encoding guide (`additional_info.md`). Table 4.9 consolidates the pass rates for all
three models across all configurations.

| Condition | ChatGPT 5.0 | Gemini 2.5 Pro | DeepSeek V3.1 |
|---|---|---|---|
| ZeroShot-V1 | 20.0% | 0.0% | 20.0% |
| FewShot-5-Random-V1 | 63.3% | 53.3% | 50.0% |
| FewShot-5-Random-V2 | 60.0% | **90.0%** | 43.3% |
| FewShot-10-Random-V1 | **75.9%** | 72.4% | 37.9% |
| FewShot-10-Random-V2 | **82.8%** | 79.3% | 48.3% |
| Manual-Prompting (web) | 30.0% | 80.0% | 60.0% |

Table 4.9: Consolidated semantic pass rates across all conditions. Bold values
indicate the best API performance for each model.

A clear trajectory emerges for each model.

ChatGPT 5.0 improved steadily as the prompt configuration became more informative.
Its pass rate rose from 20% in the zero-shot condition to 63% with five examples,
then to 76% and 83% in the 10-shot configurations. The supplementary encoding guide
had minimal effect on its output---the V1-to-V2 changes were small in both the
5-shot (63% to 60%) and 10-shot (76% to 83%) settings, suggesting that ChatGPT
learns predominantly from the examples rather than from explicit instructional text.
Its best API result (83% in 10-shot V2) was the second-highest pass rate across all
API-based conditions, behind Gemini's 90% in the 5-shot V2 configuration. The web-based trial was the notable exception:
ChatGPT's performance collapsed to 30% due to a catastrophic hallucination of
entirely fabricated stories in the final conversational chunk, a failure mode not
observed in any other experiment.

Gemini 2.5 Pro showed the most dramatic improvement from the zero-shot baseline
(0%) to its peak performance (90% in 5-shot V2). Critically, Gemini's best result
was not achieved with the most examples, but with the combination of moderate
exemplars (5) and the supplementary encoding guide. When the guide was absent
(5-shot V1), its pass rate was only 53%; adding the guide (5-shot V2) produced a
37-point jump to 90%. In the 10-shot configurations, the guide still helped, but
the improvement was smaller---from 72% to 79%---suggesting that a larger exemplar
set partially substitutes for explicit instructions. Across both API and web-based
delivery, Gemini was the most consistent model, achieving 80% in the web trial
without any of the hallucination issues that affected ChatGPT.

DeepSeek V3.1 had the most variable trajectory. Its zero-shot pass rate (20%) tied
ChatGPT, but subsequent performance depended unpredictably on the prompt
configuration. It peaked at 50% in the simplest few-shot condition (5-shot V1) and
declined as the prompt grew more complex---43% in 5-shot V2, 38% in 10-shot V1,
then a partial recovery to 48% in 10-shot V2. DeepSeek was the only model for whom
increasing the number of examples or adding instructional text could degrade output
quality. It also struggled with predicate invention: across multiple conditions,
DeepSeek generated predicate names such as `join`, `invite`, `bring`, `pour`,
`choose`, `standing_by`, `claim_reservation`, and `charged` that do not appear in
the target ontology. The web-based trial (60%) was DeepSeek's best relative showing,
narrowing the gap behind Gemini.

Across all experiments, the most persistent error patterns were the omission of
actions that were not narratively explicit (particularly `enter`), the invention
of predicates outside the established domain ontology, confusion between related
predicates (such as `informed` versus `complain` or `cancel_bill`), incorrect
timestep assignment, the failure to declare group memberships via `member/2` before
using group references, and missing `st_next` in exceptional complaint scenarios.

Regarding the research questions posed in Section 3.1, the semantic evaluation
yields the following findings. First, a reliable pipeline for narrative-to-ASP
translation is achievable (RQ1): under the right prompting conditions---ten diverse
exemplars combined with explicit encoding heuristics---ChatGPT and Gemini both
exceeded 79% semantic accuracy, and the syntactic evaluation established that
100% of these outputs were parsable. Second, model rankings were condition-dependent
(RQ2): ChatGPT led in high-exemplar API settings, Gemini led when strong
documentation was paired with moderate exemplars, and DeepSeek never surpassed 60%
in API conditions. Third, prompting strategy had a decisive effect (RQ3): the
combination of exemplar count and instructional documentation mattered far more
than either factor alone. Finally, the most common structural and logical
deficiencies (RQ4) stemmed from action omission, predicate invention, and
predicate confusion---errors that grow less frequent but do not fully disappear
as prompt configurations improve.

