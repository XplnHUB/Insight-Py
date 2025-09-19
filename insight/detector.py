import google.generativeai as genai
import os
import sys
api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: No API key found.")
    print("Please set your key using one of the following:")
    print("  export GOOGLE_API_KEY='your_key_here'")
    print("  setx GOOGLE_API_KEY 'your_key_here'")
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
