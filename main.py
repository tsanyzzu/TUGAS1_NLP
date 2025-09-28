# main.py
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

def run_colab():
    # this function intended for Google Colab usage
    try:
        from google.colab import files as colab_files
        from IPython.display import FileLink, display
    except Exception as e:
        raise RuntimeError("run_colab() only works in Google Colab environment") from e

    uploaded = colab_files.upload()
    results = {}
    for fn in uploaded.keys():
        print(f"Processing: {fn}")
        if fn.lower().endswith('.pdf'):
            md_path, json_path = process_pdf(fn)
        elif fn.lower().endswith('.docx'):
            md_path, json_path = process_docx(fn)
        else:
            print(f"Skipping unsupported file: {fn}")
            continue
        results[fn] = (md_path, json_path)
        display(FileLink(md_path))
        display(FileLink(json_path))
    return results

if _name_ == '_main_':
    if len(sys.argv) > 1:
        # CLI mode: pass file paths as arguments
        files = sys.argv[1:]
        run_local(files)
    else:
        print("No arguments provided. To run in Colab, import run_colab() and call it from a Colab cell.")
