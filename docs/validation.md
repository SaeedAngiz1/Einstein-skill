# Validation record

Authoring checks performed on 2026-11-01, on Windows with Python 3.13 and Skills CLI 1.7.4.

| Check | Observed result |
| --- | --- |
| Skill creator's `quick_validate.py` | Pass: skill frontmatter and entrypoint accepted. |
| Repository `scripts/validate.py` | Pass: skill metadata, invocation metadata, internal resource links, SVG parsing, and 10 evaluation case definitions. |
| Missing linked resource in an isolated package copy | Validator rejected the package as expected. |
| Missing invocation metadata in an isolated package copy | Validator rejected the package as expected. |
| Skills CLI local discovery | Found exactly one skill: `einstein-skill`. |
| Skills CLI install for Claude Code and Codex | Succeeded in an isolated temporary project with `--copy`. |
| Installed skill content | All four distributable files matched the source by SHA-256 in both installation destinations. |
| Banner rendering | Rendered the SVG in headless Edge at 1280 x 640 and visually inspected it. |

The repository's [Actions workflow](https://github.com/SaeedAngiz1/Einstein-skill/actions/workflows/validate.yml) runs package validation on Ubuntu and Windows with Python 3.11 and 3.13. Consult its live run results for CI status; defining the workflow alone isn't evidence of a passing run.

These checks establish package and installer behavior. They don't establish how a Claude Code or Codex model behaves when using the skill. The 10 behavioral cases are **definitions**, not executed model evaluations. No controlled comparison, paid inference, live workflow, or productivity benchmark was performed.

The source clip was processed locally. Original media and its transcript are excluded from the package.
