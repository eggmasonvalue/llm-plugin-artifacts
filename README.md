# Antigravity Skills & Workflows

This repository tracks custom skills for Antigravity.

## Note:
Workflows are no longer needed since skills are finally invokable on demand in antigravity. 

FREEDOM.

## Setup
The files are physically located in this repository and symlinked to the Antigravity system folder:
`c:\Users\<username>\.gemini\antigravity\`

- `global_workflows` -> `<repository root>\global_workflows`
- `skills` -> `<repository root>\skills`

### Terminal app on android - setup
Download the [.sh](.\`setup_terminal_android.sh`)

Run the following in your terminal app:
```bash
sudo apt install -y dos2unix
dos2unix ../../mnt/shared/Download/setup_terminal_android.sh
bash ../../mnt/shared/Download/setup_terminal_android.sh
```
