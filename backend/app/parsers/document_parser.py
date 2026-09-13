from pathlib import Path

from .docx_parser import extract_text_from_docx
from .pdf_parser import extract_text_from_pdf

SUPPORTED_EXTENSIONS = {
    ".docx",
    ".pdf",
}

def extract_text(file_path: Path | str) -> str:
    """
    Extracts text from a file based on its extension.

    Args:
        file_path (Path | str): The path to the file."""

    file_path = Path(file_path)

    extension = file_path.suffix.lower()

    if extension == ".docx":
        return extract_text_from_docx(file_path)

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    raise ValueError(
        f"Unsupported extension used: {extension}," 
        f"supported extensions are: {SUPPORTED_EXTENSIONS}"
    )