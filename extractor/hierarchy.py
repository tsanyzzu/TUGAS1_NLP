import csv
import re
from typing import List, Tuple, Dict, Optional, Any
from collections import defaultdict

NUMBERING_PATTERN = re.compile(
    r'^(?P<label>(?:BAB\s+(?:[IVXLC]+|\d+))|(?:\d+(?:\.\d+)*))[\.\)]?\s+(?P<title>[A-Za-z].+)$',
    re.I
)

ROMAN_PATTERN = re.compile(
    r'^(?P<label>[IVXLC]+)[\.\)]?\s+(?P<title>[A-Za-z].+)$',
    re.I
)

def classify_line_heading(line: str) -> Tuple[bool, Optional[int], Optional[str]]:
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
    if m:
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

    # ALLCAPS short
    if s.isupper() and 1 <= len(s.split()) <= 8:
        return True, 1, s

    # Title Case short with colon
    if re.match(r'^[A-Z][\w\s]{0,60}:?$', s) and len(s.split()) <= 6:
        return True, 2, s.rstrip(':')

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

# -------------------------
# builder for extractor rows
# -------------------------
def build_hierarchy_from_extractor(rows: List[Dict[str, Any]]) -> Dict:
    """
    Builds hierarchy tree from extractor output (list of row dicts).
    Strategy:
      - For each row, try text-pattern detection (classify_line_heading).
      - If not detected, consult font-size mapping: bigger fonts -> likely headings.
      - Uppercase short lines with larger fonts are treated as headings.
      - Fallback: append to current node content.
    Returns a root dict similar to your original build_hierarchy_from_lines.
    """
    root = {'title': 'DOCUMENT', 'level': 0, 'content': '', 'children': []}
    stack = [root]

    if not rows:
        return root

    size_map = build_font_size_map(rows)  # size -> rank (1 = largest)
    # handle case where sizes are many: compress ranks to a max depth (optional)
    # but keep as-is for now.

    for r in rows:
        raw = (r.get('text') or '').strip()
        if raw == '':
            # blank line; treat as paragraph break
            # do nothing (or could add newline)
            continue

        # first, try text-based classifier
        ok, level_text, title_text = classify_line_heading(raw)
        if ok:
            level = level_text if level_text is not None else 1
            title = title_text or raw
            # normalize level to int >=1
            level = max(1, int(level))
            node = {'title': title, 'level': level, 'content': '', 'children': []}
            while stack and stack[-1]['level'] >= level:
                stack.pop()
            stack[-1]['children'].append(node)
            stack.append(node)
            continue

        # second, try font-size heuristic
        size = float(r.get('size') or 0.0)
        font_rank = size_map.get(size)
        # If we have font_rank and it's small (i.e., 1 or 2), treat as heading
        # Map font_rank -> level: font_rank 1 => level 1, 2 => level 2, etc.
        # But avoid misclassifying tiny uppercase words: require some heuristics
        treat_as_heading = False
        inferred_level = None
        if font_rank is not None:
            # If this line's font is among the top 3 sizes on the page/doc, consider heading
            if font_rank <= 3:
                # if text is short, uppercase, or ends with colon, it's more likely a heading
                if len(raw.split()) <= 8 or raw.isupper() or raw.endswith(':'):
                    treat_as_heading = True
                    inferred_level = font_rank
                else:
                    # longer lines with large fonts: still maybe heading
                    treat_as_heading = True
                    inferred_level = font_rank

        # Additional heuristic: if the text is ALLCAPS and relatively short, promote to heading
        if not treat_as_heading and raw.isupper() and 1 <= len(raw.split()) <= 10:
            treat_as_heading = True
            inferred_level = inferred_level or 1

        if treat_as_heading:
            level = max(1, int(inferred_level or 1))
            title = raw
            node = {'title': title, 'level': level, 'content': '', 'children': []}
            while stack and stack[-1]['level'] >= level:
                stack.pop()
            stack[-1]['children'].append(node)
            stack.append(node)
            continue

        # otherwise append text to current node's content
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
        if node['title'] and node['title'] != 'DOCUMENT':
            # depth 1 -> '#', depth 2 -> '##', etc.
            header = '#' * depth + ' ' + node['title'] if depth > 0 else '# ' + node['title']
            lines.append(header)
        if node.get('content'):
            lines.append(node['content'].strip())
            lines.append('')
        for c in node.get('children', []):
            emit(c, depth+1)
    for child in tree.get('children', []):
        emit(child, depth=1)
    return '\n'.join(lines).strip()
