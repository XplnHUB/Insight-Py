import os

def save_file_report(file_info, output_dir):
    filename = os.path.basename(file_info["file"]) + ".md"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w") as f:
        f.write(f"# Report for `{file_info['file']}`\n\n")
        f.write(f"- **Total lines:** {file_info['total_lines']}\n")
        f.write(f"- **File type:** {os.path.splitext(file_info['file'])[1]}\n\n")

        f.write("## Explanation\n")
        f.write(file_info["explanation"] + "\n\n")

        f.write("## Code Preview (first 30 lines)\n")
        code_preview = "\n".join(file_info.get("preview", []))
        f.write("```text\n" + code_preview + "\n```\n")

def generate_report(analysis, output_dir="report"):
    os.makedirs(output_dir, exist_ok=True)

    for file_info in analysis:
        save_file_report(file_info, output_dir)

    summary_path = os.path.join(output_dir, "summary.md")
    total_lines = sum(f["total_lines"] for f in analysis)

    with open(summary_path, "w") as f:
        f.write("# Insight Codebase Summary\n\n")
        f.write(f"**Total files analyzed:** {len(analysis)}\n")
        f.write(f"**Total lines of code:** {total_lines}\n\n")
        f.write("## Files Included\n")
        for file_info in analysis:
            short_name = os.path.basename(file_info["file"])
            f.write(f"- [{short_name}]({short_name}.md) ({file_info['total_lines']} lines)\n")
