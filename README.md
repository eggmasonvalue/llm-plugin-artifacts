# Antigravity Skills & Workflows

This repository tracks the custom skills and workflows for Antigravity.

## Note:
While progressive disclosure is great as a strategy, agent skills aren't being reliably used by LLMs, not just due to poor YAML frontmatter.

To ensure that these skils can be explicitly invoked without remembering their names, a skill has been added to create a workflow for each skill. Now, antigravity enables you to invoke the workflow with a slash command which inturn invokes the skill.


## Setup
The files are physically located in this repository and symlinked to the Antigravity system folder:
`c:\Users\<username>\.gemini\antigravity\`

- `global_workflows` -> `<repository root>\global_workflows`
- `skills` -> `<repository root>\skills`
