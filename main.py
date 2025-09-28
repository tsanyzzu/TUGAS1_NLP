import sys
from pathlib import Path

# imports from modules
from extractor.pdf_extractor import extract_text_from_pdf
from extractor.docx_extractor import extract_paragraphs_from_docx
from extractor.hierarchy import lines_from_text, build_hierarchy_from_lines, tree_to_markdown
from utils.io_helpers import save_outputs


def process_pdf(path: str):
    text, pages = extract_text_from_pdf(path)
    lines = lines_from_text(text)
    tree = build_hierarchy_from_lines(lines, docx_paragraphs=None)
    md = tree_to_markdown(tree)
    base = Path(path).stem
    return save_outputs(base, md, tree)


def process_docx(path: str):
    full, paragraphs = extract_paragraphs_from_docx(path)
    tree = build_hierarchy_from_lines(None, docx_paragraphs=paragraphs)
    md = tree_to_markdown(tree)
    base = Path(path).stem
    return save_outputs(base, md, tree)


def run_local(files):
    results = []
    for f in files:
        f = str(f)
        if f.lower().endswith('.pdf'):
            results.append(process_pdf(f))
            print(f"Processed PDF: {f}")
        elif f.lower().endswith('.docx'):
            results.append(process_docx(f))
            print(f"Processed DOCX: {f}")
        else:
            print(f"Unsupported file type: {f}")
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        run_local(files)
    else:
        print("Usage: python main.py <file1.pdf> <file2.docx> ...")
