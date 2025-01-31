import pdfplumber

def extract_text_from_pdf(resume):
    """Extracts text content from the uploaded resume PDF."""
    if not resume:
        return ""

    text_content = ""
    try:
        with pdfplumber.open(resume) as pdf:
            text_content = "\n".join(
                page.extract_text() for page in pdf.pages if page.extract_text()
            )
    except Exception as e:
        text_content = f"Error extracting text: {e}"

    return text_content
