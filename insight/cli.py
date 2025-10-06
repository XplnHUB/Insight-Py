import argparse
import os
import re
import pathlib
from .analyzer import analyze_codebase
from .reporter import generate_report

def get_version():
    here = pathlib.Path(__file__).parent.parent
    setup_py = here / "setup.py"
    with open(setup_py, "r") as f:
        content = f.read()
        match = re.search(r"version=\"(.*?)\"", content)
        if match:
            return match.group(1)
    return "0.0.0"

def main():
    parser = argparse.ArgumentParser(description="Insight - Codebase Explainer CLI")
    parser.add_argument("--version", action="version", version=f"%(prog)s {get_version()}")
    parser.add_argument("path", help="Path to the codebase")
    parser.add_argument("-o", "--output", default="report", help="Output report directory")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of files analyzed")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"❌ Error: Path '{args.path}' not found.")
        print(f"   • Current directory: {os.getcwd()}")
        return
    
    print("Analyzing codebase...")
    analysis = analyze_codebase(args.path, limit=args.limit)

    print("Generating reports...")
    generate_report(analysis, args.output)

    print(f"Reports saved in {args.output}/")
