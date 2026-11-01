# Einstein-skill in practice

These are illustrative decisions, not measured model outputs.

## An ambiguous export

**Request:** "Export the table."

First inspect the table, existing export patterns, and acceptance notes. If the app already defines export as filtered visible rows, reuse that behavior. If all rows versus filtered rows remains unresolved and changes the output, ask that specific question before implementation.

Once resolved, implement the export directly. Verify ordering, empty results, and proper CSV escaping if CSV is the chosen format. Formula injection handling may also be required for spreadsheet-bound data; a minimal solution still addresses realistic requirements.

Avoid creating an export plugin framework just because other formats could be useful later.

## A duplicate payment bug

**Request:** "Double-clicking Pay sometimes charges twice."

Trace the submission path and existing payment idempotency. Reproduce two submissions using a provider stub or test environment; no real charges are needed. Confirm the failure is duplicate processing rather than an unrelated setup error.

Fix the actual duplication path. Disabling the button alone may not address concurrent requests or retries. Check the same reproducer, the normal single-payment path, and relevant retry behavior. Report exactly which layer was tested.

If no test environment or reliable reproducer is available, explain what was inspected and label the patch unverified. A guessed test result isn't evidence.

## A simpler implementation

**Request:** "Show the total price of these items."

Reuse the application's money representation and currency rules. If one existing aggregation operation is sufficient, use it. Don't add strategy classes, a registry, and configuration for hypothetical pricing modes.

If actual requirements include multiple currencies or rounding rules, that complexity is real. Preserve it. A line-count reduction that changes money behavior fails the task.

## An unfamiliar compatibility branch

**Request:** "Fix the header overlap on mobile."

Inspect the component and the styles affecting its layout. Change the necessary layout behavior and inspect narrow and wide viewports. Preserve an unfamiliar compatibility branch unless evidence establishes that changing it is required.

If a shared layout component causes the issue, a shared-component change can be justified. Check other affected consumers instead of forcing an artificial one-file patch.

## A document edit

**Request:** "Update the delivery date in the proposal."

Find the requested date and related references. Update the relevant occurrences and inspect the rendered result when layout can change. Preserve pricing, scope, tone, and clauses. If different dates refer to different milestones, resolve which milestone is being changed.

Don't turn a date correction into a rewrite of the proposal.

## A design task

**Request:** "Make this checkout usable on a phone."

Inspect the actual flow, identify the failing interaction, and use available design constraints. Verify the result at relevant narrow viewports, including input, errors, and focus behavior. A build passing doesn't establish that the checkout is usable.

If user testing isn't performed, describe the interaction and layout checks that were performed without claiming customer validation.

## Research and strategy

**Request:** "Tell me which acquisition channel to test first on a small budget."

Use the product, audience, geography, constraints, and existing results. Resolve missing information only when it changes the choice. Separate verified facts from assumptions. Recommend one bounded experiment with a budget, observable conversion event, and stopping rule appropriate to the supplied constraints.

A plan's internal consistency is not evidence of customer demand. State which observations would support or reject the recommendation. Don't launch campaigns or spend money unless authorized.
