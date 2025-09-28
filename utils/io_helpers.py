# utils/io_helpers.py
import json
from pathlib import Path
from typing import Tuple, Dict

def save_outputs(base_name: str, md_text: str, tree: Dict) -> Tuple[str, str]:
    md_path = f"{base_name}_structured.md"
    json_path = f"{base_name}_structured.json"
    Path(md_path).write_text(md_text, encoding='utf-8')
    Path(json_path).write_text(json.dumps(tree, ensure_ascii=False, indent=2), encoding='utf-8')
    return md_path, json_path
