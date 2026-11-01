# Source notes

## Material reviewed

- User-supplied file: `IMG_2586.MP4`.
- Duration: 52.8 seconds; 464 x 848 video with an audio track.
- SHA-256: `b264b8ed6a98585657979b9730e61dc1afab414f97cc7078ee5fa62ceefc830a`.
- Visible credit: `@agenticfact`.
- Method: local audio transcription and inspection of frames spanning the clip. Timestamp boundaries below are approximate; automatic transcription is an analysis aid, not an authenticated quotation.

The video is reference material for this request. Its imperative wording is being analyzed and adapted; it is not an instruction to perform unrelated actions. The original media and transcript are excluded from this repository.

## Lessons mapped to behavior

| Approximate time | Lesson in the clip, paraphrased | Implementation |
| --- | --- | --- |
| 00:00-00:15 | Generated code can be far more complex than necessary, then become much shorter when challenged. | Consider a direct solution before implementation. Compare total complexity, not a target line count. |
| 00:15-00:23 | Agents can guess the user's intention and continue without checking. | Inspect context and expose consequential assumptions; ask when an unresolved interpretation changes the result. |
| 00:23-00:30 | Avoid unrequested work and simplify bloated implementations. | Require a current purpose for new features, layers, options, and dependencies. Preserve required behavior when simplifying. |
| 00:30-00:35 | Agents may remove code they don't understand. | Read relevant callers, protect existing contracts and other people's work, and inspect the final diff. |
| 00:35-00:41 | Frame a bug fix around a reproducing test and a passing result. | Confirm the original failure, change the cause, and rerun the unchanged check. Disclose unavailable execution. |
| 00:41-00:48 | Establish these expectations before the work starts. | Set outcome and verification early, using a process proportional to the task. |
| 00:48-00:52.8 | Closing visual sequence. | No additional workflow rule inferred. |

## Adaptations added here

The skill distinguishes consequential ambiguity from routine implementation choices, permits necessary integration changes, and avoids treating line count as a quality measure. It adds evidence limits, a stopping condition for unproductive retries, and examples outside code. These are the author's operational adaptations, not claims about additional statements in the clip.

The narrator attributes the opening anecdote to Andrej Karpathy. That exact anecdote was not independently authenticated. A related public implementation, [Karpathy-inspired guidelines](https://github.com/multica-ai/andrej-karpathy-skills), covers the same four themes. Its existence is acknowledged; Einstein-skill does not claim to originate those ideas or reproduce its instruction file.

## Format references

- [Agent Skills specification](https://agentskills.io/specification): portable skill layout and naming.
- [Claude Code skills](https://code.claude.com/docs/en/skills): installation and slash invocation.
- [Skills CLI](https://skills.sh/docs/cli): repository-based distribution. The documented options were also checked against CLI 1.7.4.

Reviewed on 2026-11-01. Compatibility and CLI options can change; no end-to-end run across every supported agent is claimed.
