---
name: project-context
description: Maintain .context/ artifacts as living documentation. Can also bootstrap or refresh artifacts from existing code.
---

# Project Context

Manage the `.context/` living documentation.

**Primary Goal**: Keep `DESIGN.md`, `ARCHITECTURE.md`, `CHANGELOG.md` in sync with code *as you edit*.

**Artifact Definition:**
| File | Purpose | Update When |
|------|---------|-------------|
| [OVERVIEW.md](OVERVIEW.md) | Project scope and purpose | Dependencies, features change |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Module structure and data flow | Structure changes |
| [CONVENTIONS.md](CONVENTIONS.md) | Code patterns and standards | New patterns established |
| [DESIGN.md](DESIGN.md) | Feature status tracking | Features added/completed |
| [CHANGELOG.md](CHANGELOG.md) | Released changes | Any meaningful change |

**After Changes:**
Update the artifacts relevant to your change according to the table above.

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
3. **Draft `OVERVIEW.md`**: Summarize based on dependencies and features.
4. **Scrub `DESIGN.md`**: Verify implemented status against actual code.
5. **Report**: Summarize what was updated.

## Enforcement
**Definition of Done**:
- [ ] Code changes reflected in artifacts?
- [ ] `CHANGELOG.md` updated?
- [ ] TaskStatus set to "Updating .context artifacts"?
