import pdfplumber
import csv
from typing import List, Dict
from pathlib import Path

def clean_lines(lines: List[Dict], y_tol: float = 5.0) -> List[Dict]:
    cleaned = []
    i = 0
    while i < len(lines):
        current = lines[i]
        if not current["text"].strip():
            i += 1
            continue
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if not nxt["text"].strip():
                j += 1
                continue
            if abs(current["y0"] - nxt["y1"]) < y_tol:
                current["text"] = current["text"].rstrip() + " " + nxt["text"].lstrip()
                current["x0"] = min(current["x0"], nxt["x0"])
                current["x1"] = max(current["x1"], nxt["x1"])
                current["y0"] = min(current["y0"], nxt["y0"])
                current["y1"] = max(current["y1"], nxt["y1"])
                j += 1
            else:
                break
        cleaned.append(current)
        i = j
    return cleaned

def join_with_spacing(chars, space_threshold=1.0):
    text = ""
    for i, ch in enumerate(chars):
        if i > 0:
            prev = chars[i-1]
            # kalau jarak antar karakter cukup besar → tambahkan spasi
            gap = ch["x0"] - prev["x1"]
            if gap > space_threshold:
                text += " "
        text += ch["text"]
    return text

def extract_chars_to_csv(pdf_path: str):
    # otomatis bikin nama csv
    base = Path(pdf_path).stem
    csv_path = f"{base}_lines.csv"

    with pdfplumber.open(pdf_path) as pdf, open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["page", "line_num", "text", "fontname", "size", "x0", "x1", "y0", "y1"])

        for page_num, page in enumerate(pdf.pages, start=1):
            chars: List[Dict] = page.chars
            chars = sorted(chars, key=lambda c: (-c["y0"], c["x0"]))

            lines: List[List[Dict]] = []
            current_line: List[Dict] = []
            last_y = None
            tol = 2
            for c in chars:
                if last_y is None or abs(c["top"] - last_y) <= tol:
                    current_line.append(c)
                else:
                    lines.append(current_line)
                    current_line = [c]
                last_y = c["top"]
            if current_line:
                lines.append(current_line)

            line_dicts: List[Dict] = []
            for line_num, line in enumerate(lines, start=1):
                text = join_with_spacing(line)
                if not text.strip():
                    continue
                fontname = line[0]["fontname"]
                size = line[0]["size"]
                x0 = min(ch["x0"] for ch in line)
                x1 = max(ch["x1"] for ch in line)
                y0 = min(ch["y0"] for ch in line)
                y1 = max(ch["y1"] for ch in line)
                line_dicts.append({
                    "page": page_num,
                    "line_num": line_num,
                    "text": text,
                    "fontname": fontname,
                    "size": size,
                    "x0": x0,
                    "x1": x1,
                    "y0": y0,
                    "y1": y1,
                })

            cleaned = clean_lines(line_dicts)
            for idx, r in enumerate(cleaned, start=1):
                writer.writerow([
                    r["page"], idx, r["text"], r["fontname"], r["size"],
                    r["x0"], r["x1"], r["y0"], r["y1"]
                ])

    return csv_path  # cukup return csv_path
