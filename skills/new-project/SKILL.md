---
name: new-project
description: Bootstrap a new Python project with uv, personal git, and .context/ artifacts. Use this skill when the user wants to start a new Python project or repository.
---

# New Project

Scaffold a new Python project with uv, personal git, and .context/ artifacts.

## Steps

### 1. Get Project Info
Ask the user for:
- Project name (kebab-case for folder, snake_case for package)
- One-line description

### 2. Create Structure
```
<project-name>/
├── src/
│   └── <package_name>/
│       └── __init__.py
├── tests/
│   └── test_placeholder.py
├── .context/
│   ├── OVERVIEW.md
│   ├── DESIGN.md
│   ├── ARCHITECTURE.md
│   ├── CONVENTIONS.md
│   └── CHANGELOG.md
├── pyproject.toml
├── .gitignore
├── AGENTS.md
├── GEMINI.md
└── README.md
```

### 3. Initialize uv (Python 3.12)
```bash
uv init --python 3.12
uv add --dev pytest pytest-cov ruff
```

### 4. use gh cli to create the remote repo and set it up.

### 5. Scaffold .context/ Artifacts

Create placeholder artifacts:
- `OVERVIEW.md` — Purpose and description from user input
- `DESIGN.md` — `## Features` header only
- `ARCHITECTURE.md` — Basic src/tests structure diagram
- `CONVENTIONS.md` — Link to code-quality skill standards
- `CHANGELOG.md` — Initial entry with scaffold date

Create AGENTS.md in root with the following content:

```markdown
# Context Artifacts Rule
.context/ artifacts are living documentation for the code. Keep .context/ artifacts in sync with code at all times.

**Artifact Definition:**
| File | Purpose | Update When |
|------|---------|-------------|
| [.context/OVERVIEW.md](.context/OVERVIEW.md) | Project scope and purpose | Dependencies, features change |
| [.context/ARCHITECTURE.md](.context/ARCHITECTURE.md) | Module structure and data flow. Use mermaid diagrams where sensible | Structure changes |
| [.context/CONVENTIONS.md](.context/CONVENTIONS.md) | Code patterns and standards | New patterns established |
| [.context/DESIGN.md](.context/DESIGN.md) | Feature status tracking | Features added/completed |
| [.context/CHANGELOG.md](.context/CHANGELOG.md) | Released changes | Any meaningful change |

**Definition of Done**: A task is complete ONLY when `.context/` artifacts reflect the code changes. Code without context updates is considered BROKEN. 
```
symlink AGENTS.md to GEMINI.md in the same directory
```bash
ln -sf AGENTS.md GEMINI.md
```

### 6. Initial Commit
```bash
git add .
git commit -m "Initial project scaffold"
```

### 7. Report
Confirm project created, remind user to:
- Push with `git push -u origin main`
