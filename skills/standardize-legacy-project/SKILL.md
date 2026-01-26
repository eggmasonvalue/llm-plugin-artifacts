---
name: standardize-legacy-project
description: Modernize legacy projects or unmanaged codebases. Initializes git, standardizes toolchain (uv), and bootstraps .context/ artifacts. Use this when you find a project with missing git, old config, or no documentation.
---

# Standardize Legacy Project

Bring an existing coding folder up to modern standards.

## Steps

### 1. Git Standardization
Ensure git is healthy and configured for the personal user.

1. **Check Git Status**:
   - If not a repo: `git init`
   - If `user.name` != "eggmasonvalue":
     ```bash
     git config user.name "eggmasonvalue"
     git config user.email "kirubhasshankarkbs@gmail.com"
     ```
   - Check remotes: ensure `origin` points to `github-test` alias if using GitHub.

2. **Fix .gitignore**:
   Ensure `__pycache__/`, `*.pyc`, `.venv/`, `.mv/`, `.DS_Store` are ignored.

### 2. Toolchain Modernization (uv)
Switch to `uv` for dependency management.

1. **Check for existing deps**:
   - Look for `requirements.txt`, `Pipfile`, `setup.py`.
2. **Initialize uv**:
   ```bash
   uv init
   ```
3. **Migrate Dependencies**:
   - `uv add <libs>` for each library found in old files.
   - `uv add --dev ruff pytest pytest-cov`

### 3. Bootstrap Context
Establish living documentation.

1. **Create Directory**: `mkdir .context`
2. **Trigger Bootstrap**:
   Use the `project-context` skill (Full Refresh capability) to analyze the code and generate:
   - `ARCHITECTURE.md` (reverse engineered)
   - `DESIGN.md` (current state audit)

### 4. Code Quality Baseline
Run a first pass to see how "dirty" the code is, but **do not fix all errors** automatically unless asked (to avoid massive diffs).

1. `uv run ruff check .` (report count)
2. `uv run pytest` (report status)

### 5. Report
Summarize:
- Git status (newly initialized or fixed)
- Toolchain (migrated to uv)
- Context (Analysis complete)
- Quality State (Ruff error count, test status)
