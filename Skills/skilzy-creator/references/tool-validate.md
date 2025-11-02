# Tool Reference: validate_skill.py

## Purpose

Verify that a skill directory conforms to the Skilzy specification by checking both JSON schema compliance and filesystem integrity. Validation ensures skills will work correctly in the Skilzy registry and in AI agent environments.

## Command Syntax

```bash
python scripts/validate_skill.py <path/to/skill-directory>
```

### Arguments

- `<path/to/skill-directory>` - Path to the skill folder to validate (required)
  - Must be a directory containing skill.json
  - Can be absolute or relative path

## Validation Layers

The validator performs **two independent** validation checks:

### Layer 1: JSON Schema Validation

Validates the `skill.json` file against the official Skilzy schema.

**Checks performed:**

1. **Required Fields Present**
   - `name` ✓
   - `version` ✓
   - `description` ✓
   - `author` ✓
   - `license` ✓
   - `entrypoint` ✓

2. **Field Format Validation**

   **name:**
   - Pattern: `^[a-z0-9]+(-[a-z0-9]+)*$`
   - Length: 1-40 characters
   - Valid: `pdf-processor`, `web-scraper`, `data-tool-v2`
   - Invalid: `PDF_Processor`, `web scraper`, `MyTool`

   **version:**
   - Must follow Semantic Versioning (SemVer)
   - Pattern: `MAJOR.MINOR.PATCH` with optional pre-release/build
   - Valid: `1.0.0`, `2.1.3`, `1.0.0-beta.1`, `0.1.0`
   - Invalid: `1.0`, `v1.0.0`, `1.0.0.0`

   **description:**
   - Length: 20-250 characters
   - Must be informative
   - Should include WHEN to use the skill

   **keywords:**
   - Must be lowercase
   - Can contain hyphens
   - Pattern: `^[a-z0-9-]+$`
   - Valid: `["pdf", "data-analysis", "ml"]`
   - Invalid: `["PDF", "Data Analysis", "ML_Tools"]`

   **runtime.type:**
   - Must be "python" (currently only supported runtime)

3. **Data Type Validation**
   - Strings are strings
   - Arrays are arrays
   - Objects are objects
   - Numbers are numbers
   - Booleans are booleans

4. **Nested Object Validation**
   - `runtime` object structure
   - `repository` object structure
   - `dependencies` object structure
   - `permissions` object structure

### Layer 2: Filesystem Validation

Ensures that files declared in the manifest actually exist on the filesystem.

**Checks performed:**

1. **Directory Name Matches `name` Field**
   - Directory: `pdf-processor/`
   - skill.json `name`: `"pdf-processor"` ✓
   - Directory: `pdf_processor/`
   - skill.json `name`: `"pdf-processor"` ❌

2. **Entrypoint File Exists**
   - skill.json: `"entrypoint": "README.md"`
   - File must exist: `README.md` ✓

3. **Icon File Exists** (if specified)
   - skill.json: `"icon": "assets/icon.svg"`
   - File must exist: `assets/icon.svg` ✓

4. **License File Exists** (if specified)
   - skill.json: `"licenseFile": "LICENSE"`
   - File must exist: `LICENSE` ✓

5. **skill.json File is Valid JSON**
   - Must parse without syntax errors
   - Must be well-formed JSON

## Exit Codes and Output

### Exit Code 0 (Success)

**Output:**
```
--- Validation Summary ---
✅ Skill is valid!

✨ All checks passed.
```

**Meaning:**
- Schema validation passed
- Filesystem validation passed
- Skill is ready for packaging

### Exit Code 1 (Failure)

**Output example:**
```
--- Validation Summary ---
Schema validation failed:
  - description: 'Short' is too short
  - name: 'MySkill' does not match '^[a-z0-9]+(-[a-z0-9]+)*$'
  - version: '1.0' does not match SemVer pattern

Filesystem checks failed:
  - File 'assets/icon.svg' declared in 'icon' field does not exist.
  - Directory name 'my_skill' does not match skill name 'my-skill'

❌ Validation failed.
```

**Meaning:**
- One or more validation checks failed
- Errors must be fixed before packaging
- Review each error and make corrections

## Common Validation Errors

### Schema Errors

#### Error: "description is too short"

**Cause:** Description field is under 20 characters

**Example:**
```json
{
  "description": "Processes PDFs"
}
```

**Fix:** Expand to at least 20 characters and include WHEN to use:
```json
{
  "description": "Extracts text and metadata from PDF files. Use when users upload PDFs for analysis."
}
```

#### Error: "name does not match pattern"

**Cause:** Skill name contains uppercase, underscores, or spaces

**Invalid examples:**
- `"MySkill"` (uppercase)
- `"my_skill"` (underscore)
- `"my skill"` (space)

**Fix:** Use lowercase with hyphens:
```json
{
  "name": "my-skill"
}
```

#### Error: "version does not match SemVer pattern"

**Cause:** Version is not in MAJOR.MINOR.PATCH format

**Invalid examples:**
- `"1.0"` (missing PATCH)
- `"v1.0.0"` (has prefix)
- `"1.0.0.0"` (too many parts)

**Fix:** Use proper SemVer:
```json
{
  "version": "1.0.0"
}
```

#### Error: "keywords contain invalid characters"

**Cause:** Keywords have uppercase or spaces

**Invalid:**
```json
{
  "keywords": ["PDF", "Data Analysis"]
}
```

**Fix:** Use lowercase and hyphens:
```json
{
  "keywords": ["pdf", "data-analysis"]
}
```

#### Error: "required field missing"

**Cause:** One of the required fields is not present

**Required fields:**
- `name`
- `version`
- `description`
- `author`
- `license`
- `entrypoint`

**Fix:** Add the missing field to skill.json

### Filesystem Errors

#### Error: "File declared in 'entrypoint' field does not exist"

**Cause:** skill.json references a file that isn't in the directory

**Example:**
- skill.json: `"entrypoint": "README.md"`
- Missing file: `README.md`

**Fix:** Create the missing file or update the field:
```bash
touch README.md
```

#### Error: "File declared in 'icon' field does not exist"

**Cause:** Icon file referenced but not present

**Example:**
- skill.json: `"icon": "assets/logo.png"`
- Missing file: `assets/logo.png`

**Fix:** Add the icon file or remove the field:
```bash
mkdir -p assets
cp my-icon.png assets/logo.png
```

#### Error: "Directory name does not match skill name"

**Cause:** Folder name and skill.json `name` field don't match

**Example:**
- Directory: `pdf_editor/`
- skill.json: `"name": "pdf-editor"`

**Fix:** Rename the directory:
```bash
mv pdf_editor pdf-editor
```

#### Error: "skill.json is not valid JSON"

**Cause:** JSON syntax error

**Common causes:**
- Missing comma
- Trailing comma
- Unquoted keys
- Unclosed brackets

**Fix:** Use a JSON validator to find and fix syntax errors

## Integration with Other Tools

### Automatic Validation Before Packaging

The `package_skill.py` tool **automatically runs validation** before creating an archive:

```bash
python scripts/package_skill.py my-skill/
```

**Behavior:**
1. Runs full validation first
2. If validation fails → Shows errors and exits (no package created)
3. If validation passes → Creates package

**Benefit:** Prevents distributing invalid skills

### Manual Validation During Development

Run validation manually during development to catch errors early:

```bash
# After making changes
python scripts/validate_skill.py my-skill/

# Fix any errors

# Validate again
python scripts/validate_skill.py my-skill/
```

## Validation Workflow

**Recommended workflow:**

1. **Create or edit skill files**
2. **Run validation:**
   ```bash
   python scripts/validate_skill.py my-skill/
   ```
3. **If errors:**
   - Review error messages
   - Load `references/troubleshooting.md` if needed
   - Fix each issue
   - Re-run validation
4. **If success:**
   - Proceed to packaging
   - Or continue development

## Best Practices

1. **Validate frequently** - After each significant change
2. **Fix errors immediately** - Don't accumulate validation debt
3. **Use troubleshooting** - Load troubleshooting.md for error guidance
4. **Automate in CI/CD** - Run validation in automated pipelines
5. **Test before publish** - Always validate before creating packages

## Example Validation Session

```bash
# Initial validation attempt
$ python scripts/validate_skill.py web-scraper/

--- Validation Summary ---
Schema validation failed:
  - description: 'Scrapes web' is too short

❌ Validation failed.

# Fix the description in skill.json
$ nano web-scraper/skill.json
# Update "description" to be more detailed

# Validate again
$ python scripts/validate_skill.py web-scraper/

--- Validation Summary ---
✅ Skill is valid!

✨ All checks passed.

# Ready to package
$ python scripts/package_skill.py web-scraper/ -o dist/
```