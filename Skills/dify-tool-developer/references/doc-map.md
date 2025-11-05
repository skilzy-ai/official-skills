# Official Dify Documentation Map

This reference maps each official Dify documentation file, describing what information it contains and when the AI agent must load it during development.

---

## 📄 Initialize Development Tools

**URL:** `https://docs.dify.ai/plugin-dev-en/0221-initialize-development-tools.md`

**File Size:** ~3,500 characters

**CONTAINS:**
- Installing the Dify plugin CLI tool
- Supported operating systems and architectures
- Download links for different platforms
- Python environment setup requirements
- Verification commands
- Basic development workflow overview

**LOAD WHEN:**
- Phase 1: User doesn't have Dify CLI installed
- User reports CLI installation issues
- Need to verify Dify CLI version compatibility

**KEY SECTIONS:**
1. Installing the Dify Plugin Development Scaffolding Tool
   - Platform-specific download instructions
   - Installation locations and PATH setup
2. Initialize Python Environment
   - Python version requirements (3.12+)
   - Virtual environment setup
3. Develop plugins
   - Basic workflow overview

**CRITICAL COMMANDS:**
```bash
# Download for macOS (ARM64)
wget https://github.com/langgenius/dify-plugin-daemon/releases/download/0.4.0/dify-plugin-darwin-arm64

# Verify installation
./dify-plugin version
```

---

## 📄 Tool Plugin

**URL:** `https://docs.dify.ai/plugin-dev-en/0222-tool-plugin.md`

**File Size:** ~18,000 characters

**⚠️ MOST CRITICAL DOCUMENT - Contains all implementation details**

**CONTAINS:**
- Complete step-by-step tool plugin development process
- Exact project structure and file organization
- Tool implementation patterns and code examples
- YAML configuration syntax with all required fields
- Python Tool class structure with strict requirements
- Parameter handling conventions
- Message types and output formats
- Debugging techniques
- Packaging commands and options
- Publishing guidelines

**LOAD WHEN:**
- Phase 2: BEFORE running `dify plugin init` (MANDATORY)
- Phase 3: BEFORE writing any tool code (MANDATORY)
- When implementing tool YAML files
- When implementing tool Python classes
- When configuring manifest.yaml
- When troubleshooting structure issues

**KEY SECTIONS:**

### 1. Prerequisites
- Python 3.12+ requirement
- Dify CLI installation verification
- Development environment setup

### 2. Creating a New Project  
- `dify plugin init` command syntax
- Available flags and options
- Interactive vs non-interactive mode

### 3. Choosing Plugin Type and Template
- Tool plugin type selection
- Template options

### 4. Developing the Tool Plugin
**This is the MOST CRITICAL section** - contains:

#### File Structure:
```
your-plugin/
├── manifest.yaml           # Plugin manifest
├── provider/
│   ├── plugin.yaml        # Provider config
│   └── plugin.py          # Credential validation
├── tools/
│   ├── tool-name.yaml     # Tool config
│   └── tool-name.py       # Tool implementation
├── main.py                # Entry point
├── requirements.txt       # Dependencies
└── .env.example           # Environment template
```

#### manifest.yaml Format:
- All required fields and their types
- Internationalization structure (en_US, zh_Hans, pt_BR, ja_JP)
- Resource and permission configurations
- Plugin metadata

#### provider/*.yaml Format:
- Identity fields
- Credentials schema (if needed)
- Tools list
- Python source reference

#### tools/*.yaml Format:
- Identity section
- Description for humans vs AI
- Parameters array with:
  - name, type, required, label, descriptions
  - form type (llm vs form)
- Extra python source reference

#### tools/*.py Format:
- Exact import statements required
- Tool class structure
- `_invoke` method signature (MUST be exact)
- Parameter extraction patterns
- Message creation methods
- Error handling patterns

**CRITICAL CODE PATTERNS:**

```python
from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class ToolName(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # Extract parameters
        param = tool_parameters.get("param_name", "default")

        # Validate
        if not param:
            yield self.create_text_message("Error message")
            return

        # Process
        result = process(param)

        # Return messages
        yield self.create_text_message(result)
        yield self.create_json_message({"key": result})
```

### 5. Debugging the Plugin
- Local testing setup
- Running the plugin locally
- Interpreting error messages

### 6. Packaging the Plugin
- `dify plugin package` command
- Output file format (.difypkg)
- Package verification

### 7. Publishing the Plugin (Optional)
- Marketplace submission process
- Requirements for publishing

**STRICT RULES DOCUMENTED:**
- ⚠️ ONE Tool class per .py file (multiple will cause errors)
- ⚠️ Exact method signature for `_invoke` required
- ⚠️ Must use `.get()` for optional parameters
- ⚠️ Must return with `yield`, not `return`
- ⚠️ Specific import patterns required
- ⚠️ Exact YAML structure and indentation

---

## 📄 Debugging Logs

**URL:** `https://docs.dify.ai/plugin-dev-en/0222-debugging-logs.md`

**File Size:** ~1,700 characters

**CONTAINS:**
- How to add logging to plugin tools
- Required imports for logging
- DifyPluginLogHandler setup
- Viewing logs during development
- Log levels (debug, info, warning, error)

**LOAD WHEN:**
- Phase 4: During testing and debugging
- When troubleshooting runtime errors
- When adding debug output to tools

**KEY SECTIONS:**

### 1. Import logging and custom handler

**Required Imports:**
```python
import logging
from dify_plugin.handlers import DifyPluginLogHandler
```

### 2. Set up logging with the custom handler

**Setup Pattern:**
```python
logger = logging.getLogger(__name__)
logger.addHandler(DifyPluginLogHandler())

class YourTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        logger.info(f"Tool invoked with: {tool_parameters}")
        logger.debug(f"Processing...")

        # Your code

        logger.info(f"Completed successfully")
```

**Log Levels:**
- `logger.debug()` - Detailed diagnostic info
- `logger.info()` - General informational messages  
- `logger.warning()` - Warning messages
- `logger.error()` - Error messages

**Benefits:**
- Track tool execution flow
- Debug parameter issues
- Monitor API calls
- Identify performance bottlenecks

---

## 📄 Tool OAuth

**URL:** `https://docs.dify.ai/plugin-dev-en/0222-tool-oauth.md`

**File Size:** ~22,000 characters

**CONTAINS:**
- Complete OAuth 2.0 implementation guide
- OAuth flow explanations (client setup + user authorization)
- OAuth schema definition in provider YAML
- Required OAuth methods in provider Python
- Token access patterns in tools
- Version requirements for OAuth support
- Real-world examples

**LOAD WHEN:**
- Phase 2: IF user needs OAuth during planning (determine scope)
- Phase 3: BEFORE implementing OAuth (MANDATORY if OAuth needed)
- When integrating with GitHub, Google, Slack, or other OAuth providers
- When troubleshooting OAuth flow issues

**KEY SECTIONS:**

### 1. Background
Two OAuth flows explained:
- **Flow 1:** OAuth Client Setup (Admin/Developer Flow)
  - Developer registers app with provider
  - Obtains client_id and client_secret
  - Configures in Dify plugin settings
- **Flow 2:** User Authorization (Dify User Flow)
  - User grants permissions via OAuth
  - App receives access token
  - Token used for API calls

### 2. Implementation

#### Step 1: Define OAuth Schema in Provider Manifest

**In provider/*.yaml:**
```yaml
oauth_schema:
  client:
    - name: client_id
      type: string
      required: true
      label:
        en_US: Client ID
        zh_Hans: 客户端 ID
    - name: client_secret
      type: secret-input
      required: true
      label:
        en_US: Client Secret
        zh_Hans: 客户端密钥
  authorization:
    url: https://github.com/login/oauth/authorize
    scopes:
      - user
      - repo
  token:
    url: https://github.com/login/oauth/access_token
    headers:
      Accept: application/json
```

**OAuth Schema Fields:**
- `client` - Client credentials (id + secret)
- `authorization` - Auth endpoint + scopes
- `token` - Token exchange endpoint + headers
- Optional: `refresh_token_url`, `token_placement`

#### Step 2: Complete Required OAuth Methods

**In provider/*.py:**

```python
from typing import Any
from dify_plugin.entities.tool import ToolProviderCredentials

class ProviderName:
    def validate_provider_credentials(
        self, credentials: dict[str, Any]
    ) -> ToolProviderCredentials:
        """
        Validate OAuth credentials and return validated credentials

        This method is called after OAuth flow completes
        """
        try:
            # Validate access token by making test API call
            access_token = credentials.get("access_token")

            if not access_token:
                raise Exception("Access token is missing")

            # Test the token with provider API
            # import requests
            # response = requests.get(
            #     "https://api.provider.com/user",
            #     headers={"Authorization": f"Bearer {access_token}"}
            # )
            # if response.status_code != 200:
            #     raise Exception("Invalid access token")

            return ToolProviderCredentials(credentials=credentials)

        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
```

**Required Methods:**
- `validate_provider_credentials()` - Validate OAuth tokens

**Optional Methods:**
- Custom authorization URL generation
- Custom token refresh logic

#### Step 3: Access Tokens in Your Tools

**In tools/*.py:**

```python
def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
    # Access OAuth token from runtime credentials
    access_token = self.runtime.credentials.get("access_token")

    # Use token in API requests
    import requests
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }

    response = requests.get(
        "https://api.provider.com/endpoint",
        headers=headers
    )

    # Process response
    result = response.json()
    yield self.create_json_message(result)
```

**Available Credentials:**
- `access_token` - OAuth access token
- `refresh_token` - OAuth refresh token (if provided)
- `token_type` - Usually "Bearer"
- `expires_in` - Token expiration time
- `scope` - Granted scopes

#### Step 4: Specify the Correct Versions

**In requirements.txt:**
```
dify_plugin>=0.4.2,<0.5.0
```

OAuth support requires `dify_plugin` version 0.4.2 or higher.

**Common OAuth Providers:**
- GitHub: `https://github.com/login/oauth/authorize`
- Google: `https://accounts.google.com/o/oauth2/v2/auth`
- Slack: `https://slack.com/oauth/v2/authorize`
- Microsoft: `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize`

---



---

## Helper Script for Installation

The skill includes an automated CLI installer: `scripts/install_cli.py`

**Usage:**
```bash
python scripts/install_cli.py
```

This automates the process described in the official "Initialize Development Tools" documentation by:
- Detecting your platform automatically
- Downloading the correct binary
- Making it executable
- Verifying installation

Use this as an alternative to manually following the official installation doc, or when the agent needs to set up the CLI programmatically.


## Summary Table

| Document | Size | When to Load | Critical For |
|----------|------|--------------|--------------|
| initialize-development-tools.md | 3.5KB | Phase 1 (if CLI missing) | CLI installation |
| tool-plugin.md | 18KB | Phase 2 & 3 (MANDATORY) | Everything: structure, YAML, Python, packaging |
| debugging-logs.md | 1.7KB | Phase 4 (testing) | Adding logging, debugging |
| tool-oauth.md | 22KB | Phase 3 (if OAuth needed) | OAuth implementation |

---

## Loading Priority

**Always Load First:**
1. `tool-plugin.md` before Phase 2 and Phase 3

**Load If Needed:**
2. `initialize-development-tools.md` if CLI not installed
3. `debugging-logs.md` during testing
4. `tool-oauth.md` if OAuth authentication required

**Re-Load When:**
- Encountering structure questions → `tool-plugin.md`
- Debugging issues → `debugging-logs.md`
- OAuth errors → `tool-oauth.md`

---

## Quick Fetch Commands

```bash
# Initialize/Setup
curl -s https://docs.dify.ai/plugin-dev-en/0221-initialize-development-tools.md

# Tool Plugin (MAIN REFERENCE)
curl -s https://docs.dify.ai/plugin-dev-en/0222-tool-plugin.md

# Debugging
curl -s https://docs.dify.ai/plugin-dev-en/0222-debugging-logs.md

# OAuth
curl -s https://docs.dify.ai/plugin-dev-en/0222-tool-oauth.md
```

Use the helper script: `bash scripts/fetch_doc.sh [tool|oauth|debug|init]`
