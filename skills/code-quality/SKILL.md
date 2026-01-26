---
name: code-quality
description: >-
  Enforce maintainable, agent-friendly Python code. Use this skill to check and fix code style, types, and documentation before considering a file complete.
---

# Code Quality Skill

Ensure Python code is clean, typed, and documented.

## Tools

Use `ruff` for linting and formatting:
```bash
uv run ruff check . --fix
uv run ruff format .
```

## Standards

### Type Hints
All function signatures must have type hints:
```python
def calculate_total(items: list[Item], tax_rate: float) -> Decimal:
```

### Docstrings (Google Style)
Public functions and classes require docstrings:
```python
def fetch_user(user_id: str) -> User:
    """Retrieve a user by their unique identifier.

    Args:
        user_id: The unique identifier for the user.

    Returns:
        The User object if found.

    Raises:
        UserNotFoundError: If no user matches the ID.
    """
```

### Module Docstrings
Every `.py` file starts with a docstring explaining its purpose:
```python
"""User authentication and session management.

Handles login, logout, and session token lifecycle.
"""
```

## Checklist

Before considering code complete:
- [ ] `ruff check` passes
- [ ] `ruff format` applied
- [ ] Public APIs have docstrings
- [ ] Functions have type hints
- [ ] Modules have purpose docstrings
