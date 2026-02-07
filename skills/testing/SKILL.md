---
name: testing
description: >-
  Pytest conventions for testable Python code. Use this skill when writing or modifying tests to ensure coverage and structure standards are met.
---

# Testing Skill

Ensure code is tested with pytest.

## Running Tests

```bash
uv run pytest --cov
```

## Conventions

### File Naming
```
tests/
├── test_<module>.py      # Unit tests mirror src structure
├── test_integration.py   # Cross-module tests
└── conftest.py           # Shared fixtures
```

### Test Naming
```python
def test_<what>_<condition>_<expected>():
    """Verify that <what> does <expected> when <condition>."""
```

Example:
```python
def test_login_with_invalid_password_returns_error():
    """Verify that login returns an error when password is invalid."""
```

### Test Structure (AAA)
```python
def test_example():
    """Docstring explaining intent."""
    # Arrange
    user = create_test_user()
    
    # Act
    result = login(user.email, "wrong_password")
    
    # Assert
    assert result.is_error
    assert "invalid password" in result.message
```

## Requirements

- Every test function has a docstring
- Tests are independent (no shared mutable state)
- Use fixtures for common setup
- Target: 80% coverage minimum
