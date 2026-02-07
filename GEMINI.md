---
description: Keep .context/ artifacts in sync with code
---
# Context Artifacts Rule

**Definition of Done**: A task is ONLY complete when `.context/` artifacts reflect the code changes.

## Enforcement
1. **Always Read**: Start every session by reading `.context/OVERVIEW.md`.
2. **Explicit Step**: You MUST set `TaskStatus` to "Updating .context artifacts" before finishing any coding task.
3. **Verify**: Do not call `notify_user` until you have confirmed `DESIGN.md`, `ARCHITECTURE.md`, and `CHANGELOG.md` stay true to the codebase.

**CRITICAL**: Code without context updates is considered BROKEN.
**CRITICAL**: DO NOT USE THE .CONTEXT LOCATION FOR GOOGLE ANTIGRAVITY IDE'S FIRST PARTY ARTIFACTS.