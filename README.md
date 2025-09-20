# Insight

**Insight** is a Python-based CLI tool that analyzes codebases and generates detailed reports.
It provides both static analysis and AI-powered explanations (via Gemini API or local models).

## Features

* Analyze 30+ programming, web, and config file types.
* Generate a `report/` folder with:

  * One detailed `.md` file per source file.
  * A `summary.md` overview of the entire codebase.
* Collect static metrics:

  * Total lines
  * Functions, classes, imports
  * Number of comments
* AI-powered insights:

  * File explanations in plain language
  * Probability score (1–10) for AI/LLM-generated code

## Installation

Clone the repository:

```bash
git clone https://github.com/ExplainHub/Insight-Py.git
cd insight
```

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
pip install -e .
```
## Setup

If using Gemini API, set your API key:

```bash
export GEMINI_API_KEY="your_api_key_here"   # Mac/Linux
setx GEMINI_API_KEY "your_api_key_here"     # Windows
```

## Usage

Analyze the current directory:

```bash
insight .
```

Limit the number of files analyzed (useful for testing):

```bash
insight . --limit 5
```

Change output directory:

```bash
insight . -o my_reports
```

Reports will be saved in the specified folder, one Markdown file per source file plus a `summary.md`.

## Supported File Types

* Programming: `.py`, `.js`, `.ts`, `.java`, `.cpp`, `.c`, `.cs`, `.go`, `.php`, `.rb`, `.rs`, `.swift`, `.kt`, `.scala`, `.dart`, `.m`, `.mm`, `.lua`, `.pl`, `.sh`, `.bat`
* Web: `.html`, `.htm`, `.css`, `.scss`, `.less`, `.ejs`, `.erb`, `.mustache`
* Config: `.json`, `.yaml`, `.yml`, `.toml`, `.ini`, `.cfg`, `.xml`
* Docs: `.md`, `.rst`
* Build/DevOps: `.gradle`, `.pom`, `.makefile`, `.cmake`, `.dockerfile`
* Database: `.sql`

## Roadmap

* Add `.insightignore` support to skip specific files/folders.
* Export reports in HTML and PDF formats.
* Support for local AI engines (Ollama, LM Studio).
* Interactive web dashboard for reports.

## License

This project is licensed under the MIT License.


