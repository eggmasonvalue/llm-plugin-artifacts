---
name: release
description: Prepare a versioned release. Version bump, finalize changelog, tag, and push. Use this when the user requests a release.
---

# Release

Version bump, finalize changelog, tag, and push.

## Steps

### 1. Get Version Bump
Ask user: **patch**, **minor**, or **major**?

Current version from `pyproject.toml`:
```toml
[project]
version = "X.Y.Z"
```

### 2. Update Version
Bump version in `pyproject.toml` according to semver:
- patch: X.Y.Z → X.Y.(Z+1)
- minor: X.Y.Z → X.(Y+1).0
- major: X.Y.Z → (X+1).0.0

### 3. Finalize CHANGELOG
In `.context/CHANGELOG.md`, rename `## [Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD`.

Add new `## [Unreleased]` section at top.

> [!IMPORTANT]
> **Consolidation Challenge:** If the codebase has undergone rapid iteration with multiple piecemeal `[YYYY-MM-DD]` entries since the last release, consolidate all these and the current `[Unreleased]` content into the new `## [X.Y.Z]` block. This ensures a clean, version-oriented history rather than a fragmented daily log.

### 4. Run Polish Skill
Execute the polish skill (`polish` folder) to ensure quality.

### 5. Commit Release
```bash
git add .
git commit -m "Release vX.Y.Z"
```

### 6. Tag
```bash
git tag vX.Y.Z
```

### 7. Push
```bash
git push origin main --tags
```

### 8. Report
Confirm:
- Version bumped to X.Y.Z
- Changelog finalized
- Tag created
- Pushed to github-test remote
