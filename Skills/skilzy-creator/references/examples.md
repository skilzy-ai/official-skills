# Complete Skill Examples

This file contains complete, real-world examples of skill.json files for different types of skills. Use these as templates for your own skills.

## Example 1: skilzy-creator (This Skill)

**Type:** Development tool  
**Purpose:** Create and manage Skilzy skills  
**Features:** Scripts, references, comprehensive docs

```json
{
  "name": "skilzy-creator",
  "version": "1.0.0",
  "description": "Comprehensive toolset for creating, converting, validating, and packaging Skilzy-compliant AI agent skills. Use when users want to initialize new skills, convert Claude skills, validate compliance, or package for distribution.",
  "author": "Skilzy Team",
  "license": "MIT",
  "licenseFile": "LICENSE",
  "entrypoint": "README.md",
  "icon": "assets/icon.svg",
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  },
  "dependencies": {
    "python": [
      "PyYAML>=6.0",
      "jsonschema>=4.0"
    ]
  },
  "keywords": [
    "skill-creation",
    "development",
    "tooling",
    "validation",
    "packaging",
    "skilzy",
    "registry",
    "conversion"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/skilzy/skilzy-creator"
  }
}
```

**Directory structure:**
```
skilzy-creator/
├── skill.json
├── SKILL.md
├── README.md
├── LICENSE
├── assets/
│   └── icon.svg
├── scripts/
│   ├── init_skill.py
│   ├── convert_skill.py
│   ├── validate_skill.py
│   └── package_skill.py
└── references/
    ├── tool-init.md
    ├── tool-convert.md
    ├── tool-validate.md
     ├── tool-package.md
    ├── schema-reference.md
    ├── troubleshooting.md
    └── examples.md
```

---

## Example 2: Simple Data Processor

**Type:** Data analysis tool  
**Purpose:** Process CSV and Excel files  
**Features:** Minimal dependencies, focused scope

```json
{
  "name": "data-processor",
  "version": "1.0.0",
  "description": "Processes CSV and Excel files with statistical analysis. Use when users upload tabular data files (.csv, .xlsx) and request data analysis, summaries, or basic statistics.",
  "author": "Data Team",
  "license": "MIT",
  "licenseFile": "LICENSE",
  "entrypoint": "README.md",
  "icon": "assets/icon.svg",
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  },
  "dependencies": {
    "python": [
      "pandas>=2.0.0",
      "openpyxl>=3.1.0"
    ]
  },
  "permissions": {
    "filesystem": {
      "access": "read",
      "paths": ["~/Downloads", "~/Documents"],
      "description": "Read data files for analysis"
    }
  },
  "keywords": [
    "data",
    "csv",
    "excel",
    "analysis",
    "statistics",
    "pandas"
  ]
}
```

**Directory structure:**
```
data-processor/
├── skill.json
├── SKILL.md
├── README.md
├── LICENSE
├── assets/
│   └── icon.svg
└── scripts/
    ├── process_csv.py
    ├── process_excel.py
    └── calculate_stats.py
```

---

## Example 3: PDF Processing Skill

**Type:** Document processor  
**Purpose:** Extract and manipulate PDF files  
**Features:** System dependencies, multiple scripts

```json
{
  "name": "pdf-processor",
  "version": "2.1.0",
  "description": "Extracts text, images, and metadata from PDF documents with OCR support. Use when users upload PDF files or request PDF content extraction, form filling, merging, or document analysis.",
  "author": "Document Solutions Inc",
  "license": "Apache-2.0",
  "licenseFile": "LICENSE.txt",
  "entrypoint": "README.md",
  "icon": "assets/icon.svg",
  "runtime": {
    "type": "python",
    "version": ">=3.10"
  },
  "dependencies": {
    "system": [
      "poppler-utils",
      "tesseract"
    ],
    "python": [
      "PyPDF2>=3.0.0",
      "pdfplumber>=0.10.0",
      "pillow>=10.0.0",
      "pytesseract>=0.3.10"
    ]
  },
  "permissions": {
    "filesystem": {
      "access": "readWrite",
      "paths": ["/tmp", "~/Documents"],
      "description": "Read PDF files and write extracted content"
    }
  },
  "keywords": [
    "pdf",
    "document",
    "extraction",
    "ocr",
    "text-extraction",
    "forms",
    "merge"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/docsolutions/pdf-processor"
  }
}
```

**Directory structure:**
```
pdf-processor/
├── skill.json
├── SKILL.md
├── README.md
├── LICENSE.txt
├── assets/
│   └── icon.svg
├── scripts/
│   ├── extract_text.py
│   ├── extract_images.py
│   ├── ocr_pdf.py
│   ├── merge_pdfs.py
│   └── fill_form.py
└── references/
    └── form-fields-guide.md
```

---

## Example 4: API Integration Skill

**Type:** External service integration  
**Purpose:** Interact with external API   
**Features:** Network permissions, API credentials

```json
{
  "name": "stripe-payment-handler",
  "version": "1.3.2",
  "description": "Processes payments, manages subscriptions, and handles billing through Stripe API. Use when users need to process payments, create customer accounts, manage subscriptions, or handle refunds.",
  "author": "Payment Services Team",
  "license": "Proprietary",
  "licenseFile": "LICENSE",
  "entrypoint": "README.md",
  "icon": "assets/stripe-icon.svg",
  "runtime": {
    "type": "python",
    "version": ">=3.11"
  },
  "dependencies": {
    "python": [
      "stripe>=7.0.0",
      "python-dotenv>=1.0.0",
      "requests>=2.31.0"
    ]
  },
  "permissions": {
    "network": {
      "allowedHosts": [
        "api.stripe.com",
        "files.stripe.com"
      ],
      "description": "Connect to Stripe API for payment processing"
    },
    "filesystem": {
      "access": "read",
      "paths": ["~/.env"],
      "description": "Read API credentials from environment file"
    }
  },
  "keywords": [
    "payment",
    "stripe",
    "billing",
    "subscription",
    "api",
    "ecommerce",
    "checkout"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/internal/stripe-handler"
  }
}
```

**Directory structure:**
```
stripe-payment-handler/
├── skill.json
├── SKILL.md
├── README.md
├── LICENSE
├── assets/
│   └── stripe-icon.svg
├── scripts/
│   ├── create_payment.py
│   ├── create_customer.py
│   ├── manage_subscription.py
│   └── process_refund.py
└── references/
    ├── api-endpoints.md
    └── error-codes.md
```

---

## Example 5: Web Scraping Skill

**Type:** Data extraction  
**Purpose:** Scrape structured data from websites  
**Features:** Network permissions, parsing libraries

```json
{
  "name": "web-scraper",
  "version": "0.5.0",
  "description": "Extracts structured data from websites using customizable scraping rules. Use when users need to collect data from HTML pages, monitor website changes, or extract tables and lists from web content.",
  "author": "Automation Labs",
  "license": "MIT",
  "licenseFile": "LICENSE",
  "entrypoint": "README.md",
  "icon": "assets/icon.svg",
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  },
  "dependencies": {
    "python": [
      "requests>=2.31.0",
      "beautifulsoup4>=4.12.0",
      "lxml>=4.9.0",
      "selenium>=4.15.0"
    ],
    "system": [
      "chromium-driver"
    ]
  },
  "permissions": {
    "network": {
      "allowedHosts": ["*"],
      "description": "Access websites for data extraction (user provides URLs)"
    },
    "filesystem": {
      "access": "write",
      "paths": ["/tmp", "~/Downloads"],
      "description": "Save extracted data to files"
    }
  },
  "keywords": [
    "web",
    "scraping",
    "html",
    "parsing",
    "extraction",
    "automation",
    "selenium"
  ]
}
```

**Directory structure:**
```
web-scraper/
├── skill.json
├── SKILL.md
├── README.md
├── LICENSE
├── assets/
│   └── icon.svg
├── scripts/
│   ├── scrape_static.py
│   ├── scrape_dynamic.py
│   └── parse_html.py
└── references/
    ├── css-selectors.md
    └── best-practices.md
```

---

## Example 6: Frontend Template Builder

**Type:** Code generator  
**Purpose:** Generate frontend applications  
**Features:** Asset templates, boilerplate code

```json
{
  "name": "frontend-webapp-builder",
  "version": "2.0.1",
  "description": "Generates React and HTML frontend applications from user requirements with pre-built templates. Use when users request to build web apps, dashboards, landing pages, or frontend components.",
  "author": "WebDev Collective",
  "license": "MIT",
  "licenseFile": "LICENSE",
  "entrypoint": "README.md",
  "icon": "assets/react-icon.svg",
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  },
  "dependencies": {
    "system": [
      "node",
      "npm"
    ],
    "python": [
      "jinja2>=3.1.0"
    ]
  },
  "permissions": {
    "filesystem": {
      "access": "readWrite",
      "paths": ["~/projects", "~/workspace"],
      "description": "Create and write frontend project files"
    }
  },
  "keywords": [
    "frontend",
    "react",
    "webapp",
    "html",
    "javascript",
    "templates",
    "boilerplate"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/webdev/webapp-builder"
  }
}
```

**Directory structure:**
```
frontend-webapp-builder/
├── skill.json
├── SKILL.md
├── README.md
├── LICENSE
├── assets/
│   ├── react-icon.svg
│   ├── templates/
│   │   ├── react-basic/
│   │   │   ├── package.json
│   │   │   ├── src/
│   │   │   └── public/
│   │   └── html-basic/
│   │       ├── index.html
│   │       ├── style.css
│   │       └── script.js
└── scripts/
    ├── generate_react_app.py
    ├── generate_html_site.py
    └── customize_template.py
```

---

## Example 7: Database Query Assistant

**Type:** Database integration  
**Purpose:** Query and analyze databases  
**Features:** Reference schemas, SQL generation

```json
{
  "name": "bigquery-assistant",
  "version": "1.2.0",
  "description": "Queries Google BigQuery databases with pre-loaded schema knowledge and generates optimized SQL. Use when users request data from BigQuery tables, ask analytical questions about the database, or need query optimization.",
  "author": "Data Analytics Corp",
  "license": "Apache-2.0",
  "licenseFile": "LICENSE",
  "entrypoint": "README.md",
  "icon": "assets/bigquery-icon.svg",
  "runtime": {
    "type": "python",
    "version": ">=3.10"
  },
  "dependencies": {
    "python": [
      "google-cloud-bigquery>=3.11.0",
      "pandas>=2.0.0",
      "sqlparse>=0.4.4"
    ]
  },
  "permissions": {
    "network": {
      "allowedHosts": [
        "*.googleapis.com"
      ],
      "description": "Connect to Google BigQuery API"
    },
    "filesystem": {
      "access": "read",
      "paths": ["~/.config/gcloud"],
      "description": "Read Google Cloud credentials"
    }
  },
  "keywords": [
    "bigquery",
    "sql",
    "database",
    "analytics",
    "google-cloud",
    "data-warehouse"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/analytics/bigquery-assistant"
  }
}
```

**Directory structure:**
```
bigquery-assistant/
├── skill.json
├── SKILL.md
├── README.md
├── LICENSE
├── assets/
│   └── bigquery-icon.svg
├── scripts/
│   ├── execute_query.py
│   ├── optimize_sql.py
│   └── export_results.py
└── references/
    ├── schema.md
    ├── common-queries.md
    └── performance-tips.md
```

---

## Example 8: Image Processing Skill

**Type:** Media processor  
**Purpose:** Edit and transform images  
**Features:** System dependencies, multiple formats

```json
{
  "name": "image-editor",
  "version": "1.4.2",
  "description": "Edits, transforms, and optimizes images with support for multiple formats. Use when users upload images and request resizing, cropping, format conversion, filters, or optimization.",
  "author": "Media Tools Team",
  "license": "MIT",
  "licenseFile": "LICENSE",
  "entrypoint": "README.md",
  "icon": "assets/icon.svg",
  "runtime": {
    "type": "python",
    "version": ">=3.9"
  },
  "dependencies": {
    "system": [
      "imagemagick",
      "ffmpeg"
    ],
    "python": [
      "Pillow>=10.0.0",
      "opencv-python>=4.8.0",
      "numpy>=1.24.0"
    ]
  },
  "permissions": {
    "filesystem": {
      "access": "readWrite",
      "paths": ["/tmp", "~/Pictures", "~/Downloads"],
      "description": "Read source images and write processed results"
    }
  },
  "keywords": [
    "image",
    "photo",
    "editing",
    "resize",
    "crop",
    "filter",
    "conversion",
    "optimization"
  ]
}
```

**Directory structure:**
```
image-editor/
├── skill.json
├── SKILL.md
├── README.md
├── LICENSE
├── assets/
│   └── icon.svg
├── scripts/
│   ├── resize_image.py
│   ├── crop_image.py
│   ├── apply_filter.py
│   ├── convert_format.py
│   └── optimize_image.py
└── references/
    └── supported-formats.md
```

---

## Example 9: Minimal Skill (Bare Minimum)

**Type:** Simple utility  
**Purpose:** Demonstrates minimum required fields  
**Features:** No dependencies, no permissions

```json
{
  "name": "text-counter",
  "version": "1.0.0",
  "description": "Counts words, characters, and lines in text. Use when users provide text and request word count, character count, or text statistics.",
  "author": "John Doe",
  "license": "MIT",
  "entrypoint": "README.md"
}
```

**Directory structure:**
```
text-counter/
├── skill.json
├── SKILL.md
├── README.md
└── LICENSE
```

**Note:** This is the absolute minimum. Most skills should include more metadata (icon, keywords, runtime, dependencies) for better functionality and discoverability.

---

## Pattern Summary

### Common Field Patterns

**For development tools:**
```json
{
  "keywords": ["development", "tooling", "automation", "cli"],
  "dependencies": {
    "python": ["tool-specific-libs"]
  }
}
```

**For data processing:**
```json
{
  "keywords": ["data", "analysis", "processing", "file-format"],
  "dependencies": {
    "python": ["pandas", "numpy"]
  },
  "permissions": {
    "filesystem": {
      "access": "read",
      "paths": ["~/Documents", "~/Downloads"],
      "description": "Read data files"
    }
  }
}
```

**For API integrations:**
```json
{
  "keywords": ["api", "integration", "service-name"],
  "dependencies": {
    "python": ["requests", "service-sdk"]
  },
  "permissions": {
    "network": {
      "allowedHosts": ["api.service.com"],
      "description": "Connect to Service API"
    }
  }
}
```

**For document processing:**
```json
{
  "keywords": ["document", "pdf", "text-extraction"],
  "dependencies": {
    "system": ["poppler-utils"],
    "python": ["document-libs"]
  },
  "permissions": {
    "filesystem": {
      "access": "readWrite",
      "paths": ["/tmp"],
      "description": "Process document files"
    }
  }
}
```

Use these examples as starting points and customize for your specific skill requirements.