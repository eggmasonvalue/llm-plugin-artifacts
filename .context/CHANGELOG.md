# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2026-01-26
### Added
- Initialized `.context/CHANGELOG.md` and `.context/README.md`.
- Established release workflow compliance.

## [2.0.1] - 2026-01-26
### Fixed
- Restored `GEMINI.md` to repository root.
- Created symlink for `GEMINI.md` in `C:\Users\uig55220\.gemini`.

## [Unreleased]
### Changed
- Renamed `antigravity-skill-mirroring` to `antigravity-skill-manager`.
- Expanded scope of `antigravity-skill-manager` to include skill modification and location management.
- Updated global workflows to reflect the new skill name.

## [2.1.0] - 2026-01-26
### Changed
- Improved `mirror_skills.py` to correctly parse multi-line YAML frontmatter (fixes empty descriptions for `code-quality`).
- Renamed `antigravity-skill-mirroring` to `antigravity-skill-manager`.
- Expanded capability of `antigravity-skill-manager` to find and modify skills.

## [2.2.0] - 2026-01-26
### Changed
- Merged `sync-context` into `project-context` skill.
- Added progressive discovery rules for full context refresh in `project-context`.
- Removed standalone `sync-context` skill.

## [1.0.1] - 2026-01-26
- Previous release.
