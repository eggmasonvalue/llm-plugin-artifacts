---
name: antigravity-skill-manager
description: Manage Antigravity skills. Mirror skills as workflows, locate skill definitions, and enable skill modification.
---

# Antigravity Skill Manager

This skill is the central manager for Antigravity skills. It handles:
1. **Mirroring**: Exposing skills as global workflows (slash commands).
2. **Maintenance**: finding and editing skill definitions.

## Capabilities

### 1. Modify Existing Skills
When the user asks to "modify", "update", or "edit" a skill:

1. **Locate**: Find the skill in `d:\Misc2\01_Software_Projects\AI_Tools\AI skill workflow setup\skills\<skill-name>`.
2. **Edit**: Use `view_file` to read `SKILL.md` or scripts, then `replace_file_content` to make changes.
3. **Verify Symlinks**: Ensure the skill is correctly linked in `C:\Users\uig55220\.gemini\antigravity\skills`.
   - If missing, create the symlink.
4. **Mirror**: Run the mirroring script if the skill name or description changed.

### 2. Mirror Skills to Workflows
Generate global workflow files for all skills to expose them as slash commands.

```bash
python3 scripts/mirror_skills.py
```

### 3. Verify
Check `global_workflows/` to see updated workflow files.
