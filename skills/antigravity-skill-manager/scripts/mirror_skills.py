import os
import re
from pathlib import Path

def parse_frontmatter(content):
    """Simple regex-based frontmatter parser that handles multi-line descriptions."""
    match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    frontmatter = match.group(1)
    data = {}
    
    # Very basic YAML parsing for top-level keys
    # Handle multi-line strings (>- or |) by continually reading lines until next key
    lines = frontmatter.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            
            # Handle multi-line string indicators
            if value in (">", ">-", "|", "|-"):
                multiline_value = []
                i += 1
                while i < len(lines):
                    next_line = lines[i]
                    # Check if line is indented (part of value) or empty
                    if not next_line.strip() or next_line.startswith("  "):
                        multiline_value.append(next_line.strip())
                        i += 1
                    else:
                        # Found start of next key, backtrack
                        i -= 1
                        break
                data[key] = " ".join(multiline_value)
            else:
                data[key] = value
        i += 1
            
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
