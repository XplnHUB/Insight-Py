# Instructions to Run Insight CLI

Insight CLI is a codebase explainer tool powered by Google Generative AI.  
Follow the steps below to set it up and run it on your machine.

---

## 1. Clone / Open the Project
If you already have the project folder, skip this step.  
Otherwise:
```bash
git clone <your-repo-url>
cd <project-folder>
```

---

## 2. Create a Virtual Environment

Inside the project directory:

```bash
python3 -m venv venv
```

---

## 3. Activate the Virtual Environment

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows (PowerShell):

```powershell
venv\Scripts\Activate.ps1
```

You should now see `(venv)` in your terminal prompt.

---

## 4. Install Dependencies

Install the published package:

```bash
pip install insight-cli-sarang
```

---

## 5. Set Your Google API Key

The tool requires a Google API Key for Generative AI.
Replace `your_api_key_here` with your actual key.

On macOS/Linux:

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

On Windows (PowerShell):

```powershell
setx GOOGLE_API_KEY "your_api_key_here"
```

Note: The `export` command only works for the current session.
If you want the key to be available permanently, add it to your shell profile (`.zshrc`, `.bashrc`, or PowerShell profile).

---

## 6. Run the CLI

Basic usage:

```bash
insight-cli <path-to-codebase>
```

Example: analyze the current folder and save reports in `reports/`:

```bash
insight-cli . -o reports
```

Limit the number of files analyzed (e.g., 10 files):

```bash
insight-cli . --limit 10
```

---

## 7. Help Menu

For all available options:

```bash
insight-cli --help
```
