from __future__ import annotations
from pathlib import Path
import os
import re

REPO_ROOT = Path(os.getenv("CREW_REPO_ROOT", Path.cwd())).resolve()

def _safe_path(path: str) -> Path:
    # Normaliser les chemins qui commencent par / pour les traiter comme relatifs
    # Par exemple /docs/SPECS.md devient docs/SPECS.md
    if path.startswith("/") and not path.startswith("//"):
        path = path.lstrip("/")
    p = (REPO_ROOT / path).resolve()
    if not str(p).startswith(str(REPO_ROOT)):
        raise ValueError("Path outside repo root is not allowed.")
    return p

def read_file(path: str) -> str:
    p = _safe_path(path)
    return p.read_text(encoding="utf-8")

def write_file(path: str, content: str) -> str:
    p = _safe_path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return f"Wrote {len(content)} chars to {path}"

def list_tree(path: str = ".", max_depth: int = 4) -> str:
    base = _safe_path(path)
    lines = []
    base_depth = len(base.parts)
    for p in sorted(base.rglob("*")):
        depth = len(p.parts) - base_depth
        if depth <= max_depth:
            rel = p.relative_to(REPO_ROOT)
            lines.append(str(rel) + ("/" if p.is_dir() else ""))
    return "\n".join(lines)

def apply_patch(patch: str) -> str:
    """
    Very small git-style patch applier (supports only unified diffs for add/replace whole files).
    For reliability: agents should prefer write_file for full files, or patch only when needed.
    """
    # Minimal: detect "+++ b/<path>" then write the content after "@@"
    # In practice: we keep it simple and encourage full-file writes.
    m = re.search(r"\+\+\+ b/(.+)", patch)
    if not m:
        raise ValueError("Patch missing '+++ b/<path>' header.")
    target = m.group(1).strip()
    # naive extract all lines that start with '+' (excluding headers) as new content is not safe;
    # so we require patch contains a marker block:
    marker = "\n*** FILE_CONTENT_START ***\n"
    if marker not in patch:
        raise ValueError("Patch must include FILE_CONTENT_START marker.")
    content = patch.split(marker, 1)[1]
    return write_file(target, content)
