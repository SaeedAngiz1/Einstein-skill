# Evaluate behavior, not the slogan

The cases in [evals/cases.json](../evals/cases.json) describe observable successes and failures. They are an evaluation set, not recorded results. Structural validation ensures the cases are present and well formed; it doesn't run an agent or judge its decisions.

## A practical comparison

1. Start from a reproducible task and a frozen copy of its artifacts. Define acceptance before running either condition.
2. Give one fresh session the task without this skill. Give another fresh session the identical task with this skill. Keep model, tools, permissions, context, and budget the same. Don't give either session the other one's answer.
3. Collect each session's questions, final artifact or diff, tool results, and verification evidence. Use independent scratch copies; don't let a session modify the baseline for the other condition.
4. Judge each run against the case's acceptance and failure criteria. Evaluate behavior and correctness before counting lines, tool calls, time, or tokens. If a run doesn't complete, record that instead of dropping it.
5. Repeat when drawing conclusions about a model. Alternate which condition runs first. Report all attempts and relevant variability.

Agent runs, paid inference, or live external actions require whatever authorization the evaluation environment normally requires. Synthetic fixtures should use local files, test data, and stubs rather than live payments or publishing.

## Suggested record

| Field | Record |
| --- | --- |
| Task / case ID | Exact prompt and fixture revision |
| Environment | Model version, client, tools, permissions, and budget |
| Condition | Skill enabled or baseline |
| Acceptance | Pass, fail, or unresolved, with observable evidence |
| Scope | Required and unrelated changes |
| Clarification | Necessary questions, unnecessary questions, and silent assumptions |
| Verification | Commands or inspections actually performed and their results |
| Cost / duration | Observed values and measurement method, if available |
| Limits | Missing environment, incomplete execution, or evaluator uncertainty |

For a bug case, a pass requires a reproducer that fails for the reported reason before the fix and passes afterward. For a trivial edit, a long plan and unnecessary questions count against the result. For simplification, behavior and readability must survive.

## What this release establishes

The repository supplies a runnable package validator, portable skill instructions, source notes, and evaluation cases. No controlled model comparison has been performed as part of authoring. Package and install checks establish packaging behavior only. They don't establish a reduction in errors, tokens, or elapsed time, and don't predict how consistently a model will follow the instructions.

Share concrete failing cases. A narrowly demonstrated failure is more useful than adding another universal rule.
