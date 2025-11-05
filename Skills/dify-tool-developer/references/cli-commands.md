# Dify CLI Commands Reference

Quick reference for all Dify plugin CLI commands.

---

## Installation & Verification

### Check CLI Version
```bash
dify version
```

**Output:**
```
v0.4.0
```



---

## CLI Installation Helper

### Automated Installation

Use the provided Python script to automatically install Dify CLI:

```bash
python scripts/install_cli.py
```

**Features:**
- Auto-detects your OS (macOS, Linux, Windows)
- Auto-detects architecture (AMD64, ARM64)
- Fetches latest version from GitHub API
- Downloads appropriate binary
- Makes executable automatically
- Verifies installation

**Options:**

```bash
# Install latest version to current directory
python scripts/install_cli.py

# Install specific version
python scripts/install_cli.py --version 0.4.0

# Install to custom directory
python scripts/install_cli.py --path ~/bin

# Combine options
python scripts/install_cli.py --version 0.4.0 --path /usr/local/bin
```

**What it does:**
1. Detects platform (e.g., darwin-arm64, linux-amd64)
2. Queries GitHub API for latest release (or uses specified version)
3. Downloads from: `https://github.com/langgenius/dify-plugin-daemon/releases/download/{version}/dify-plugin-{os}-{arch}`
4. Saves as `dify` (or `dify.exe` on Windows)
5. Makes executable (chmod +x on Unix)
6. Runs `dify version` to verify
7. Prints PATH setup instructions

**Supported Platforms:**
- macOS: darwin-amd64, darwin-arm64
- Linux: linux-amd64, linux-arm64
- Windows: windows-amd64, windows-arm64


### Check CLI Help
```bash
dify --help
```

---

## Plugin Initialization

### Basic Initialization (Interactive)
```bash
dify plugin init
```

Prompts for all options interactively.

### Non-Interactive Initialization
```bash
dify plugin init \
  --name "plugin-name" \
  --author "author-name" \
  --description "Plugin description" \
  --category tool \
  --language python \
  --min-dify-version "0.6.0" \
  --quick
```

### Required Flags

| Flag | Description | Example |
|------|-------------|---------|
| `--name` | Plugin name (lowercase, hyphens only) | `--name "weather-tool"` |
| `--author` | Author name | `--author "your-author-name"` |
| `--description` | Brief description | `--description "Fetch weather data"` |
| `--category` | Plugin category (tool/llm/etc) | `--category tool` |
| `--language` | Programming language | `--language python` |

### Optional Flags

| Flag | Description | Default |
|------|-------------|---------|
| `--min-dify-version` | Minimum Dify version | `"0.6.0"` |
| `--quick` | Skip interactive prompts | Interactive mode |
| `--repo` | Repository URL | None |

### Permission Flags

| Flag | Description | Use When |
|------|-------------|----------|
| `--allow-network` | Enable external API calls | Calling APIs, webhooks |
| `--allow-storage` | Enable persistent storage | Storing data, cache |
| `--allow-tool` | Allow invoking other tools | Chaining tools |
| `--allow-llm` | Allow invoking LLM models | Need AI completion |
| `--allow-model` | Allow invoking models | Using AI models |
| `--allow-moderation` | Allow content moderation | Content filtering |
| `--allow-rerank` | Allow reranking models | Search reranking |
| `--allow-speech2text` | Allow speech-to-text | Audio transcription |
| `--allow-text-embedding` | Allow text embeddings | Semantic search |
| `--allow-tts` | Allow text-to-speech | Voice generation |
| `--allow-app` | Allow app invocation | Cross-app features |
| `--allow-endpoint` | Allow endpoint registration | Custom endpoints |
| `--allow-node` | Allow node invocation | Workflow nodes |

### Storage Size

```bash
--storage-size <bytes>
```

**Examples:**
- 1 MB: `--storage-size 1048576`
- 10 MB: `--storage-size 10485760`
- 100 MB: `--storage-size 104857600`

---

## Common Initialization Patterns

### Simple API Tool
```bash
dify plugin init \
  --name "api-tool" \
  --author "your-author-name" \
  --description "Call external API" \
  --category tool \
  --language python \
  --allow-network \
  --quick
```

### Tool with Storage
```bash
dify plugin init \
  --name "cache-tool" \
  --author "your-author-name" \
  --description "Cache API responses" \
  --category tool \
  --language python \
  --allow-network \
  --allow-storage \
  --storage-size 10485760 \
  --quick
```

### OAuth Tool
```bash
dify plugin init \
  --name "github-tool" \
  --author "your-author-name" \
  --description "GitHub integration via OAuth" \
  --category tool \
  --language python \
  --allow-network \
  --quick
```

After initialization, implement OAuth as described in tool-oauth.md

---

## Testing & Debugging

### Run Plugin Locally
```bash
cd your-plugin-directory
python -m main
```

### Run with Environment Variables
```bash
cd your-plugin-directory
# Edit .env file first
python -m main
```

### Python Version Check
```bash
python --version
# Should be 3.12 or higher
```

### Install Dependencies
```bash
cd your-plugin-directory
pip install -r requirements.txt
```

---

## Packaging

### Basic Packaging
```bash
dify plugin package ./your-plugin-directory
```

**Output:** Creates `your-plugin-name.difypkg` in current directory

### Packaging with Custom Output Path
```bash
dify plugin package ./your-plugin-directory --output_path dist/plugin.difypkg
```

### Packaging with Output Directory
```bash
dify plugin package ./your-plugin-directory --output_path dist/
```

**Output:** Creates `dist/your-plugin-name.difypkg`

### Verify Package
```bash
ls -lh *.difypkg
# Check file size and timestamp
```

---

## File Operations

### List Plugin Files
```bash
cd your-plugin-directory
ls -la
```

### Check File Structure
```bash
cd your-plugin-directory
tree
# Or use ls -R
```

### Validate YAML Files
```bash
# Install yamllint
pip install yamllint

# Validate YAML
yamllint manifest.yaml
yamllint provider/*.yaml
yamllint tools/*.yaml
```

### Check Python Syntax
```bash
python -m py_compile tools/*.py
python -m py_compile provider/*.py
```

---

## Debugging Commands

### View Plugin Logs
```bash
cd your-plugin-directory
python -m main 2>&1 | tee plugin.log
```

### Test Python Imports
```bash
python -c "from dify_plugin import Tool; print('OK')"
```

### Check Installed Packages
```bash
pip list | grep dify
pip show dify_plugin
```

### Validate JSON
```bash
python -m json.tool < skill.json
```

---

## Git Commands (Version Control)

### Initialize Git
```bash
cd your-plugin-directory
git init
git add .
git commit -m "Initial commit"
```

### Create Version Tag
```bash
git tag v0.0.1
git tag -l  # List tags
```

### Gitignore Template
```bash
cat > .gitignore << EOF
__pycache__/
*.py[cod]
*$py.class
.env
*.egg-info/
dist/
build/
*.difypkg
.DS_Store
EOF
```

---

## Environment Setup

### Create Virtual Environment
```bash
cd your-plugin-directory
python -m venv venv
```

### Activate Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\Scripts\activate
```

### Install in Virtual Environment
```bash
pip install -r requirements.txt
```

### Deactivate Virtual Environment
```bash
deactivate
```

---

## Troubleshooting Commands

### Reset Plugin (Clean Build)
```bash
cd your-plugin-directory
rm -rf __pycache__
rm -rf *.egg-info
find . -name "*.pyc" -delete
```

### Reinstall Dependencies
```bash
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
```

### Check Python Path
```bash
python -c "import sys; print('\n'.join(sys.path))"
```

### Verify Dify Plugin Module
```bash
python -c "import dify_plugin; print(dify_plugin.__version__)"
```

---

## Quick Commands Cheat Sheet

| Task | Command |
|------|---------|
| Check version | `dify version` |
| Init plugin | `dify plugin init --quick` |
| Run locally | `python -m main` |
| Package | `dify plugin package ./plugin` |
| List files | `ls -la` |
| Check Python | `python --version` |
| Install deps | `pip install -r requirements.txt` |
| View logs | `python -m main 2>&1 \| tee log.txt` |

---

## Useful Bash Aliases

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
# Dify plugin shortcuts
alias dify-init='dify plugin init --quick'
alias dify-pack='dify plugin package .'
alias dify-run='python -m main'
alias dify-ver='dify version'
```

Reload shell:
```bash
source ~/.bashrc
# or
source ~/.zshrc
```

---

## Documentation Fetch Commands

### Fetch Official Docs

```bash
# Initialize tools
curl -s https://docs.dify.ai/plugin-dev-en/0221-initialize-development-tools.md

# Tool plugin guide
curl -s https://docs.dify.ai/plugin-dev-en/0222-tool-plugin.md

# Debugging logs
curl -s https://docs.dify.ai/plugin-dev-en/0222-debugging-logs.md

# OAuth guide
curl -s https://docs.dify.ai/plugin-dev-en/0222-tool-oauth.md
```

### Save Docs Locally

```bash
mkdir -p docs
curl -s https://docs.dify.ai/plugin-dev-en/0222-tool-plugin.md > docs/tool-plugin.md
```

### Use Helper Script

```bash
bash scripts/fetch_doc.sh tool    # Fetch tool-plugin.md
bash scripts/fetch_doc.sh oauth   # Fetch tool-oauth.md
bash scripts/fetch_doc.sh debug   # Fetch debugging-logs.md
bash scripts/fetch_doc.sh init    # Fetch initialize-development-tools.md
```

---

## Complete Workflow Example

```bash
# 1. Verify CLI
dify version

# 2. Initialize plugin
dify plugin init \
  --name "my-tool" \
  --author "your-name" \
  --description "My custom tool" \
  --category tool \
  --language python \
  --allow-network \
  --quick

# 3. Navigate to plugin
cd my-tool

# 4. Set up environment
cp .env.example .env
# Edit .env as needed

# 5. Install dependencies
pip install -r requirements.txt

# 6. Implement tool (edit files)
# ... edit tools/my-tool.yaml
# ... edit tools/my-tool.py
# ... edit manifest.yaml

# 7. Test locally
python -m main

# 8. Package
cd ..
dify plugin package ./my-tool

# 9. Verify
ls -lh my-tool.difypkg
```

---

## References

- Official Dify Docs: https://docs.dify.ai/plugin-dev-en/
- Dify GitHub: https://github.com/langgenius/dify
- Plugin Daemon: https://github.com/langgenius/dify-plugin-daemon
