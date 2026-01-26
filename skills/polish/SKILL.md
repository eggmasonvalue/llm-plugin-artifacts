---
name: polish
description: Review and improve code quality. Run quality checks, tests, and update changelog. Use this when the user wants to polish the code or check for quality issues.
---

# Polish

Run quality checks, tests, and update changelog.

## Steps

### 1. Code Quality
Run ruff for linting and formatting:
```bash
uv run ruff check . --fix
uv run ruff format .
```

Review any remaining issues and fix.

### 2. Docstrings & Types
Check that:
- Public functions have Google-style docstrings
- Function signatures have type hints
- Modules have purpose docstrings

Add any missing documentation.

### 3. Run Tests
```bash
uv run pytest --cov
```

Fix any failures. Note coverage percentage.

### 4. Update CHANGELOG
Add entry to `.context/CHANGELOG.md`:
```markdown
## [YYYY-MM-DD]
- <summary of changes made>
```

### 5. Report
Summarize:
- Lint issues fixed
- Tests passed/failed
- Coverage percentage
- Changelog updated
