import google.generativeai as genai
import os
import sys
from rich.console import Console
from rich.panel import Panel

console = Console()

def show_error(message):
    console.print(
        Panel.fit(
            f"[bold red]❌ ERROR[/bold red]\n\n{message}",
            border_style="red",
            title="System Message",
            title_align="left"
        )
    )
api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not api_key:
    error_message =''' Error: No API key found. 
    Please set your key using one of the following:
    export GOOGLE_API_KEY='your_key_here'
    setx GOOGLE_API_KEY 'your_key_here'
    '''
    show_error(error_message)
    sys.exit(1)
genai.configure(api_key=api_key)
def explain_code(content: str, filename: str):
    if not content.strip():
        return "File is empty.", 1
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    You are analyzing a code file.
    File: {filename}
    Tasks:
    1. Summarize what this file does in detail.
    2. Mention its key logic (functions, classes, workflows).
    3. Estimate if this code looks AI/LLM-generated.
       - Return a probability score between 1 (definitely human) and 10 (definitely AI).
       - Give a short reasoning.

    Code (truncated if too long):
    {content[:5000]}
    """
    try:
        response = model.generate_content(prompt)
        text = response.text if response else "No explanation generated."
        ai_score = 5

        for num in range(10, 0, -1):
            if str(num) in text:
                ai_score = num
                break
        return text, ai_score
    except Exception as e:
        return f"Gemini API error: {str(e)}", 1
