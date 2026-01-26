---
name: project-context
description: >-
  Maintain .context/ artifacts as living documentation. Use this skill whenever code changes affect design, structure, or behavior to keep documentation in sync.
---

# Project Context Skill

You maintain a `.context/` folder containing living documentation that stays in sync with code.

## On Every Task

### Before Starting
1. Read relevant artifacts to understand current state
2. Check `DESIGN.md` status markers to know what exists vs. planned

### After Changes
Update artifacts based on what changed:

| Change | Artifact |
|--------|----------|
| Feature started | `DESIGN.md` → status to `[implementing]` |
| Feature done | `DESIGN.md` → `[done]`, add to `CHANGELOG.md` |
| Structure changed | `ARCHITECTURE.md` |
| New pattern | `CONVENTIONS.md` |
| Any meaningful change | `CHANGELOG.md` |

## Status Markers

In `DESIGN.md`, each feature has a status:

```
[idea]         — Concept only, no code
[designing]    — Being detailed, no code yet
[implementing] — Code in progress
[done]         — Complete and working
```

## Principles

- **Concise** — Summaries, not code duplicates
- **Incremental** — Update what changed, don't rewrite
- **Visual** — Use mermaid diagrams for flows/relationships

## Enforcement Checklist

**Do not signal task completion until:**

- [ ] `DESIGN.md` status matches reality?
- [ ] `ARCHITECTURE.md` reflects structural changes?
- [ ] `CONVENTIONS.md` captures new patterns?
- [ ] `CHANGELOG.md` has a new entry?
- [ ] **TaskStatus** was set to "Updating .context artifacts"?
