import pdfplumber
from typing import Tuple, List

def extract_text_from_pdf(path: str) -> Tuple[str, List[str]]:
    pages = []
    with pdfplumber.open(path) as pdf:
        for p in pdf.pages:
            text = p.extract_text() or ''
            pages.append(text)
    full = "\n\n".join(pages)
    return full, pages