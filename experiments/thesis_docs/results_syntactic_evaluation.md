Chapter 4
Results and Evaluation
Having established the experimental framework, including the dataset, prompting condi-
tions, and model configurations in the preceding chapter, this chapter presents a systematic
evaluation of the Large Language Models' ability to generate syntactically valid and semanti-
cally accurate Answer Set Programming (ASP) encodings from unstructured narrative text.
Where Chapter 3 detailed how the data were generated, this chapter addresses the central
empirical question: how well did the models perform?

The evaluation is structured to directly address the research questions posed in Sec-
tion 3.1. Specifically, we assess RQ3---the effectiveness of different prompting strategies
(varying shot counts and the presence of supplementary instructional documents)---RQ2---
the comparative performance of GPT-5, Gemini 2.5 Pro, and DeepSeek V3.1 under equiva-
lent conditions---and RQ4---the common structural and logical deficiencies observed in the
generated outputs. The overarching goal is to determine whether a reliable pipeline (RQ1)
can be constructed to transform natural language into logic-compatible representations.

4.1 Evaluation Metrics and Annotation Protocol

To enable a reproducible and fine-grained assessment, we employed a two-stage evaluation
protocol. The first stage measured syntactic validity by determining whether a generated
ASP encoding could be successfully parsed by the clingo grounder. The second stage assessed
semantic accuracy for outputs that passed the syntactic filter, comparing their logical content
against the ground-truth encodings through manual annotation.

4.1.1 Syntactic Validity: Automated Clingo Parsing

Syntactic evaluation focused exclusively on whether generated ASP encodings would be
parsable by clingo, the standard grounder and solver for Answer Set Programming. A
generated logic form was considered syntactically valid if and only if it could be successfully
parsed by the clingo grounder without raising a lexer or syntax error.

To operationalize this criterion at scale, we developed an automated validation pipeline
using the official clingo Python library (version 5.8). The process proceeded as follows:

1. Extraction: For each experimental condition and each model, the generated JSON
outputs were parsed to extract the predicted ASP predicate strings from the logic form
field.

2. Conversion: Each extracted predicate string was converted from its JSON represen-
tation to a flat string format suitable for clingo ingestion.

3. Parsing: The predicate string was fed directly to the clingo parser via the Control.add()
and Control.ground() methods. These methods invoke the grounder's lexer and
parser without performing any solving.

4. Classification: If the parser raised an exception (indicating a lexer error, syntax
error, or malformed predicate), the encoding was marked as syntactically invalid. If no
exception was raised, the encoding was marked as syntactically valid.

This automated validation was applied exhaustively to all generated encodings across
every experimental condition, model, and story. The exhaustive nature of this evaluation---
covering all 100 stories across all conditions---provides a comprehensive and reproducible
baseline for comparing model performance on syntactic correctness.

4.2 Syntactic Evaluation Results

Applying the automated clingo parsing pipeline described in Section 4.1.1, we evaluated
the syntactic parsability of all generated ASP encodings across the five API-based experi-
mental conditions. This section presents the aggregate results for each condition, followed
by a detailed analysis of the specific failure modes observed.

4.2.1 ZeroShot-V1

The zero-shot condition, in which models received no exemplar translations and only the
supplementary instructional documents, establishes the baseline syntactic competence of
each model.

| Model | Total | Parsable | Not Parsable | Parsability Rate |
|---|---|---|---|---|
| ChatGPT 5.0 | 100 | 80 | 20 | 80.0% |
| DeepSeek V3.1 | 100 | 99 | 1 | 99.0% |
| Gemini 2.5 Pro | 100 | 80 | 20 | 80.0% |

DeepSeek V3.1 achieved near-perfect syntactic parsability with only a single failure,
while both ChatGPT 5.0 and Gemini 2.5 Pro produced invalid output for 20 of their
100 encodings.

Failure Analysis. All 20 invalid outputs from ChatGPT and all 20 from Gemini share a
single, uniform cause: the absence of terminating periods. In the ASP language, every
predicate or rule must end with a period (`.`). However, both models consistently
generated predicates separated only by whitespace, producing strings such as:

```
person("Jasper") person("Frank") customer("Jasper") customer("Frank")
restaurant(r) waiter(w) food("roast beef") st_hpd(pay("Frank", b), true, 2)
```

This format resembles a space-delimited token sequence rather than a valid clingo
program. Crucially, the error pattern is uniform across all 40 invalid outputs: every
predicate in every failing encoding is individually well-formed---correct arity, properly
quoted strings, balanced parentheses---yet the absence of a single `.` character after
each predicate renders the entire program unparsable. This indicates that both ChatGPT
and Gemini, when operating without exemplars, default to a serialisation convention
that is incompatible with clingo's grammar.

DeepSeek's single failure (SID 71) was qualitatively different: a stray closing parenthesis
inserted mid-argument:

```
st_hpd(put_down("waitress", "glass of water"), t), true, 5)
```

The extra `)` after `"glass of water"` creates a malformed term structure that the parser
cannot resolve. This is an isolated punctuation error rather than a systematic formatting
issue.

4.2.2 FewShot-5-Random-V1

The introduction of five worked examples produced a sharp divergence in syntactic
outcomes across the three models.

| Model | Total | Parsable | Not Parsable | Parsability Rate |
|---|---|---|---|---|
| ChatGPT 5.0 | 95 | 95 | 0 | 100.0% |
| DeepSeek V3.1 | 95 | 74 | 21 | 77.9% |

ChatGPT and Gemini both achieved perfect syntactic parsability, demonstrating that a
small set of exemplars was sufficient to teach them the period-delimited formatting
convention. DeepSeek, however, exhibited the opposite trend: its parsability rate dropped
from 99% in the zero-shot condition to 77.9%. Two of the 21 failures were missing or null
predicted outputs for target stories; the remaining 19 were parsing errors from complete
encodings.

Failure Analysis. The 21 DeepSeek failures in this condition fall into two categories,
both distinct from the zero-shot error pattern.

Unsafe free variables (19 of 21 failures). The dominant failure mode---accounting for
the majority of invalid outputs---is the use of free variables as placeholders for unspecified
entities. When a story describes a character ordering "food" or "a meal" without naming
the specific dish, DeepSeek's encoding substitutes a variable rather than using the
constant `f` (the convention established in the ground-truth encodings and the
instructional documents). For example:

```
st_hpd(order(they, X, w), true, 1). st_hpd(eat(they, X), true, 2).
```

In clingo's safety requirement, every variable appearing in a rule or fact must appear
in at least one positive predicate in the rule's body, ensuring that the variable can be
grounded to a finite domain. Facts containing variables---such as the examples above---
have no body predicates to ground `X`, making the variable unsafe. The parser
rejects such constructs with an "unsafe variables" error.

This error appears across a diverse range of narrative structures. DeepSeek uses `X` for
unspecified food items (`order(they, X, w)`, `eat("Tim", X)`), `Y` for unspecified
table locations (`put_down("the waiter", Y, t)`), and occasionally both in a single
encoding:

```
restaurant("a restaurant"). customer("Tim"). waiter("the waiter").
story_step(0..3). st_hpd(eat("Tim", X), true, 0).
st_hpd(put_down("the waiter", "their food", t), true, 1).
st_hpd(informed("Tim", "something was wrong", "the waiter"), true, 2).
st_hpd(put_down("the waiter", Y, t), true, 3).
```

The pattern suggests that DeepSeek treats the predicate vocabulary as a template into
which slot values must be inserted. When a slot (e.g., the specific food ordered) is not
explicitly filled by the story text, the model produces a variable rather than falling back
to a default constant. This is in contrast to ChatGPT and Gemini, which in the same
situation use either a generic constant or omit the predicate altogether.

Missing output (2 of 21 failures). Two target stories (SIDs 36 and 44) had no valid
predicted output---one was missing entirely from the model's response and the other
contained a null value. These completeness failures are distinct from the syntactic
errors described above.

4.2.3 FewShot-5-Random-V2

The addition of the `additional_info.md` encoding guide---which included explicit
heuristics for handling unspecified entities, negated actions, and role compression---
yielded a partial improvement in DeepSeek's syntactic performance while introducing
a new and unexpected failure mode.

| Model | Total | Parsable | Not Parsable | Parsability Rate |
|---|---|---|---|---|
| ChatGPT 5.0 | 95 | 95 | 0 | 100.0% |
| DeepSeek V3.1 | 95 | 80 | 15 | 84.2% |
| Gemini 2.5 Pro | 95 | 95 | 0 | 100.0% |

ChatGPT and Gemini maintained their perfect scores. DeepSeek improved from 77.9%
to 84.2%, suggesting that the supplementary heuristics partly addressed the unsafe-
variable problem. However, the nature of DeepSeek's remaining failures changed
dramatically.

Failure Analysis. While the number of unsafe-variable errors dropped from 21 to 2,
a new failure mode emerged that accounts for 12 of the 15 invalid outputs: character
corruption in the form of random Chinese character insertions.

The corrupting character is consistently the Chinese character 极 (pronounced *jí*,
meaning "extreme" or "extremely"). Its appearance follows no discernible semantic
pattern. It is inserted:

- **Within predicate names:** `st极_hpd(drink(...))` --- the character splits the
  predicate token, producing an unrecognised identifier.
- **Within string literals:** `waiter("极the waiter")` --- embedded inside a quoted
  entity name.
- **Adjacent to numbers:** `true, 极4)` or `true, 7极)` --- corrupting time-step
  arguments.
- **Adjacent to variables:** `f极` or `put_down(w极, ...)` --- attached to constant or
  variable tokens.
- **Within other tokens:** `st极pd(...)` --- a hybrid of a truncated predicate name
  and the corrupting character.

The following example, taken from SID 67, illustrates the severity of the corruption:

```
restaurant("a quiet Italian restaurant"). customer("Maria"). customer("Leo").
beverage("a bottle of red wine"). food("two pasta dishes").
waiter("极the waiter"). st_hpd(lead_to("the waiter", "Maria", t), true, 1).
st_hpd(order("Maria", "a bottle of red wine", "the waiter"), true, 2).
st_hpd(drink("Maria", "a bottle of red wine"), true, 7). st极_hpd(drink("Leo",
"a bottle of red wine"), true, 7极). st_hpd(pay("Maria", b), true, 8).
```

Note the three distinct corruptions in this single encoding: a prefixed `极` inside a
string literal (`"极the waiter"`), an infixed `极` splitting a predicate name
(`st极_hpd`), and a suffixed `极` adjacent to a numeric argument (`7极`). Each of
these is independently sufficient to cause a parse failure.

The mechanism underlying this corruption appears to be a token-level hallucination.
During generation, the model's output distribution assigns non-zero probability to a
token that is semantically unrelated to the ASP domain. The token `极` corresponds to
a single Unicode character that, in DeepSeek's tokeniser, may be represented as a
standalone byte or token. Its repeated appearance across multiple independent outputs
(13 of 15 failures in this condition) suggests that the corruption is not a random
sampling artifact but rather a systematic failure mode triggered by the interaction
between the supplementary encoding guide and DeepSeek's generation dynamics.

Notably, this corruption was absent from the zero-shot condition (0 occurrences) and
the V1 five-shot condition (0 occurrences). It appeared only after the addition of
`additional_info.md`, suggesting that the longer or more complex prompt may have
destabilised DeepSeek's output distribution in a way that occasionally produces
out-of-vocabulary or cross-lingual token insertions.

4.2.4 FewShot-10-Random-V1

The 10-shot V1 condition doubled the number of exemplars to ten while keeping the
same documentation configuration as 5-shot V1 (output expectations document only).

| Model | Total | Parsable | Not Parsable | Parsability Rate |
|---|---|---|---|---|
| ChatGPT 5.0 | 90 | 90 | 0 | 100.0% |
| DeepSeek V3.1 | 90 | 87 | 3 | 96.7% |
| Gemini 2.5 Pro | 90 | 90 | 0 | 100.0% |

ChatGPT 5.0 and Gemini 2.5 Pro achieved perfect syntactic parsability, demonstrating
that ten diverse exemplars without supplementary heuristics were already sufficient to
teach them the full clingo grammar. DeepSeek V3.1 achieved 96.7% parsability, with
3 of 90 encodings failing.

Failure Analysis. The three DeepSeek failures fall into two categories, both consistent
with patterns observed in earlier conditions.

Incorrect predicate names (2 failures). Two DeepSeek outputs use `st_informed(...)`
instead of the correct `informed(...)`. The `st_` prefix is conventionally used for
fluent and action predicates (`st_obs/3`, `st_hpd/3`), but `informed` is a static
predicate that should not carry this prefix. The resulting encodings are:

```
st_informed("Nicole", "no bill needed", "the waitress"), true, 4).
st_informed("the waitress", "on the house", "Nicole"), true, 2).
```

The malformed structure---a parenthesised predicate list followed by `, true, 4)`---
indicates that DeepSeek attempted to wrap `st_informed(...)` within the `st_hpd/3`
or `st_obs/3` template, producing a hybrid that satisfies neither signature. This
suggests a generalisation error in DeepSeek's predicate-selection mechanism: it
recognised that an event or state was being described but applied the wrong
predicate template.

Unsafe variables (1 failure). One DeepSeek output contains the unsafe variable
pattern observed in the five-shot condition:

```
member(X, "the book club members").
```

Here `X` appears only in this single fact with no body predicate to ground it,
violating clingo's safety requirement. This is the same failure mode documented
in Section 4.2.2.

4.2.5 FewShot-10-Random-V2

The addition of `additional_info.md` to the 10-shot configuration---combining ten
diverse exemplars with explicit encoding heuristics---achieved the best outcome across
all conditions.

| Model | Total | Parsable | Not Parsable | Parsability Rate |
|---|---|---|---|---|
| ChatGPT 5.0 | 90 | 90 | 0 | 100.0% |
| DeepSeek V3.1 | 90 | 90 | 0 | 100.0% |
| Gemini 2.5 Pro | 90 | 90 | 0 | 100.0% |

All three primary models produced outputs for all 90 target stories, and every encoding
parsed successfully. This represents a 100% syntactic parsability rate across 270
generated encodings. Notably, the problems that plagued DeepSeek in earlier
conditions---unsafe-variable errors in V1 five-shot and both unsafe-variable and
character-corruption errors in V2 five-shot---were entirely eliminated. The inclusion
of `additional_info.md` in the 10-shot configuration, combined with the larger
exemplar set, was sufficient to close the remaining syntactic gap for DeepSeek while
maintaining the perfect performance already achieved by ChatGPT and Gemini.

4.3 Discussion of Syntactic Results

The per-condition analyses presented in Sections 4.2.1 through 4.2.5 revealed distinct
patterns of syntactic competence and failure across models and prompting configurations.
In this section, we step back from the condition-by-condition narrative to address four
cross-cutting questions that synthesise the empirical findings: (1) which model achieved
the highest overall syntactic validity, (2) how the number of few-shot exemplars affected
syntactic correctness, (3) whether the supplementary encoding guide improved or harmed
syntactic validity, and (4) what were the most common parser errors observed across all
conditions.

4.3.1 Comparative Model Performance

To answer RQ2---how the three primary models compare on the syntactic validity
dimension---we aggregate the parsability rates across all five API-based conditions.
Table 4.1 presents the per-condition parsability rates for each model.

| Condition | ChatGPT 5.0 | DeepSeek V3.1 | Gemini 2.5 Pro |
|---|---|---|---|
| ZeroShot-V1 (100 targets) | 80.0% | 99.0% | 80.0% |
| FewShot-5-Random-V1 (95 targets) | 100.0% | 77.9% | 100.0% |
| FewShot-5-Random-V2 (95 targets) | 100.0% | 84.2% | 100.0% |
| FewShot-10-Random-V1 (90 targets) | 100.0% | 96.7% | 100.0% |
| FewShot-10-Random-V2 (90 targets) | 100.0% | 100.0% | 100.0% |
| **Weighted Average** | **95.7%** | **91.5%** | **95.7%** |

Table 4.1: Per-condition syntactic parsability rates for the three primary models.
Weighted averages are calculated across all target stories for each model (ChatGPT:
450/470 parsible; DeepSeek: 430/470; Gemini: 450/470).

ChatGPT 5.0 and Gemini 2.5 Pro achieved very similar weighted-average parsability
rates of 95.7%, with their only syntactic failures concentrated entirely in the zero-shot
condition. DeepSeek V3.1 achieved a lower weighted average of 91.5%, despite recording
the single best performance of any model (99.0% in the zero-shot condition). This
paradoxical result---the best individual-condition score belonging to the lowest overall
performer---illustrates the differential effect of prompting on each model's syntactic
output. ChatGPT and Gemini were brittle in the absence of exemplars but became
perfect once exemplars were introduced. DeepSeek was near-perfect in isolation but
became syntactically less reliable when exemplars and instructional documents were
added to its context.

4.3.2 Effect of Shot Count on Syntactic Correctness

The relationship between shot count and syntactic correctness was neither monotonic
nor uniform across models.

For ChatGPT and Gemini, the transition from zero-shot to any few-shot configuration
was sufficient to eliminate all syntactic errors. Five exemplars were as effective as
ten, and the addition of further exemplars neither improved nor degraded their
performance. This suggests that these models did not require a large or diverse exemplar
set to learn the syntactic conventions of the ASP output format; a minimal demonstration
of the period-delimited convention, quoted-entity formatting, and predicate arity was
sufficient.

For DeepSeek, the relationship was more complex and exhibited a U-shaped pattern.
DeepSeek's syntactic performance was strongest in the extreme conditions---zero-shot
(99.0%) and the most richly specified condition, 10-shot V2 (100.0%)---and weakest
in the intermediate conditions. In the 5-shot V1 condition, DeepSeek's parsability
dropped to 77.9%, and even with the supplementary encoding guide in the V2
configuration it rose only to 84.2%. The 10-shot configuration substantially recovered
this deficit, achieving 96.7% in V1 and 100% in V2.

We interpret this pattern as follows. In the zero-shot setting, DeepSeek appears to
operate from a default internal template that produces syntactically clean output.
The introduction of five diverse exemplars disrupts this template without providing
sufficient coverage to establish a new robust convention: DeepSeek learns that the
examples use `X` as a variable in the context of rules with bodies, but fails to
generalise the safety constraint that facts must not contain free variables. The
result is the unsafe-variable errors documented in Section 4.2.2. By the time ten
exemplars are provided, the broader coverage of syntactic patterns---including cases
where unspecified entities are handled via default constants rather than variables---is
sufficient to re-establish high parsability.

This nonlinear relationship underscores an important nuance for prompt engineering:
*more* exemplars do not always produce *better* syntax, and models may pass through
a region of degraded performance at intermediate shot counts before converging to a
higher-quality output regime.

4.3.3 Effect of the Supplementary Encoding Guide

The `additional_info.md` document was introduced in the V2 variants of the 5-shot and
10-shot conditions to provide explicit heuristics for encoding edge cases, negation
formatting, role compression, and unspecified-entity handling. Its effect on syntactic
validity was not uniformly beneficial.

For ChatGPT and Gemini, `additional_info.md` had no measurable effect on syntactic
parsability, as both models already achieved 100% in the V1 configurations. The
document neither improved nor harmed their output.

For DeepSeek, the effect was condition-dependent and ambivalent. In the 5-shot
setting, the encoding guide produced a modest improvement in overall parsability (from
77.9% to 84.2%), reducing the unsafe-variable error count from 21 to 2. However, this
improvement was accompanied by the emergence of a novel and severe failure mode:
the insertion of the Chinese character 极 into predicate tokens, string literals, and
numeric arguments, accounting for 12 of the 15 remaining failures (Section 4.2.3).
The net effect was an improvement of 6.9 percentage points in parsability, but the
cost was the introduction of a qualitatively more severe error type---corrupted tokens
are harder to diagnose and repair than unsafe variables.

In the 10-shot setting, the effect was unambiguously positive: DeepSeek's parsability
rose from 96.7% to 100%, and the character-corruption failure mode did not appear.
The larger exemplar set appears to have stabilised DeepSeek's output distribution
sufficiently to prevent the cross-lingual token interference observed in the 5-shot V2
condition.

This dual effect of `additional_info.md`---partial syntactic improvement at the cost
of a novel failure mode in one condition, and complete syntactic resolution in
another---highlights a tension in supplementary documentation. The additional context
can provide useful syntactic guidance, as evidenced by the reduction in unsafe-variable
errors. However, longer prompts also shift the model's output distribution into less
predictable regions, where token-level hallucinations become more likely. The practical
implication is that supplementary instructional documents should be paired with
adequate exemplar coverage to stabilise the model's generation.

4.3.4 Common Parser Errors and Failure Mode Taxonomy

Synthesising the failure analyses from Sections 4.2.1 through 4.2.5, we identified six
distinct categories of syntactic failure. Table 4.2 presents their distribution across
models and conditions.

| Failure Mode | Affected Models | Conditions | Occurrences |
|---|---|---|---|
| Missing terminating periods | ChatGPT, Gemini | ZeroShot-V1 | 40 |
| Unsafe free variables | DeepSeek | FewShot-5-Random-V1, FewShot-5-Random-V2, FewShot-10-Random-V1 | 22 |
| Chinese character corruption | DeepSeek | FewShot-5-Random-V2 | 12 |
| Incorrect predicate names | DeepSeek | FewShot-10-Random-V1 | 2 |
| Stray punctuation | DeepSeek | ZeroShot-V1 | 1 |
| Missing output | DeepSeek | FewShot-5-Random-V1 | 2 |

Table 4.2: Distribution of syntactic failure modes across models and conditions.
A total of 79 invalid encodings were observed across 1,410 total predicted outputs
(5.6% overall syntactic failure rate).

The failure modes fall into two broad classes. **Format-level errors**---missing periods
and stray punctuation---account for 41 of 79 failures (51.9%) and are the only syntactic
errors that affect ChatGPT and Gemini. These errors are purely surface-form issues:
the predicates are internally well-formed (correct arity, balanced parentheses, properly
quoted strings) but fail to respect the delimiters required by the clingo parser. The
uniformity of the missing-period pattern across 40 independent failures suggests that
ChatGPT and Gemini share a common default output convention for ASP-like text---a
space-delimited token sequence---that is incompatible with clingo's grammar.

**Content-level errors**---unsafe variables, character corruption, incorrect predicate
names, and missing outputs---account for 38 of 79 failures (48.1%) and are exclusive to
DeepSeek. These errors reflect deeper issues in how the model maps natural language
entities and actions to formal predicate structures. The unsafe-variable pattern
(22 occurrences, the single most frequent DeepSeek failure) reveals a conceptual gap:
the model understands that an entity exists (e.g., "food" was ordered) but fails to
instantiate it with a concrete constant, substituting a free variable instead. The
character-corruption pattern (12 occurrences) represents a qualitatively different
failure mechanism---a token-level hallucination that produces syntactically malformed
tokens rather than simply unsafe ones. Its appearance only in the condition where
`additional_info.md` was added without adequate exemplar stabilisation (5-shot V2)
marks it as a pathology of prompt-destabilised generation rather than a conceptual
error.

The overall syntactic failure rate of 5.8% indicates that, across all conditions and
models, approximately 1 in every 17 generated encodings is syntactically unparsable.
However, this aggregate statistic masks the wide variation documented above: the
failure rate ranges from 0% (in three of the five conditions for ChatGPT and Gemini,
and in FewShot-10-Random-V2 for all models) to 22.1% (DeepSeek in FewShot-5-Random-V1).
The sensitivity of these rates to prompting configuration---and the differential
sensitivity across models---is a central finding of this syntactic evaluation.

In summary, the syntactic evaluation establishes that reliable ASP syntax generation
is achievable across all three primary models under the right prompting configuration
(ten diverse exemplars combined with explicit encoding heuristics). The performance
ranking, weighted across conditions, places ChatGPT 5.0 and Gemini 2.5 Pro at 95.7%
parsability, with DeepSeek V3.1 trailing at 91.5%. However, DeepSeek's trajectory
across conditions suggests that its syntactic competence is fundamentally high---it
achieves 99% in zero-shot---but its output mechanism is more sensitive to prompt
perturbation than its counterparts. The practical implication is that prompt engineering
for DeepSeek requires particular attention to exemplar diversity and documentation
stability: too few exemplars invite unsafe-variable errors, while supplementary
documents in the absence of sufficient exemplars can trigger token-corruption
pathologies. With adequate exemplar coverage and explicit heuristics, all three
models achieve 100% syntactic validity, providing a reliable foundation for the
semantic evaluation in Section 4.4.
