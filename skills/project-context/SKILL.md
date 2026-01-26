---
name: project-context
description: Maintain .context/ artifacts as living documentation. Can also bootstrap or refresh artifacts from existing code.
---

# Project Context

Manage the `.context/` living documentation.

**Primary Goal**: Keep `DESIGN.md`, `ARCHITECTURE.md`, `CHANGELOG.md` in sync with code *as you edit*.

## Capabilities

### 1. Maintain (Standard Workflow)
Use this when making code changes.

**Before Starting:**
1. Read relevant artifacts.
2. Check `DESIGN.md` status (`[idea]`, `[implementing]`, etc.).

**Status Markers:**
- `[idea]` → Concept
- `[designing]` → Specs exist
- `[implementing]` → Coding
- `[done]` → Shipped

**After Changes:**
| Change | Artifact |
|--------|----------|
| Feature started | `DESIGN.md` → `[implementing]` |
| Feature done | `DESIGN.md` → `[done]`, `CHANGELOG.md` |
| Structure/Arch | `ARCHITECTURE.md` |
| Patterns | `CONVENTIONS.md` |

### 2. Full Refresh / Bootstrap (Progressive)
**Trigger**: 
1. The `.context/` folder does not exist.
2. User explicitly asks for "full refresh", "sync context", or "regenerate docs".

> [!CAUTION]
> **User Confirmation Required**: If the `.context/` folder ALREADY exists, you **MUST** ask the user for confirmation before performing a full refresh:
> *"You already have context artifacts. A full refresh might overwrite your manually curated design notes. Do you want to proceed with a full re-analysis?"*

**Steps for Refresh:**
1. **Analyze Code**: Scan source for modules, classes, and relationships.
2. **Regenerate `ARCHITECTURE.md`**: Create Mermaid diagrams and abstraction lists.
3. **Draft `OVERVIEW.md` / `README.md`**: Summarize based on dependencies and features.
4. **Scrub `DESIGN.md`**: Verify implemented status against actual code.
5. **Report**: Summarize what was updated.

## Enforcement
**Definition of Done**:
- [ ] Code changes reflected in artifacts?
- [ ] `CHANGELOG.md` updated?
- [ ] TaskStatus set to "Updating .context artifacts"?
