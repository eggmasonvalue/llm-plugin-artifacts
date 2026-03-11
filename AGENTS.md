## Context artifacts Enforcement
**Explicit Step**: You MUST set `TaskStatus` to "Updating .context artifacts" before finishing any coding task.
**Verify**: Do not call `notify_user` until you have confirmed that all the files in .context folder stay true to the codebase.
**CRITICAL**:
DO NOT USE THE .CONTEXT LOCATION FOR GOOGLE ANTIGRAVITY IDE'S FIRST PARTY ARTIFACTS.

# Browser subagent Watchdog Protocol
## Objective
Prevent infinite loops and resource waste in `browser_subagent` interactions. When invoking any browser subagent instance, establish a watchdog-like protocol tailored to the task in the prompt to the subagent. 

The protocol should contain the following at the minimum: 
1. a temporary .md file the subagent should write to as a **minimal** "status update" after each step
2. you shall poll the .md file and terminate the subagent if the status update seems to indicate that the subagent is deviating from the task at hand.