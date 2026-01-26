---
description: Bootstrap a new Python project
---

# /new-project

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
│   ├── README.md
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

### 4. Configure Git (Personal Account)
```bash
git init
git config user.name "eggmasonvalue"
git config user.email "kirubhasshankarkbs@gmail.com"
```

Set remote to use `github-test` SSH alias:
```bash
git remote add origin git@github-test:eggmasonvalue/<project-name>.git
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