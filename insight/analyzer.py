import ast
import os
from .detector import explain_code
from .utils import list_source_files

def extract_code_stats(file_path, content):
    """Extract basic static analysis stats."""
    stats = {
        "functions": 0,
        "classes": 0,
        "imports": [],
        "comments": 0
    }

    # Count comments
    stats["comments"] = sum(1 for line in content.splitlines() if line.strip().startswith("#"))

    # For Python files → use AST parsing
    if file_path.endswith(".py"):
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    stats["functions"] += 1
                elif isinstance(node, ast.ClassDef):
                    stats["classes"] += 1
                elif isinstance(node, ast.Import):
                    stats["imports"].extend(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom):
                    stats["imports"].append(node.module)
        except Exception:
            pass  # ignore parsing errors

    return stats

def analyze_file(file_path):
    with open(file_path, "r", errors="ignore") as f:
        content = f.read()

    lines = content.splitlines()
    preview = lines[:30]

    # Extract static stats
    stats = extract_code_stats(file_path, content)

    # Ask Gemini for explanation + AI probability score
    explanation, ai_score = explain_code(content, file_path)

    return {
        "file": file_path,
        "total_lines": len(lines),
        "preview": preview,
        "explanation": explanation,
        "functions": stats["functions"],
        "classes": stats["classes"],
        "imports": stats["imports"],
        "comments": stats["comments"],
        "ai_score": ai_score  # 1–10 scale
    }

def analyze_codebase(path, limit=None):
    results = []
    files = list(list_source_files(path))
    total_files = len(files)

    for idx, file_path in enumerate(files, start=1):
        if limit and idx > limit:
            break
        print(f"🔎 Processing {idx}/{total_files}: {file_path}")
        results.append(analyze_file(file_path))

    return results
