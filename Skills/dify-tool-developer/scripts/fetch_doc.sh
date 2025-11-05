#!/bin/bash
# Helper script to fetch official Dify documentation

DOC_NAME=$1
BASE_URL="https://docs.dify.ai/plugin-dev-en"

if [ -z "$DOC_NAME" ]; then
    echo "Usage: bash scripts/fetch_doc.sh [tool|oauth|debug|init]"
    echo ""
    echo "Available docs:"
    echo "  tool  - Tool plugin development guide"
    echo "  oauth - OAuth implementation guide"
    echo "  debug - Debugging and logging guide"
    echo "  init  - CLI installation and setup"
    exit 1
fi

case $DOC_NAME in
  "init"|"initialize"|"setup")
    echo "Fetching: Initialize Development Tools..."
    curl -s "$BASE_URL/0221-initialize-development-tools.md"
    ;;
  "tool"|"tool-plugin"|"plugin")
    echo "Fetching: Tool Plugin Guide..." >&2
    curl -s "$BASE_URL/0222-tool-plugin.md"
    ;;
  "debug"|"debugging"|"logs"|"logging")
    echo "Fetching: Debugging Logs Guide..." >&2
    curl -s "$BASE_URL/0222-debugging-logs.md"
    ;;
  "oauth"|"auth"|"authentication")
    echo "Fetching: OAuth Guide..." >&2
    curl -s "$BASE_URL/0222-tool-oauth.md"
    ;;
  *)
    echo "Unknown doc: $DOC_NAME"
    echo "Available: tool, oauth, debug, init"
    exit 1
    ;;
esac
