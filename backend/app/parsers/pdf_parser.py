from pathlib import Path
from pypdf import PdfReader

def extract_text_from_pdf(file_path: Path | str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        file_path (Path | str): The path to the PDF file."""

    reader = PdfReader(file_path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages).strip()