# Dify Plugin Troubleshooting Guide

Common errors and their solutions when developing Dify tool plugins.

---

## Error Categories

- [Import Errors](#import-errors)
- [Structure Errors](#structure-errors)
- [Parameter Errors](#parameter-errors)
- [Credential Errors](#credential-errors)
- [Runtime Errors](#runtime-errors)
- [Packaging Errors](#packaging-errors)
- [YAML Errors](#yaml-errors)

---

## Import Errors

### Error: `Multiple subclasses of Tool in /path/to/file.py`

**Cause:** Multiple Tool classes defined in a single Python file

**Solution:**
1. Check the problematic file:
```bash
cat tools/problematic_file.py | grep "class.*Tool"
```

2. Keep ONLY ONE Tool class per file
3. Move other Tool classes to separate files

**Example:**

❌ **Wrong - Multiple classes in one file:**
```python
# tools/search.py
class SearchTool(Tool):  # First class
    pass

class FilterTool(Tool):  # Second class - WRONG!
    pass
```

✅ **Correct - One class per file:**
```python
# tools/search.py
class SearchTool(Tool):
    pass

# tools/filter.py  (separate file)
class FilterTool(Tool):
    pass
```

---

### Error: `ImportError: cannot import name 'function_name' from 'module'`

**Cause:** Import name doesn't match the actual function/class definition

**Solution:**
1. Check function name in the source file:
```bash
grep "def function_name" utils/helpers.py
```

2. Verify exact spelling, including:
   - Underscores vs hyphens
   - Uppercase vs lowercase
   - Plural vs singular

**Example:**

❌ **Wrong:**
```python
# utils/helpers.py
def process_data(data):
    pass

# tools/tool.py
from utils.helpers import processData  # WRONG spelling
```

✅ **Correct:**
```python
# utils/helpers.py
def process_data(data):
    pass

# tools/tool.py
from utils.helpers import process_data  # Correct spelling
```

---

### Error: `ModuleNotFoundError: No module named 'dify_plugin'`

**Cause:** dify_plugin package not installed

**Solution:**
```bash
pip install dify_plugin
# or
pip install -r requirements.txt
```

**Verify installation:**
```bash
pip show dify_plugin
```

---

## Structure Errors

### Error: `Tool class not found in file`

**Cause:** 
- Tool class name doesn't follow pattern
- Class doesn't inherit from Tool
- File naming mismatch

**Solution:**

1. **Verify class inheritance:**
```python
from dify_plugin import Tool  # Import Tool base class

class MyTool(Tool):  # Must inherit from Tool
    pass
```

2. **Check class naming:**
   - Class name should end with `Tool`
   - Use CamelCase: `MyAwesomeTool`

3. **Verify file-to-class correspondence:**
   - `tools/search.py` → class `SearchTool`
   - `tools/weather-api.py` → class `WeatherApiTool`

---

### Error: `Method '_invoke' not found or has wrong signature`

**Cause:** Missing or incorrect `_invoke` method signature

**Solution:**

✅ **Correct signature (MUST match exactly):**
```python
from collections.abc import Generator
from typing import Any
from dify_plugin.entities.tool import ToolInvokeMessage

class MyTool(Tool):
    def _invoke(
        self, 
        tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage]:
        # Implementation
        yield self.create_text_message("result")
```

**Key requirements:**
- Method name: `_invoke` (with underscore)
- Parameter: `tool_parameters: dict[str, Any]`
- Return type: `Generator[ToolInvokeMessage]`
- Use `yield`, not `return`

---

## Parameter Errors

### Error: `KeyError: 'parameter_name'`

**Cause:** Accessing parameter without checking if it exists

**Solution:**

❌ **Wrong - Direct access:**
```python
def _invoke(self, tool_parameters: dict[str, Any]):
    query = tool_parameters["query"]  # Throws KeyError if missing
```

✅ **Correct - Use .get():**
```python
def _invoke(self, tool_parameters: dict[str, Any]):
    query = tool_parameters.get("query", "")  # Returns "" if missing

    # Validate
    if not query:
        yield self.create_text_message("Error: query is required")
        return
```

---

### Error: `Parameter validation failed`

**Cause:** Parameter type or format doesn't match YAML definition

**Solution:**

1. **Check YAML parameter definition:**
```yaml
parameters:
  - name: count
    type: number        # Expects numeric value
    required: true
```

2. **Handle type conversion:**
```python
def _invoke(self, tool_parameters: dict[str, Any]):
    count = tool_parameters.get("count", 1)

    # Convert to int if needed
    try:
        count = int(count)
    except (ValueError, TypeError):
        yield self.create_text_message("Error: count must be a number")
        return
```

---

## Credential Errors

### Error: `ToolProviderCredentialValidationError: Invalid API key`

**Cause:** API key validation failed

**Solution:**

1. **Check API key format:**
```python
api_key = credentials.get("api_key")

if not api_key:
    raise Exception("API key is required")

if not api_key.startswith("sk-"):  # Example format check
    raise Exception("API key must start with 'sk-'")
```

2. **Test API endpoint:**
```python
import requests

response = requests.get(
    "https://api.example.com/validate",
    headers={"Authorization": f"Bearer {api_key}"},
    timeout=10
)

if response.status_code != 200:
    raise Exception(f"Invalid API key: {response.text}")
```

3. **Verify .env file:**
```bash
cat .env
# Make sure API_KEY is set correctly
```

---

### Error: `Credentials not found`

**Cause:** Missing credentials configuration

**Solution:**

1. **Add credentials to provider YAML:**
```yaml
credentials_for_provider:
  api_key:
    type: secret-input
    required: true
    label:
      en_US: "API Key"
```

2. **Implement validation in provider.py:**
```python
def _validate_credentials(self, credentials: dict[str, Any]):
    api_key = credentials.get("api_key")
    if not api_key:
        raise Exception("API key is required")
    return ToolProviderCredentials(credentials=credentials)
```

---

## Runtime Errors

### Error: `RuntimeError: event loop is already running`

**Cause:** Async/await issues in synchronous context

**Solution:**

Use synchronous code only (no async/await in tools):

❌ **Wrong:**
```python
async def _invoke(self, tool_parameters):  # Don't use async
    result = await some_async_function()
```

✅ **Correct:**
```python
def _invoke(self, tool_parameters):  # Synchronous only
    result = some_sync_function()
    yield self.create_text_message(result)
```

---

### Error: `requests.exceptions.Timeout`

**Cause:** API request taking too long

**Solution:**

Always set timeout on requests:

```python
import requests

try:
    response = requests.get(
        "https://api.example.com/data",
        timeout=10  # 10 second timeout
    )
    response.raise_for_status()
except requests.Timeout:
    yield self.create_text_message("Error: Request timed out")
    return
except requests.RequestException as e:
    yield self.create_text_message(f"Error: {str(e)}")
    return
```

---

### Error: `UnboundLocalError: local variable referenced before assignment`

**Cause:** Variable used before being defined

**Solution:**

Initialize variables before use:

❌ **Wrong:**
```python
if condition:
    result = process_a()
# result might not be defined here
yield self.create_text_message(result)  # Error if condition was False
```

✅ **Correct:**
```python
result = None  # Initialize first

if condition:
    result = process_a()
else:
    result = "default"

yield self.create_text_message(result)
```

---

## Packaging Errors

### Error: `Failed to pack plugin`

**Cause:** Missing files or invalid structure

**Solution:**

1. **Verify all required files exist:**
```bash
cd your-plugin
ls manifest.yaml  # Must exist
ls provider/      # Must exist
ls tools/         # Must exist
ls main.py        # Must exist
```

2. **Check manifest.yaml validity:**
```bash
python -c "import yaml; yaml.safe_load(open('manifest.yaml'))"
```

3. **Verify file references:**
   - manifest.yaml → provider/*.yaml path correct
   - provider/*.yaml → tools/*.yaml paths correct
   - tools/*.yaml → tools/*.py paths correct

---

### Error: `YAML syntax error`

**Cause:** Invalid YAML formatting

**Solution:**

1. **Check indentation (must use spaces, not tabs):**
```yaml
identity:        # 0 spaces
  name: tool     # 2 spaces
  label:         # 2 spaces
    en_US: Name  # 4 spaces
```

2. **Validate YAML:**
```bash
pip install yamllint
yamllint manifest.yaml
```

3. **Common YAML mistakes:**
   - ❌ Using tabs instead of spaces
   - ❌ Missing colon after key
   - ❌ Incorrect indentation
   - ❌ Missing quotes around special characters

---

## YAML Errors

### Error: `mapping values are not allowed in this context`

**Cause:** YAML syntax error, usually missing space after colon

**Solution:**

❌ **Wrong:**
```yaml
name:tool-name  # Missing space after colon
```

✅ **Correct:**
```yaml
name: tool-name  # Space after colon
```

---

### Error: `did not find expected key`

**Cause:** Indentation error in YAML

**Solution:**

❌ **Wrong indentation:**
```yaml
identity:
  name: tool
label:            # Wrong indent level
  en_US: Tool
```

✅ **Correct indentation:**
```yaml
identity:
  name: tool
  label:          # Correct indent (part of identity)
    en_US: Tool
```

---

## Debug Workflow

When encountering any error:

### Step 1: Read Error Message
```bash
python -m main 2>&1 | tee error.log
```

Look for:
- File name where error occurred
- Line number
- Error type (ImportError, KeyError, etc.)

### Step 2: Check File Structure
```bash
ls -la
tree  # or ls -R
```

Verify all required files present.

### Step 3: Validate YAML Files
```bash
python -c "import yaml; yaml.safe_load(open('manifest.yaml'))"
python -c "import yaml; yaml.safe_load(open('provider/plugin.yaml'))"
python -c "import yaml; yaml.safe_load(open('tools/tool.yaml'))"
```

### Step 4: Check Python Syntax
```bash
python -m py_compile tools/*.py
python -m py_compile provider/*.py
```

### Step 5: Verify Imports
```bash
python -c "from dify_plugin import Tool; print('OK')"
python -c "from tools.your_tool import YourTool; print('OK')"
```

### Step 6: Add Debug Logging
```python
import logging
logger = logging.getLogger(__name__)

def _invoke(self, tool_parameters):
    logger.info(f"Parameters: {tool_parameters}")
    logger.debug("Step 1 complete")
    # ... more logging
```

### Step 7: Test in Isolation
```bash
python
>>> from tools.your_tool import YourTool
>>> tool = YourTool()
>>> # Test methods individually
```

---

## Prevention Checklist

Before packaging, verify:

- [ ] One Tool class per .py file
- [ ] All imports spelled correctly
- [ ] Using `.get()` for all parameters
- [ ] `_invoke` method signature exact
- [ ] All YAML files valid (no tabs)
- [ ] All file paths in YAMLs correct
- [ ] Error handling included
- [ ] Logging added
- [ ] Requirements.txt complete
- [ ] manifest.yaml fully filled
- [ ] Tested locally with `python -m main`

---

## Getting Help

If stuck:

1. **Re-read official documentation:**
```bash
curl -s https://docs.dify.ai/plugin-dev-en/0222-tool-plugin.md
```

2. **Check reference files:**
   - `references/doc-map.md`
   - `references/workflow.md`
   - `references/examples.md`

3. **Review working examples:**
   - Look at successfully packaged plugins
   - Compare structure and patterns

4. **Start fresh if needed:**
   - Re-initialize plugin
   - Copy working code piece by piece
   - Test after each addition

---

## Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| Import error | Check spelling, use exact names |
| Multiple Tool classes | One class per file, move extras |
| KeyError | Use `.get()` instead of direct access |
| YAML error | Check indentation (spaces not tabs) |
| Package fail | Verify all files exist, check paths |
| Timeout | Add `timeout=10` to requests |
| Credential fail | Test API key manually first |
