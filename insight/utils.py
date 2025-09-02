import os

SUPPORTED_EXTS = (
    ".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".c", ".cpp", ".cs",
    ".go", ".rb", ".php", ".rs", ".swift", ".kt", ".scala", ".dart",
    ".m", ".mm", ".sh", ".bat", ".pl", ".lua",
    ".html", ".htm", ".css", ".scss", ".less", ".ejs", ".erb", ".mustache",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".xml",
    ".md", ".rst", ".sql", ".gradle", ".pom", ".makefile", ".cmake", ".dockerfile"
)

IGNORED_DIRS = {"venv", "node_modules", "__pycache__", ".git", "dist", "build"}

def list_source_files(path):
    """Yield all supported source files in a directory, skipping ignored dirs."""
    if os.path.isfile(path):
        yield path
        return

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]  # skip heavy dirs
        for file in files:
            for ext in SUPPORTED_EXTS:
                if file.lower().endswith(ext) or file.lower() == ext.strip("."):
                    yield os.path.join(root, file)
