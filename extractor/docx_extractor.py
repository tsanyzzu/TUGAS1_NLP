# extractor/docx_extractor.py
import re
import docx
from typing import Tuple, List, Dict

def extract_paragraphs_from_docx(path: str) -> Tuple[str, List[Dict]]:
    document = docx.Document(path)
    paragraphs = []
    for para in document.paragraphs:
        text = para.text.strip()
        style_name = getattr(para.style, "name", "") if text else ""
        is_heading = False
        heading_level = None
        if style_name:
            s_lower = style_name.lower()
            m = re.match(r'heading\s*(\d+)', s_lower)
            if m:
                is_heading = True
                heading_level = int(m.group(1))
            elif 'title' in s_lower and text:
                is_heading = True
                heading_level = 1
            elif 'subtitle' in s_lower and text:
                is_heading = True
                heading_level = 2
        paragraphs.append({
            'text': text,
            'style': style_name,
            'is_heading': is_heading,
            'heading_level': heading_level
        })
    full = "\n\n".join([p['text'] for p in paragraphs])
    return full, paragraphs
