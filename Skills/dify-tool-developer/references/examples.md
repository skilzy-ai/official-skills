# Dify Plugin Examples

Real-world plugin examples demonstrating different patterns and use cases.

---

## Example 1: Simple API Tool (Weather)

A basic tool that calls an external weather API.

### Requirements
- Network access
- API key

### File Structure
```
weather-tool/
├── manifest.yaml
├── provider/
│   ├── weather-tool.yaml
│   └── weather-tool.py
├── tools/
│   ├── get-weather.yaml
│   └── get-weather.py
├── main.py
└── requirements.txt
```

### tools/get-weather.yaml
```yaml
identity:
  name: "get-weather"
  author: "your-author-name"
  label:
    en_US: "Get Weather"
    zh_Hans: "获取天气"

description:
  human:
    en_US: "Fetch current weather for a location"
    zh_Hans: "获取位置的当前天气"
  llm: "Fetches current weather data for a specified city using OpenWeatherMap API"

parameters:
  - name: city
    type: string
    required: true
    label:
      en_US: "City Name"
      zh_Hans: "城市名称"
    human_description:
      en_US: "Name of the city to get weather for"
      zh_Hans: "要获取天气的城市名称"
    llm_description: "The city name to fetch weather data for (e.g., London, Tokyo, New York)"
    form: llm

  - name: units
    type: string
    required: false
    label:
      en_US: "Units"
      zh_Hans: "单位"
    human_description:
      en_US: "Temperature units (metric or imperial)"
      zh_Hans: "温度单位（公制或英制）"
    llm_description: "Temperature units: 'metric' for Celsius or 'imperial' for Fahrenheit"
    form: llm

extra:
  python:
    source: tools/get-weather.py
```

### tools/get-weather.py
```python
from collections.abc import Generator
from typing import Any
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetWeatherTool(Tool):
    """
    Fetch current weather data for a city
    """

    def _invoke(
        self, 
        tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage]:
        """
        Fetch weather data from OpenWeatherMap API
        """
        try:
            # Extract parameters
            city = tool_parameters.get("city", "")
            units = tool_parameters.get("units", "metric")

            # Validate required parameter
            if not city:
                yield self.create_text_message("Error: City name is required")
                return

            # Get API key from credentials
            api_key = self.runtime.credentials.get("api_key")

            if not api_key:
                yield self.create_text_message("Error: API key not configured")
                return

            # Call weather API
            url = "https://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": city,
                "appid": api_key,
                "units": units
            }

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            # Extract relevant data
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            # Format result
            unit_symbol = "°C" if units == "metric" else "°F"
            result_text = f"""Weather in {city}:
Temperature: {temp}{unit_symbol}
Feels like: {feels_like}{unit_symbol}
Conditions: {description}
Humidity: {humidity}%"""

            # Return text message
            yield self.create_text_message(result_text)

            # Return structured data
            yield self.create_json_message({
                "city": city,
                "temperature": temp,
                "feels_like": feels_like,
                "description": description,
                "humidity": humidity,
                "units": units
            })

        except requests.HTTPError as e:
            if e.response.status_code == 404:
                yield self.create_text_message(f"Error: City '{city}' not found")
            else:
                yield self.create_text_message(f"API Error: {str(e)}")
        except requests.Timeout:
            yield self.create_text_message("Error: Request timed out")
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
```

### provider/weather-tool.yaml
```yaml
identity:
  author: "your-author-name"
  name: "weather-tool"
  label:
    en_US: "Weather Tool"
    zh_Hans: "天气工具"
  description:
    en_US: "Get current weather data"
    zh_Hans: "获取当前天气数据"
  icon: icon.svg

credentials_for_provider:
  api_key:
    type: secret-input
    required: true
    label:
      en_US: "OpenWeatherMap API Key"
      zh_Hans: "OpenWeatherMap API 密钥"
    placeholder:
      en_US: "Enter your API key"
      zh_Hans: "输入您的 API 密钥"
    help:
      en_US: "Get your free API key at https://openweathermap.org/api"
      zh_Hans: "在 https://openweathermap.org/api 获取免费 API 密钥"
    url: https://openweathermap.org/api

tools:
  - tools/get-weather.yaml

extra:
  python:
    source: provider/weather-tool.py
```

### requirements.txt
```
dify_plugin>=0.0.1
requests>=2.31.0
```

---

## Example 2: Text Processing Tool (No API)

A tool that processes text locally without external APIs.

### Requirements
- No network access needed
- No credentials needed

### tools/text-analyzer.yaml
```yaml
identity:
  name: "text-analyzer"
  author: "your-author-name"
  label:
    en_US: "Text Analyzer"

description:
  human:
    en_US: "Analyze text for word count, character count, and sentiment"
  llm: "Analyzes text to provide statistics and basic sentiment analysis"

parameters:
  - name: text
    type: string
    required: true
    label:
      en_US: "Text to Analyze"
    llm_description: "The text content to analyze"
    form: llm

extra:
  python:
    source: tools/text-analyzer.py
```

### tools/text-analyzer.py
```python
from collections.abc import Generator
from typing import Any
import re

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class TextAnalyzerTool(Tool):
    """
    Analyze text for various metrics
    """

    def _invoke(
        self, 
        tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage]:
        """
        Analyze the provided text
        """
        try:
            # Extract parameter
            text = tool_parameters.get("text", "")

            if not text:
                yield self.create_text_message("Error: Text is required")
                return

            # Calculate metrics
            char_count = len(text)
            char_count_no_spaces = len(text.replace(" ", ""))
            word_count = len(text.split())
            sentence_count = len(re.split(r'[.!?]+', text)) - 1
            paragraph_count = len([p for p in text.split('

') if p.strip()])

            # Simple sentiment (very basic)
            positive_words = ['good', 'great', 'excellent', 'happy', 'love']
            negative_words = ['bad', 'terrible', 'awful', 'sad', 'hate']

            text_lower = text.lower()
            positive_count = sum(1 for word in positive_words if word in text_lower)
            negative_count = sum(1 for word in negative_words if word in text_lower)

            if positive_count > negative_count:
                sentiment = "Positive"
            elif negative_count > positive_count:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            # Format result
            result_text = f"""Text Analysis Results:

Characters: {char_count} ({char_count_no_spaces} without spaces)
Words: {word_count}
Sentences: {sentence_count}
Paragraphs: {paragraph_count}
Estimated Sentiment: {sentiment}"""

            yield self.create_text_message(result_text)

            # Return structured data
            yield self.create_json_message({
                "character_count": char_count,
                "character_count_no_spaces": char_count_no_spaces,
                "word_count": word_count,
                "sentence_count": sentence_count,
                "paragraph_count": paragraph_count,
                "sentiment": sentiment
            })

        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
```

---

## Example 3: Multi-Tool Plugin (Calculator)

A plugin with multiple related tools.

### File Structure
```
calculator/
├── manifest.yaml
├── provider/
│   ├── calculator.yaml
│   └── calculator.py
├── tools/
│   ├── add.yaml
│   ├── add.py
│   ├── subtract.yaml
│   ├── subtract.py
│   ├── multiply.yaml
│   └── multiply.py
├── main.py
└── requirements.txt
```

### tools/add.yaml
```yaml
identity:
  name: "add"
  author: "your-author-name"
  label:
    en_US: "Add Numbers"

description:
  human:
    en_US: "Add two or more numbers"
  llm: "Calculates the sum of two or more numbers"

parameters:
  - name: numbers
    type: string
    required: true
    label:
      en_US: "Numbers"
    llm_description: "Comma-separated numbers to add (e.g., '5,10,15')"
    form: llm

extra:
  python:
    source: tools/add.py
```

### tools/add.py
```python
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class AddTool(Tool):
    """Add multiple numbers"""

    def _invoke(
        self, 
        tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage]:
        try:
            numbers_str = tool_parameters.get("numbers", "")

            if not numbers_str:
                yield self.create_text_message("Error: Numbers required")
                return

            # Parse numbers
            try:
                numbers = [float(n.strip()) for n in numbers_str.split(',')]
            except ValueError:
                yield self.create_text_message("Error: Invalid number format")
                return

            # Calculate sum
            result = sum(numbers)

            yield self.create_text_message(
                f"Sum of {', '.join(str(n) for n in numbers)} = {result}"
            )

            yield self.create_variable_message("result", result)

        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
```

### provider/calculator.yaml
```yaml
identity:
  author: "your-author-name"
  name: "calculator"
  label:
    en_US: "Calculator"
  description:
    en_US: "Basic math operations"
  icon: icon.svg

tools:
  - tools/add.yaml
  - tools/subtract.yaml
  - tools/multiply.yaml

extra:
  python:
    source: provider/calculator.py
```

**Note:** Implement `subtract.py` and `multiply.py` following the same pattern as `add.py`, with each in a separate file.

---

## Example 4: OAuth Tool (GitHub)

A tool using OAuth authentication (conceptual example).

### tools/github-issues.yaml
```yaml
identity:
  name: "list-issues"
  author: "your-author-name"
  label:
    en_US: "List GitHub Issues"

description:
  human:
    en_US: "List issues from a GitHub repository"
  llm: "Retrieves a list of issues from a specified GitHub repository"

parameters:
  - name: repo
    type: string
    required: true
    label:
      en_US: "Repository"
    llm_description: "Repository in format 'owner/repo' (e.g., 'facebook/react')"
    form: llm

extra:
  python:
    source: tools/github-issues.py
```

### tools/github-issues.py
```python
from collections.abc import Generator
from typing import Any
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class ListIssuesTool(Tool):
    """List GitHub repository issues"""

    def _invoke(
        self, 
        tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage]:
        try:
            repo = tool_parameters.get("repo", "")

            if not repo or '/' not in repo:
                yield self.create_text_message(
                    "Error: Repository must be in format 'owner/repo'"
                )
                return

            # Get OAuth access token
            access_token = self.runtime.credentials.get("access_token")

            if not access_token:
                yield self.create_text_message("Error: OAuth not configured")
                return

            # Call GitHub API
            url = f"https://api.github.com/repos/{repo}/issues"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/vnd.github.v3+json"
            }

            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            issues = response.json()

            if not issues:
                yield self.create_text_message(f"No issues found in {repo}")
                return

            # Format issues
            issues_text = f"Issues in {repo}:\n\n"
            for i, issue in enumerate(issues[:10], 1):  # Limit to 10
                issues_text += f"{i}. #{issue['number']}: {issue['title']}\n"
                issues_text += f"   Status: {issue['state']}\n"
                issues_text += f"   URL: {issue['html_url']}\n\n"

            yield self.create_text_message(issues_text)

            yield self.create_json_message({
                "repo": repo,
                "count": len(issues),
                "issues": issues[:10]
            })

        except requests.HTTPError as e:
            yield self.create_text_message(f"GitHub API Error: {str(e)}")
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
```

### provider/github-tool.yaml
```yaml
identity:
  author: "your-author-name"
  name: "github-tool"
  label:
    en_US: "GitHub Tool"
  description:
    en_US: "Access GitHub via OAuth"
  icon: icon.svg

oauth_schema:
  client:
    - name: client_id
      type: string
      required: true
      label:
        en_US: "Client ID"
    - name: client_secret
      type: secret-input
      required: true
      label:
        en_US: "Client Secret"
  authorization:
    url: https://github.com/login/oauth/authorize
    scopes:
      - repo
      - read:user
  token:
    url: https://github.com/login/oauth/access_token
    headers:
      Accept: application/json

tools:
  - tools/github-issues.yaml

extra:
  python:
    source: provider/github-tool.py
```

**Note:** For complete OAuth implementation, see the official `tool-oauth.md` documentation.

---

## Common Patterns

### Pattern: Error Handling
```python
try:
    # Operation
    result = process_data()
    yield self.create_text_message(result)
except ValueError as e:
    yield self.create_text_message(f"Validation Error: {str(e)}")
except requests.HTTPError as e:
    yield self.create_text_message(f"API Error: {str(e)}")
except requests.Timeout:
    yield self.create_text_message("Error: Request timed out")
except Exception as e:
    yield self.create_text_message(f"Unexpected Error: {str(e)}")
```

### Pattern: Parameter Validation
```python
# Required parameter
param = tool_parameters.get("param_name", "")
if not param:
    yield self.create_text_message("Error: param_name is required")
    return

# Optional parameter with default
optional = tool_parameters.get("optional_param", "default_value")

# Type conversion
try:
    count = int(tool_parameters.get("count", "10"))
except ValueError:
    yield self.create_text_message("Error: count must be a number")
    return
```

### Pattern: API Calls with Credentials
```python
api_key = self.runtime.credentials.get("api_key")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(
    "https://api.example.com/endpoint",
    headers=headers,
    timeout=10
)
response.raise_for_status()
data = response.json()
```

---

## Testing Examples

### Example Test Script
```python
# test_tool.py
from tools.get_weather import GetWeatherTool

def test_weather_tool():
    tool = GetWeatherTool()

    # Mock runtime and credentials
    class MockRuntime:
        credentials = {"api_key": "test_key"}

    tool.runtime = MockRuntime()

    # Test with valid parameters
    params = {"city": "London", "units": "metric"}
    results = list(tool._invoke(params))

    print(f"Results: {results}")
    assert len(results) > 0

if __name__ == "__main__":
    test_weather_tool()
```

---

## Initialization Commands Used

### Weather Tool
```bash
dify plugin init \
  --name "weather-tool" \
  --author "your-author-name" \
  --description "Get current weather data" \
  --category tool \
  --language python \
  --allow-network \
  --quick
```

### Text Analyzer (No Network)
```bash
dify plugin init \
  --name "text-analyzer" \
  --author "your-author-name" \
  --description "Analyze text content" \
  --category tool \
  --language python \
  --quick
```

### Calculator (Multiple Tools)
```bash
dify plugin init \
  --name "calculator" \
  --author "your-author-name" \
  --description "Basic math operations" \
  --category tool \
  --language python \
  --quick
```

### GitHub OAuth Tool
```bash
dify plugin init \
  --name "github-tool" \
  --author "your-author-name" \
  --description "Access GitHub via OAuth" \
  --category tool \
  --language python \
  --allow-network \
  --quick
```

---

These examples demonstrate the key patterns you'll use when developing Dify tool plugins. Adapt them to your specific use case!
