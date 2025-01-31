import os

from openai import OpenAI


def open_ai_llm_summarizer(resume_content):
    """Uses LLM to extract applicant name and generate a summary."""
    api_key = os.getenv("OPENAI_API_KEY")
    system_prompt = (
        "You are an AI assistant that extracts structured information from resumes. "
        "Return the applicant's name (if detected) and generate a concise summary."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": resume_content},
    ]

    openai = OpenAI(api_key=api_key)
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)

    extracted_text = response.choices[0].message.content

    # Simple Parsing: Assume LLM returns name and summary as structured text
    name, summary = (
        extracted_text.split("\n", 1)
        if "\n" in extracted_text
        else ("Unknown", extracted_text)
    )

    return name, summary
