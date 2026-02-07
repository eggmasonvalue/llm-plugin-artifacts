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
└── README.md
```

### 3. Initialize uv (Python 3.12)
```bash
uv init --python 3.12
uv add --dev pytest pytest-cov ruff
```

> uv auto-downloads Python 3.12 and manages the virtual environment internally. No manual venv setup needed.

### 4. Configure Git
1. Read identity from `skills/user_identity.md`.
2. Initialize repository and set config:
```bash
git init
git config user.name "<Git Name from user_identity.md>"
git config user.email "<Git Email from user_identity.md>"
```

3. Set remote to use the identity:
```bash
git remote add origin git@<SSH Alias from user_identity.md>:<Git Name from user_identity.md>/<project-name>.git
```

### 5. Scaffold .context/ Artifacts

Create placeholder artifacts:
- `OVERVIEW.md` — Purpose and description from user input
- `DESIGN.md` — `## Features` header only
- `ARCHITECTURE.md` — Basic src/tests structure diagram
- `CONVENTIONS.md` — Link to code-quality skill standards
- `CHANGELOG.md` — Initial entry with scaffold date

### 6. Initial Commit
```bash
git add .
git commit -m "Initial project scaffold"
```

### 7. Report
Confirm project created, remind user to:
- Create GitHub repo named `<project-name>`
- Push with `git push -u origin main`
