#!/bin/bash
sudo apt update && sudo apt upgrade
sudo apt install -y dos2unix wget
dos2unix ../../mnt/shared/Download/setup_terminal_android.sh
bash ../../mnt/shared/Download/setup_terminal_android.sh
set -e

# ── apt deps ──────────────────────────────────────────────────────────────────
sudo apt install -y git curl unzip wget

# ── gh cli (official repo) ────────────────────────────────────────────────────
sudo mkdir -p -m 755 /etc/apt/keyrings
out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
  && cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
  | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install -y gh

# ── python + uv ───────────────────────────────────────────────────────────────
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# ── java ──────────────────────────────────────────────────────────────────────
sudo apt install -y default-jdk

# ── node + npm (via nvm) ──────────────────────────────────────────────────────
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
export NVM_DIR="$HOME/.nvm"
source "$NVM_DIR/nvm.sh"
nvm install --lts

# ── codex + gemini CLIs ───────────────────────────────────────────────────────
npm install -g @openai/codex
npm install -g @google/gemini-cli

# ── shared folder ─────────────────────────────────────────────────────────────
mkdir -p /mnt/shared/Download/demigod-dumps

# ── AGENTS.md ─────────────────────────────────────────────────────────────────
mkdir -p ~/.codex
cat > ~/.codex/AGENTS.md << 'EOF'
# Agent Environment

You are running inside a Debian Linux VM on a Google Pixel 10 (Android 16),
managed by Android Virtualization Framework (AVF). This is NOT a standard
Linux machine — you are sandboxed inside Android.

## Environment facts
- Architecture: aarch64 (arm64)
- A Wayland display is available but NOT active by default
- Internet access is available via the Android host's connection
- You cannot interact with Android or other apps on the device directly

## Launching GUI applications
The display must be activated by the user manually first — they must tap the
display icon in the top-right corner of the Terminal app. This is a human
action you cannot trigger yourself.

Once the display is active, the Wayland compositor is Weston, which comes
preinstalled. To run a GUI app:
1. Set the Wayland socket: `export WAYLAND_DISPLAY=wayland-0`
2. Launch your app normally, e.g. `gedit`, `xfce4-terminal`, etc.

If you need to start Weston yourself (display activity already open):
```bash
weston &
```
Do NOT attempt to launch GUI apps without confirming the display activity is
open — they will fail silently or error.

## File sharing with the outside world
The ONLY way to share files with the user's Android device is via:
- **Drop zone:** `/mnt/shared/Download/demigod-dumps/`
- This maps directly to the Download folder on Android internal storage
- Files placed here are immediately visible in Android's Files app
- You CANNOT reach any other Android storage path outside `/mnt/shared/`
- Do NOT create files elsewhere expecting the user to find them

## Clipboard
When the user needs to copy text (a command, URL, code snippet, or any text):
- Write ONLY the raw content to `/mnt/shared/Download/demigod-dumps/clipboard.md`
- Overwrite completely each time — never append
- No preamble, no explanation, no wrapping — just the raw content to be copied
- The user will open this file and copy from it manually

## User's files
- Repos: `~/dev/`
- Drop zone: `/mnt/shared/Download/demigod-dumps/`

## Rules
- Always drop files the user needs into the drop zone
- Never assume the user can scroll back or copy from the terminal
- When in doubt whether something belongs in clipboard.md — it does
EOF

ln -sf ~/.codex/AGENTS.md ~/.gemini/GEMINI.md

echo ""
echo "✓ Done! Now run: source ~/.bashrc"
echo "Then authenticate: gh auth login && codex && gemini"