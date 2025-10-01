import re
from typing import List, Tuple, Dict, Optional

import re

NUMBERING_PATTERN = re.compile(
    r'^(?P<label>(?:BAB\s+(?:[IVXLC]+|\d+))|(?:\d+(?:\.\d+)*))[\.\)]?\s+(?P<title>[A-Za-z].+)$',
    re.I
)

ROMAN_PATTERN = re.compile(
    r'^(?P<label>[IVXLC]+)[\.\)]?\s+(?P<title>[A-Za-z].+)$',
    re.I
)


def lines_from_text(text: str) -> List[str]:
    raw_lines = text.splitlines()
    lines = []
    for ln in raw_lines:
        s = ln.rstrip()
        if s.strip() == '':
            lines.append('')
        else:
            lines.append(s)
    return lines

def classify_line_heading(line: str) -> Tuple[bool, Optional[int], Optional[str]]:
    s = line.strip()
    if not s:
        return False, None, None

    m_bab = re.match(r'^(BAB)\s+(?P<num>(?:[IVXLC]+|\d+))\b(?:[\.\)]\s*)?(?P<rest>.*)$', s, re.I)
    if m_bab:
        title = s
        return True, 1, title

    if re.match(r'^\d+\.\s', s):
        return False, None, None

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

    m2 = ROMAN_PATTERN.match(s)
    if m2:
        title = m2.group('title').strip() or m2.group('label')
        return True, 1, title

    if s.isupper() and 1 <= len(s.split()) <= 8:
        return True, 1, s

    if re.match(r'^[A-Z][\w\s]{0,60}:?$', s) and len(s.split()) <= 6:
        return True, 2, s.rstrip(':')

    return False, None, None

def build_hierarchy_from_lines(lines: Optional[List[str]], docx_paragraphs=None) -> Dict:
    root = {'title': 'DOCUMENT', 'level': 0, 'content': '', 'children': []}
    stack = [root]
    if docx_paragraphs is not None:
        for p in docx_paragraphs:
            text = p['text']
            if not text:
                continue
            if p['is_heading'] and p['heading_level'] is not None:
                level = p['heading_level']
                node = {'title': text, 'level': level, 'content': '', 'children': []}
                while stack and stack[-1]['level'] >= level:
                    stack.pop()
                stack[-1]['children'].append(node)
                stack.append(node)
            else:
                ok, level, title = classify_line_heading(text)
                if ok:
                    node = {'title': title, 'level': level, 'content': '', 'children': []}
                    while stack and stack[-1]['level'] >= level:
                        stack.pop()
                    stack[-1]['children'].append(node)
                    stack.append(node)
                else:
                    cur = stack[-1]
                    if cur['content']:
                        cur['content'] += '\n' + text
                    else:
                        cur['content'] = text
        return root
    else:
        i = 0
        n = len(lines or [])
        while i < n:
            line = (lines[i] or '').strip()
            if not line:
                i += 1
                continue
            ok, level, title = classify_line_heading(line)
            if ok:
                node = {'title': title, 'level': level, 'content': '', 'children': []}
                while stack and stack[-1]['level'] >= level:
                    stack.pop()
                stack[-1]['children'].append(node)
                stack.append(node)
                i += 1
                continue
            else:
                cur = stack[-1]
                if cur['content']:
                    cur['content'] += '\n' + line
                else:
                    cur['content'] = line
                i += 1
        return root

def tree_to_markdown(tree: Dict) -> str:
    lines = []
    def emit(node: Dict, depth: int = 0):
        if node['title'] and node['title'] != 'DOCUMENT':
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
