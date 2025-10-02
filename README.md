# Insight

**Insight** is a powerful Python CLI tool that analyzes codebases and generates comprehensive reports combining static analysis with AI-powered insights using Google's Gemini API.

## ✨ Features

### 📁 **Multi-Language Support**

- Supports **30+ file types** including Python, JavaScript, TypeScript, Java, C++, Go, and more
- Analyzes web technologies (HTML, CSS, React), configuration files (JSON, YAML), and documentation

### 📊 **Comprehensive Analysis**

- **Static Metrics:** Lines of code, functions, classes, imports, and comments
- **AI Insights:** Plain-language explanations and AI-generation probability scores (1-10)
- **Organized Reports:** Individual analysis files plus executive summary

### 🚀 **Easy to Use**

- Simple CLI interface with intuitive commands
- Flexible output options and file limiting for large projects
- Detailed error messages and helpful troubleshooting

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/XplnHUB/Insight-Py.git
cd Insight-Py
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate        # Mac/Linux
# OR
venv\Scripts\activate          # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

### 4. Configure API Key

Follow the [Configuration](#configuration) section below to set up your Google Gemini API key.

### 5. Test Installation

```bash
insight --help
```

You should see the help message confirming successful installation.

## Configuration

### API Key Setup

Insight uses the Google Gemini API for AI-powered code analysis. You'll need to configure your API key before using the tool.

#### 1. Get Your API Key

- Visit [Google AI Studio](https://aistudio.google.com/app/api-keys)
- Create or manage your API keys
- Copy your API key for the next step

#### 2. Set Your API Key

**Temporary Setup (Current Session Only):**

```bash
# Mac/Linux
export GEMINI_API_KEY="your_api_key_here"

# Windows (PowerShell)
$env:GEMINI_API_KEY="your_api_key_here"

# Windows (Command Prompt)
set GEMINI_API_KEY=your_api_key_here
```


#### 3. Verify Setup (optional)

Test if your API key is properly configured:

```bash
echo $GEMINI_API_KEY  # Mac/Linux
echo %GEMINI_API_KEY% # Windows CMD
```

### Troubleshooting

- **"API key not found" error:** Ensure the environment variable is set in the current terminal session
- **"Model not found" error:** Verify your API key is valid and has proper permissions
- **Permission errors:** Check that your Google Cloud account has Generative AI API access enabled

## Usage

### Basic Commands

Analyze the current directory:

```bash
insight .
```

Analyze a specific project folder:

```bash
insight /path/to/your/project
```

### Advanced Usage Examples

**Limit files for testing or large projects:**

```bash
insight . --limit 10                    # Analyze only first 10 files
insight ./src --limit 5                 # Analyze first 5 files in src folder
```

**Custom output directories:**

```bash
insight . -o reports                    # Save to 'reports' folder
insight . -o ../analysis_results        # Save to parent directory
insight ./backend -o frontend_analysis  # Analyze backend, save with custom name
```


### Output Structure

After running, you'll find in your output directory:

- `summary.md` - High-level overview of the entire codebase
- Individual `.md` files for each analyzed source file
- Organized analysis with code metrics and AI insights

### Getting Help

```bash
insight --help                          # Show all available options
```

## 📋 Supported File Types

| Category                  | Extensions                                                                                                                                |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Programming Languages** | `.py` `.js` `.ts` `.java` `.cpp` `.c` `.cs` `.go` `.php` `.rb` `.rs` `.swift` `.kt` `.scala` `.dart` `.m` `.mm` `.lua` `.pl` `.sh` `.bat` |
| **Web Development**       | `.html` `.htm` `.css` `.scss` `.less` `.ejs` `.erb` `.mustache`                                                                           |
| **Configuration**         | `.json` `.yaml` `.yml` `.toml` `.ini` `.cfg` `.xml`                                                                                       |
| **Documentation**         | `.md` `.rst`                                                                                                                              |
| **Build & DevOps**        | `.gradle` `.pom` `.makefile` `.cmake` `.dockerfile`                                                                                       |
| **Database**              | `.sql`                                                                                                                                    |

> **Total: 30+ file types supported** for comprehensive codebase analysis


## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Make your changes** and test thoroughly
4. **Commit your changes:** `git commit -m 'Add amazing feature'`
5. **Push to the branch:** `git push origin feature/amazing-feature`
6. **Open a Pull Request**

## 📖 Documentation

- **[INSTRUCTION.md](INSTRUCTION.md)** - Detailed setup and usage guide
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines
- **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** - Community standards

## ⚠️ Known Issues

- Google Cloud warnings may appear (safe to ignore for local development)
- Large codebases may take time to analyze (use `--limit` for testing)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ by the Insight team**

[Report Bug](https://github.com/XplnHUB/Insight-Py/issues) • [Request Feature](https://github.com/XplnHUB/Insight-Py/issues) • [Documentation](INSTRUCTION.md)

</div>
