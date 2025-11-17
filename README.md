# Insight — Code Analysis CLI

**Insight** is a Python-based command-line tool that analyzes codebases and generates detailed reports.  
It combines static code analysis with AI-powered explanations using the Gemini API or local models.

## Download Stats

<div align="center">

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/insight-cli-sarang?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=YELLOWGREEN&left_text=Total)](https://pepy.tech/projects/insight-cli-sarang)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/insight-cli-sarang?period=monthly&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=MAGENTA&left_text=Monthly)](https://pepy.tech/projects/insight-cli-sarang)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/insight-cli-sarang?period=weekly&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=BLUE&left_text=Weekly)](https://pepy.tech/projects/insight-cli-sarang)

</div>

## Features

* Analyze 30+ programming, web, and configuration file types.
* Generate a `report/` folder containing:

  * One detailed `.md` file per source file
  * A `summary.md` overview of the entire codebase
* Collect static metrics:

  * Total lines of code
  * Functions, classes, imports
  * Number of comments
* AI-powered insights:

  * File explanations in plain language
  * Probability score (1–10) for AI/LLM-generated code

## Installation

Clone the repository:

```bash
git clone https://github.com/XplnHUB/Insight-Py.git
cd Insight-Py
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

Limit the number of files analyzed (for testing):

```bash
insight . --limit 5
```

Change the output directory:

```bash
insight . -o my_reports
```

Reports are saved in the specified folder, with one Markdown file per source file plus a `summary.md`..

## Supported File Types

* **Programming:** `.py`, `.js`, `.ts`, `.java`, `.cpp`, `.c`, `.cs`, `.go`, `.php`, `.rb`, `.rs`, `.swift`, `.kt`, `.scala`, `.dart`, `.m`, `.mm`, `.lua`, `.pl`, `.sh`, `.bat`
* **Web:** `.html`, `.htm`, `.css`, `.scss`, `.less`, `.ejs`, `.erb`, `.mustache`
* **Config:** `.json`, `.yaml`, `.yml`, `.toml`, `.ini`, `.cfg`, `.xml`
* **Docs:** `.md`, `.rst`
* **Build/DevOps:** `.gradle`, `.pom`, `.makefile`, `.cmake`, `.dockerfile`
* **Database:** `.sql`

## Roadmap

* Add `.insightignore` support to skip files/folders
* Export reports in HTML and PDF formats
* Support for local AI engines (Ollama, LM Studio)
* Interactive web dashboard for reports

## 📖 Full Documentation

For detailed instructions, see [INSTRUCTION.md](INSTRUCTION.md).

## License

This project is licensed under the MIT License.

