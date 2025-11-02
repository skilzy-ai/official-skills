# skill.json Schema Reference

## Complete Schema

The skill.json file must conform to this JSON Schema specification:

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Skilzy Skill Manifest",
    "description": "Schema for the skilzy.ai skill.json manifest file. This file describes the metadata, dependencies, and permissions for a Skilzy AI skill.",
    "type": "object",
    "properties": {
        "name": {
            "description": "Unique, hyphen-case name of the skill. Must match the parent directory name.",
            "type": "string",
            "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$",
            "maxLength": 40
        },
        "version": {
            "description": "The version of the skill, strictly following Semantic Versioning (SemVer).",
            "type": "string",
            "pattern": "^(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?$"
        },
        "description": {
            "description": "A brief, clear summary of what the skill does and when an agent should use it.",
            "type": "string",
            "minLength": 20,
            "maxLength": 250
        },
        "author": {
            "description": "The name of the individual or organization that created the skill.",
            "type": "string"
        },
        "license": {
            "description": "An OSI-approved SPDX license identifier (e.g., 'MIT', 'Apache-2.0').",
            "type": "string"
        },
        "licenseFile": {
            "description": "Relative path to the file containing the full license text (e.g., 'LICENSE').",
            "type": "string"
        },
        "repository": {
            "description": "The source code repository for the skill.",
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "enum": [
                        "git"
                    ]
                },
                "url": {
                    "type": "string",
                    "format": "uri"
                }
            },
            "required": [
                "type",
                "url"
            ]
        },
        "icon": {
            "description": "Relative path to the skill's icon file, for display in the Skilzy web UI.",
            "type": "string"
        },
        "entrypoint": {
            "description": "The main instructional markdown file for display on the registry.",
            "type": "string",
            "default": "README.md"
        },
        "runtime": {
            "description": "The execution environment required by the skill.",
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "enum": [
                        "python"
                    ]
                },
                "version": {
                    "description": "The required version constraint for the runtime (e.g., '>=3.9').",
                    "type": "string"
                }
            },
            "required": [
                "type"
            ]
        },
        "dependencies": {
            "description": "Lists of system, runtime, and other skill dependencies.",
            "type": "object",
            "properties": {
                "system": {
                     "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "python": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "skills": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            }
        },
        "permissions": {
            "description": "Declares the resources the skill requires access to at runtime.",
            "type": "object",
            "properties": {
                "network": {
                    "type": "object",
                    "properties": {
                        "allowedHosts": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "allowedHosts",
                        "description"
                    ]
                },
                "filesystem": {
                    "type": "object",
                    "properties": {
                        "access": {
                            "type": "string",
                            "enum": [
                                "read",
                                "write",
                                "readWrite",
                                "none"
                            ]
                        },
                        "paths": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "access",
                        "description"
                    ]
                }
            }
        },
        "keywords": {
            "description": "An array of keywords to improve discoverability in the registry.",
            "type": "array",
            "items": {
                "type": "string",
                "pattern": "^[a-z0-9-]+$"
            }
        }
    },
    "required": [
        "name",
        "version",
        "description",
        "author",
        "license",
        "entrypoint"
    ]
}
```

## Field-by-Field Breakdown

### Required Fields

#### name

**Type:** String  
**Required:** Yes  
**Pattern:** `^[a-z0-9]+(-[a-z0-9]+)*$`  
**Max Length:** 40 characters

**Description:** Unique identifier for the skill. Must use lowercase letters, numbers, and hyphens only. The skill directory name must match this field exactly.

**Valid examples:**
- `"pdf-processor"`
- `"web-scraper"`
- `"data-analyzer-v2"`
- `"ml-predictor"`

**Invalid examples:**
- `"PDF_Processor"` (uppercase, underscore)
- `"web scraper"` (space)
- `"mySkill"` (camelCase)
- `"tool."` (ends with punctuation)

**Best practices:**
- Use descriptive names that indicate purpose
- Keep under 30 characters when possible
- Use hyphens to separate words
- Avoid version numbers in name (use version field instead)

---

#### version

**Type:** String  
**Required:** Yes  
**Pattern:** Semantic Versioning (SemVer)

**Description:** The skill version following SemVer specification: `MAJOR.MINOR.PATCH` with optional pre-release and build metadata.

**Format:** `MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]`

**Valid examples:**
- `"1.0.0"` (standard release)
- `"2.3.15"` (with minor and patch updates)
- `"0.1.0"` (initial development)
- `"1.0.0-alpha"` (pre-release)
- `"1.0.0-beta.1"` (numbered pre-release)
- `"1.0.0+20241102"` (with build metadata)
- `"2.0.0-rc.1+build.123"` (combined)

**Invalid examples:**
- `"1.0"` (missing patch version)
- `"v1.0.0"` (has 'v' prefix)
- `"1.0.0.0"` (too many parts)
- `"1.0.0-Beta"` (uppercase in pre-release)

**Versioning guidelines:**
- **MAJOR** (X.0.0): Breaking changes, incompatible API changes
- **MINOR** (0.X.0): New features, backwards compatible
- **PATCH** (0.0.X): Bug fixes, backwards compatible
- Start development at `0.1.0`
- First stable release should be `1.0.0`

---

#### description

**Type:** String  
**Required:** Yes  
**Min Length:** 20 characters  
**Max Length:** 250 characters

**Description:** Clear summary of what the skill does and when an AI agent should use it. This is critical for skill discovery and triggering.

**Must include:**
- **WHAT** the skill does (capabilities)
- **WHEN** to use it (triggers, scenarios, file types)

**Good examples:**
```json
{
  "description": "Processes and analyzes CSV files to generate statistical summaries. Use when the user uploads a CSV and requests data analysis, trends, or visualizations."
}
```

```json
{
  "description": "Extracts text and metadata from PDF documents using OCR when needed. Use when users upload PDFs or request PDF content extraction, form filling, or document analysis."
}
```

```json
{
  "description": "Queries BigQuery databases with pre-loaded schema knowledge. Use when users request data from BigQuery tables or ask analytical questions about the database."
}
```

**Bad examples:**
```json
{
  "description": "Processes files" 
  // Too short (14 chars), not descriptive
}
```

```json
{
  "description": "This skill is a comprehensive tool for data"
  // Doesn't specify WHEN to use it
}
```

**Best practices:**
- Front-load with the main purpose
- Include specific triggers (file types, keywords, scenarios)
- Use active voice
- Be concise but complete
- Aim for 80-150 characters for optimal readability

---

#### author

**Type:** String  
**Required:** Yes

**Description:** Name of the individual or organization that created the skill.

**Examples:**
- `"John Doe"`
- `"Acme Corp"`
- `"Data Team"`
- `"OpenAI"`

**Best practices:**
- Use real names or official organization names
- Avoid email addresses or URLs here (use repository field instead)
- Can be a team name for internal skills

---

#### license

**Type:** String  
**Required:** Yes

**Description:** SPDX license identifier for the skill. Should be an OSI-approved open source license or "Proprietary" for private skills.

**Common licenses:**
- `"MIT"` (most permissive, recommended for public skills)
- `"Apache-2.0"` (permissive with patent grant)
- `"GPL-3.0"` (copyleft, requires derivative works to be open source)
- `"BSD-3-Clause"` (permissive with attribution)
- `"Proprietary"` (private/commercial skills)

**Examples:**
```json
{
  "license": "MIT"
}
```

```json
{
  "license": "Apache-2.0"
}
```

**Best practices:**
- Use SPDX identifiers (see https://spdx.org/licenses/)
- Match the license in your LICENSE file
- MIT is recommended for community skills
- Use "Proprietary" for internal company skills

---

#### entrypoint

**Type:** String  
**Required:** Yes  
**Default:** `"README.md"`

**Description:** Path to the main documentation file displayed on the Skilzy registry. Should point to human-readable documentation (README.md), not agent instructions (SKILL.md).

**Valid examples:**
- `"README.md"` (standard, recommended)
- `"DOCUMENTATION.md"`
- `"docs/overview.md"`

**Invalid examples:**
- `"SKILL.md"` (this is for agents, not humans)
- `"script.py"` (must be markdown)

**Important:** AI agents always load SKILL.md directly for instructions, regardless of this field. The entrypoint is only for registry display.

---

### Optional Fields

#### licenseFile

**Type:** String  
**Required:** No  
**Default:** None

**Description:** Relative path to the file containing the full license text.

**Examples:**
- `"LICENSE"`
- `"LICENSE.txt"`
- `"LICENSE.md"`
- `"legal/LICENSE"`

**Best practices:**
- Include a license file in your skill
- Reference it here for visibility
- Place at skill root for easy discovery

---

#### repository

**Type:** Object  
**Required:** No

**Description:** Information about the skill's source code repository.

**Structure:**
```json
{
  "repository": {
    "type": "git",
    "url": "https://github.com/username/skill-name"
  }
}
```

**Properties:**
- `type` (required if repository specified): Currently only `"git"` supported
- `url` (required if repository specified): Full URL to the repository

**Examples:**
```json
{
  "repository": {
    "type": "git",
    "url": "https://github.com/acme/pdf-processor"
  }
}
```

```json
{
  "repository": {
    "type": "git",
    "url": "https://gitlab.com/team/data-analyzer"
  }
}
```

**Best practices:**
- Include for open source skills
- Use public URLs for discoverability
- Keep repository updated with releases

---

#### icon

**Type:** String  
**Required:** No

**Description:** Relative path to the skill's icon file for display in the Skilzy registry.

**Recommended format:** SVG (scalable, small file size)  
**Supported formats:** SVG, PNG, JPEG

**Examples:**
- `"assets/icon.svg"`
- `"icon.png"`
- `"images/logo.svg"`

**Best practices:**
- Use SVG for best quality and performance
- Keep file size under 50KB
- Use square aspect ratio (1:1)
- Recommended size: 512x512px for PNG
- Include meaningful branding or skill representation

---

#### runtime

**Type:** Object  
**Required:** No (but recommended)

**Description:** Specifies the execution environment required by the skill.

**Structure:**
```json
{
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  }
}
```

**Properties:**
- `type` (required): Runtime type (currently only `"python"` supported)
- `version` (optional): Version constraint using comparison operators

**Version operators:**
- `>=3.9` (greater than or equal to)
- `>3.8` (greater than)
- `==3.11` (exactly)
- `>=3.9,<4.0` (range)

**Examples:**
```json
{
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  }
}
```

```json
{
  "runtime": {
    "type": "python",
    "version": ">=3.11"
  }
}
```

**Best practices:**
- Always specify runtime for skills with scripts
- Use `>=3.9` for maximum compatibility
- Use specific versions only when necessary
- Test with the minimum version specified

---

#### dependencies

**Type:** Object  
**Required:** No

**Description:** Lists all external dependencies required by the skill.

**Structure:**
```json
{
  "dependencies": {
    "system": ["ffmpeg", "imagemagick"],
    "python": ["pandas>=2.0", "numpy>=1.20"],
    "skills": ["data-validator>=1.0.0"]
  }
}
```

**Properties:**

**dependencies.system** (Array of strings)
- System-level tools and binaries
- Examples: `"ffmpeg"`, `"imagemagick"`, `"node"`, `"git"`

**dependencies.python** (Array of strings)
- Python packages from PyPI
- Include version constraints when needed
- Examples: `"pandas>=2.0"`, `"requests"`, `"beautifulsoup4>=4.12"`

**dependencies.skills** (Array of strings)
- Other Skilzy skills required
- Use format: `"skill-name>=version"`
- Examples: `"pdf-processor>=1.0.0"`, `"data-validator>=2.1.0"`

**Examples:**

Minimal dependencies:
```json
{
  "dependencies": {
    "python": ["requests", "beautifulsoup4"]
  }
}
```

Complex dependencies:
```json
{
  "dependencies": {
    "system": ["ffmpeg", "imagemagick"],
    "python": [
      "pandas>=2.0.0",
      "numpy>=1.20.0",
      "pillow>=10.0.0"
    ],
    "skills": [
      "image-processor>=1.5.0"
    ]
  }
}
```

**Best practices:**
- **ALWAYS list dependencies** - Don't assume they're installed
- Use version constraints to prevent breaking changes
- Test with minimum versions specified
- Keep dependencies minimal
- Document why each dependency is needed (in README)

---

#### permissions

**Type:** Object  
**Required:** No

**Description:** Declares what resources the skill needs access to at runtime. Used for security and user consent.

**Structure:**
```json
{
  "permissions": {
    "network": {
      "allowedHosts": ["api.example.com", "*.github.com"],
      "description": "Fetch data from external APIs"
    },
    "filesystem": {
      "access": "readWrite",
      "paths": ["/tmp", "~/workspace"],
      "description": "Read input files and write processed results"
    }
  }
}
```

**Network Permissions:**

```json
{
  "network": {
    "allowedHosts": ["api.example.com", "*.openai.com"],
    "description": "Query OpenAI API for embeddings"
  }
}
```

- `allowedHosts` (required): Array of domains or wildcard patterns
- `description` (required): Human-readable explanation

**Filesystem Permissions:**

```json
{
  "filesystem": {
    "access": "read",
    "paths": ["~/Documents"],
    "description": "Read user documents for analysis"
  }
}
```

- `access` (required): `"read"`, `"write"`, `"readWrite"`, or `"none"`
- `paths` (optional): Array of path patterns
- `description` (required): Human-readable explanation

**Examples:**

Network access only:
```json
{
  "permissions": {
    "network": {
      "allowedHosts": ["api.stripe.com"],
      "description": "Process payments via Stripe API"
    }
  }
}
```

Filesystem access only:
```json
{
  "permissions": {
    "filesystem": {
      "access": "readWrite",
      "paths": ["/tmp"],
      "description": "Create temporary files during processing"
    }
  }
}
```

Both:
```json
{
  "permissions": {
    "network": {
      "allowedHosts": ["*.googleapis.com"],
      "description": "Query Google Cloud APIs"
    },
    "filesystem": {
      "access": "read",
      "paths": ["~/Downloads"],
      "description": "Read files from downloads folder"
    }
  }
}
```

**Best practices:**
- Only request permissions actually needed
- Be specific about hosts and paths
- Provide clear descriptions for user consent
- Use wildcards sparingly (`*.example.com` only when needed)

---

#### keywords

**Type:** Array of strings  
**Required:** No

**Description:** Array of keywords to improve discoverability in the Skilzy registry search.

**Pattern:** Each keyword must match `^[a-z0-9-]+$` (lowercase, numbers, hyphens only)

**Examples:**
```json
{
  "keywords": ["pdf", "document", "extraction", "ocr"]
}
```

```json
{
  "keywords": ["data-analysis", "csv", "excel", "statistics", "visualization"]
}
```

```json
{
  "keywords": ["web", "scraping", "html", "parsing", "automation"]
}
```

**Best practices:**
- Include 5-10 relevant keywords
- Use domain-specific terms users would search for
- Include file types if applicable (`"pdf"`, `"csv"`, `"json"`)
- Include use cases (`"automation"`, `"analysis"`, `"visualization"`)
- Use hyphens for multi-word terms (`"data-analysis"`, not `"data analysis"`)
- Don't repeat words from the skill name

---

## Validation Rules Summary

| Field | Required | Type | Constraints |
|-------|----------|------|-------------|
| name | ✅ Yes | string | Lowercase, hyphens, 1-40 chars |
| version | ✅ Yes | string | SemVer format |
| description | ✅ Yes | string | 20-250 chars |
| author | ✅ Yes | string | Any |
| license | ✅ Yes | string | SPDX identifier |
| entrypoint | ✅ Yes | string | Path to markdown file |
| licenseFile | ❌ No | string | Path to license file |
| repository | ❌ No | object | type + url |
| icon | ❌ No | string | Path to image file |
| runtime |  ❌ No | object | type + optional version |
| dependencies | ❌ No | object | system/python/skills arrays |
| permissions | ❌ No | object | network/filesystem objects |
| keywords | ❌ No | array | Lowercase strings |

---

## Common Patterns

### Minimal Valid skill.json

```json
{
  "name": "my-skill",
  "version": "1.0.0",
  "description": "A simple skill that does something useful. Use when users need that specific thing.",
  "author": "John Doe",
  "license": "MIT",
  "entrypoint": "README.md"
}
```

### Complete skill.json with All Fields

```json
{
  "name": "advanced-data-processor",
  "version": "2.1.3",
  "description": "Processes CSV and Excel files with advanced statistical analysis and visualization. Use when users upload tabular data and request insights, trends, or charts.",
  "author": "Data Analytics Team",
  "license": "Apache-2.0",
  "licenseFile": "LICENSE",
  "repository": {
    "type": "git",
    "url": "https://github.com/analytics/data-processor"
  },
  "icon": "assets/icon.svg",
  "entrypoint": "README.md",
  "runtime": {
    "type": "python",
    "version": ">=3.11"
  },
  "dependencies": {
    "system": ["pandoc"],
    "python": [
      "pandas>=2.0.0",
      "numpy>=1.24.0",
      "matplotlib>=3.7.0",
      "openpyxl>=3.1.0"
    ],
    "skills": []
  },
  "permissions": {
    "filesystem": {
      "access": "readWrite",
      "paths": ["/tmp", "~/workspace"],
      "description": "Read data files and write analysis results"
    }
  },
  "keywords": [
    "data",
    "csv",
    "excel",
    "analysis",
    "statistics",
    "visualization",
    "pandas"
  ]
}
```

### API Integration Skill

```json
{
  "name": "stripe-payment-processor",
  "version": "1.0.0",
  "description": "Processes payments and manages subscriptions via Stripe API. Use when users need to handle payments, create customers, or manage billing.",
  "author": "Payment Team",
  "license": "Proprietary",
  "licenseFile": "LICENSE",
  "entrypoint": "README.md",
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  },
  "dependencies": {
    "python": ["stripe>=7.0.0", "python-dotenv>=1.0.0"]
  },
  "permissions": {
    "network": {
      "allowedHosts": ["api.stripe.com"],
      "description": "Process payments via Stripe API"
    }
  },
  "keywords": ["payment", "stripe", "billing", "subscription", "api"]
}
```