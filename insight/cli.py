import argparse
import os
from .analyzer import analyze_codebase
from .reporter import generate_report

def main():
    parser = argparse.ArgumentParser(description="Insight - Codebase Explainer CLI")
    parser.add_argument("path", help="Path to the codebase")
    parser.add_argument("-o", "--output", default="report", help="Output report directory")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of files analyzed")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print("❌ Path not found.")
        return
    
    print("🔍 Analyzing codebase...")
    analysis = analyze_codebase(args.path, limit=args.limit)

    print("📝 Generating reports...")
    generate_report(analysis, args.output)

    print(f"✅ Reports saved in {args.output}/")
