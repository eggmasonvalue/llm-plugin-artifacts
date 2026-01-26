---
name: antigravity-skill-mirroring
description: Mirror all skills as global workflows to expose them via slash commands. Use this skill when you add a new skill and want it to be accessible as a workflow.
---

# Antigravity Skill Mirroring

This skill creates a global workflow file for each skill found in the skills directory. This serves as a workaround to expose skills in real-time in Antigravity via slash commands.

## Steps

### 1. Run Mirroring Script
Execute the script to scan skills and generate workflow files.

```bash
python3 scripts/mirror_skills.py
```

### 2. Verify
Check the `global_workflows/` directory to ensure new workflows have been created.
