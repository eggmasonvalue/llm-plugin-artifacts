import os
import re
from pathlib import Path

def parse_frontmatter(content):
    """Simple regex-based frontmatter parser."""
    match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    frontmatter = match.group(1)
    data = {}
    for line in frontmatter.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data

def mirror_skills():
    # Determine paths relative to this script
    script_dir = Path(__file__).resolve().parent
    # Script is in skills/antigravity-skill-mirroring/scripts/
    # We want to go up to skills/
    skills_dir = script_dir.parent.parent
    # And then up to root/global_workflows
    repo_root = skills_dir.parent
    workflows_dir = repo_root / "global_workflows"

    print(f"Scanning skills in: {skills_dir}")
    print(f"Target workflows dir: {workflows_dir}")
    
    workflows_dir.mkdir(parents=True, exist_ok=True)
    
    count = 0
    for skill_dir in skills_dir.iterdir():
        if skill_dir.is_dir():
            skill_file = skill_dir / "SKILL.md"
            if skill_file.exists():
                # print(f"Processing {skill_dir.name}...")
                content = skill_file.read_text(encoding="utf-8")
                metadata = parse_frontmatter(content)
                
                name = metadata.get("name", skill_dir.name)
                # Fallback description if not found
                description = metadata.get("description", f"Use the {name} skill.")
                
                # Create the workflow content
                workflow_content = f"""---
description: {description}
---

# /{name}

Instruction: Use the '{name}' skill to complete this task.
"""
                target_file = workflows_dir / f"{name}.md"
                target_file.write_text(workflow_content, encoding="utf-8")
                # print(f"Created/Updated {target_file.name}")
                count += 1
                
    print(f"Successfully mirrored {count} skills to global_workflows.")

if __name__ == "__main__":
    mirror_skills()
