import csv
import re
from typing import List, Tuple, Dict, Optional, Any
from collections import defaultdict

NUMBERING_PATTERN = re.compile(
    r'^(?P<label>(?:BAB\s+(?:[IVXLC]+|\d+))|(?:\d+(?:\.\d+)*))[\.\)]?\s+(?P<title>[A-Z][A-Za-z].+)$'
)

ROMAN_PATTERN = re.compile(
    r'^(?P<label>[IVXLC]+)[\.\)]?\s+(?P<title>[A-Za-z].+)$',
    re.I
)

def classify_line_heading(line: str, size: float = None) -> Tuple[bool, Optional[int], Optional[str]]:
    s = line.strip()
    if not s:
        return False, None, None

    # BAB format
    m_bab = re.match(r'^(BAB)\s+(?P<num>(?:[IVXLC]+|\d+))\b(?:[\.\)]\s*)?(?P<rest>.*)$', s, re.I)
    if m_bab:
        title = s
        return True, 1, title

    # ignore simple numbered list
    if re.match(r'^\d+\.\s', s):
        return False, None, None

    # matches BAB/1.1 style
    m = NUMBERING_PATTERN.match(s)
    if m and size >12:
        label = m.group('label').strip()
        raw_title = m.group('title').strip() or label
        title = f"{label} {raw_title}"
        if label.upper().startswith('BAB') or re.match(r'^[IVXLC]+$', label.strip(), re.I):
            level = 1
        else:
            level = label.count('.') + 1 if '.' in label else 1
        return True, level, title

    # matches "IV. something"
    m2 = ROMAN_PATTERN.match(s)
    if m2:
        title = m2.group('title').strip() or m2.group('label')
        return True, 1, title

    # NEW RULE: ALLCAPS ... dots ... page number
    m3 = re.match(r'^([A-Z\s]+?)\s?\.{3,}\s+([ivxlcdmIVXLCDM\d]+)$', s)
    if m3:
        title = m3.group(1).strip()
        return True, 1, title

    # ALLCAPS short, font size > 12
    if s.isupper() and 1 <= len(s.split()) <= 8 and (size > 12):
        return True, 1, s

    return False, None, None


# -------------------------
# read CSV produced by your extractor
# -------------------------
def read_lines_from_csv(csv_path: str) -> List[Dict[str, Any]]:
    """
    Reads CSV created by extract_chars_to_csv and returns a list of dicts:
      {'page': int, 'line_num': int, 'text': str, 'fontname': str, 'size': float, 'x0': float, ...}
    Assumes CSV header row present and columns named at least: page,line_num,text,fontname,size
    """
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                page = int(r.get("page", r.get("Page", 0)) or 0)
            except ValueError:
                page = 0
            try:
                line_num = int(r.get("line_num", r.get("line", r.get("Line", 0))) or 0)
            except ValueError:
                line_num = 0
            # parse numeric fields safely
            def to_float(k):
                try:
                    return float(r.get(k, "") or 0.0)
                except Exception:
                    return 0.0
            size = to_float("size")
            x0 = to_float("x0"); x1 = to_float("x1"); y0 = to_float("y0"); y1 = to_float("y1")
            text = (r.get("text") or r.get("Text") or "").rstrip("\n")
            rows.append({
                "page": page,
                "line_num": line_num,
                "text": text,
                "fontname": r.get("fontname") or r.get("FontName") or "",
                "size": size,
                "x0": x0, "x1": x1, "y0": y0, "y1": y1
            })
    # ensure ordering by page then line_num (same order extractor used)
    rows.sort(key=lambda e: (e["page"], e["line_num"]))
    return rows

# -------------------------
# font-size based heuristics
# -------------------------
def build_font_size_map(rows: List[Dict[str, Any]]) -> Dict[float, int]:
    """
    Create a map from font-size to rank-level:
      largest size -> rank 1 (likely top heading), next -> 2, ...
    Returns dict size->rank
    """
    sizes = sorted({r['size'] for r in rows if r['size'] > 0}, reverse=True)
    size_to_rank = {s: idx+1 for idx, s in enumerate(sizes)}
    return size_to_rank

def build_hierarchy_from_extractor(rows: List[Dict[str, Any]]) -> Dict:
    root = {'title': 'DOCUMENT', 'level': 0, 'content': '', 'children': []}
    stack = [root]

    if not rows:
        return root

    size_map = build_font_size_map(rows)

    for r in rows:
        raw = (r.get('text') or '').strip()
        if raw == '':
            continue

        size = float(r.get('size') or 0.0)

        # --- cek pakai classifier regex rules ---
        ok, level_text, title_text = classify_line_heading(raw, size)
        if ok:
            level = max(1, int(level_text or 1))
            node = {
                'title': title_text or raw,   # normalized version
                'raw': raw,                   # simpan teks asli
                'level': level,
                'content': '',
                'children': []
            }
            while stack and stack[-1]['level'] >= level:
                stack.pop()
            stack[-1]['children'].append(node)
            stack.append(node)
            continue

        # --- heuristik font ---
        font_rank = size_map.get(size)
        treat_as_heading = False
        inferred_level = None

        if font_rank is not None and font_rank <= 3:
            treat_as_heading = True
            inferred_level = font_rank

        # kalau ALLCAPS pendek tapi font kecil → jangan jadi heading
        if raw.isupper() and len(raw.split()) <= 10 and size > 12:
            treat_as_heading = True
            inferred_level = inferred_level or 1

        if treat_as_heading:
            node = {
                'title': raw,
                'raw': raw,
                'level': max(1, inferred_level or 1),
                'content': '',
                'children': []
            }
            while stack and stack[-1]['level'] >= node['level']:
                stack.pop()
            stack[-1]['children'].append(node)
            stack.append(node)
            continue

        # --- isi biasa ---
        cur = stack[-1]
        if cur['content']:
            cur['content'] += '\n' + raw
        else:
            cur['content'] = raw

    return root

# -------------------------
# optional wrapper: read CSV and build tree directly
# -------------------------
def build_hierarchy_from_csv(csv_path: str) -> Dict:
    rows = read_lines_from_csv(csv_path)
    tree = build_hierarchy_from_extractor(rows)
    return tree

# -------------------------
# tree -> markdown (kept your original behaviour, slight safe-guards)
# -------------------------
def tree_to_markdown(tree: Dict) -> str:
    lines: List[str] = []
    def emit(node: Dict, depth: int = 0):
        if node.get('raw') and node['title'] != 'DOCUMENT':
            # gunakan raw (tampilan asli) untuk heading
            header = '#' * depth + ' ' + node['raw'] if depth > 0 else '# ' + node['raw']
            lines.append(header)
        if node.get('content'):
            lines.append(node['content'].strip())
            lines.append('')
        for c in node.get('children', []):
            emit(c, depth+1)
    for child in tree.get('children', []):
        emit(child, depth=1)
    return '\n'.join(lines).strip()
