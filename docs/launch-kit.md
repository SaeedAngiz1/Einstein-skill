# Launch kit

## Positioning

**Einstein-skill: think first, build less, prove it.**

For people who use coding agents and keep receiving oversized patches, silent guesses, and unsupported completion claims. The useful distinction is calibrated execution: ask about consequential ambiguity, keep edits focused, and choose evidence that actually demonstrates the result.

The four core themes are established ideas. Lead with the practical implementation and real examples, not a claim to have invented a new intelligence method.

## Short launch post

I made Einstein-skill for a familiar AI coding problem: a small request becomes a big patch, and you still have to ask whether it works.

It teaches the agent to expose consequential assumptions, keep changes focused, choose a simple complete solution, and verify the result.

Markdown. No API key. Includes evaluation cases so you can test it on your own workflow.

Try it: https://github.com/SaeedAngiz1/Einstein-skill

What task would you use to expose an overengineering agent?

## A 30-second demo to record

This is a recording outline, not a claim that the demo has been run.

- **0-5 seconds:** Show one real, reproducible bug and the exact user request.
- **5-12 seconds:** Show the agent locating the relevant path and confirming the failure. Display the actual output.
- **12-22 seconds:** Show the focused fix and the unchanged reproducer passing.
- **22-27 seconds:** Show the final diff and a concise account of what was verified.
- **27-30 seconds:** Show the repo name and install command.

If comparing a baseline with the skill, record matched fresh sessions and publish the full artifacts as well as the short clip. Label edited time and illustrative material. Don't stage an intentionally poor baseline or invent a savings percentage.

## Launch sequence

1. Record a real task using the [evaluation protocol](evaluation.md). Prefer a small example that a viewer can reproduce.
2. Attach the full prompt, diff, test output, and environment to the demo. Make the evidence easy to inspect.
3. Publish the clip with the repository link where your intended users already discuss coding agents, following that community's posting rules.
4. Ask for a specific counterexample. Turn demonstrated failures into focused improvements and publish the resulting comparison.

The first bottleneck is evidence: a memorable name and banner help people notice the repo; a reproducible result gives them a reason to share it. The next action is to record one honest demo, not add more branding.

The [social preview image](../assets/social-preview.png) is ready for GitHub's repository Settings > Social preview upload. The README uses a [looping GIF](../assets/hero-animated.gif) rendered from the editable [SVG source](../assets/hero.svg), with the static image selected for reduced-motion preferences. Regenerate both with [scripts/render_readme.py](../scripts/render_readme.py). Providing the image doesn't imply the repository setting has been configured.
