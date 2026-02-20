#!/usr/bin/env python3
"""
build_paysage_combined.py

Rassemble tous les fichiers .py d'un dossier de contributions (ex: "paysage/")
en un seul fichier Python. Le fichier de sortie contient :
 - les imports dédupliqués (en tête),
 - toutes les définitions de fonctions / classes / assignations sûres extraites
   des fichiers sources,
 - un __all__ contenant les noms de fonctions top-level collectés.

Usage :
    python3 scripts/build_paysage_combined.py --src-dir paysage --out-file paysage_combined.py
    # ou pour écrire dans le package (paysage/__init__.py) :
    python3 scripts/build_paysage_combined.py --src-dir paysage --in-package

Remarques :
 - Le script ignore les blocs `if __name__ == "__main__":`.
 - Les appels top-level (ex : dessin au module import) sont détectés et SKIPPÉS :
   ils sont listés en avertissement pour que tu corriges le fichier source.
 - Requiert Python 3.8+ pour la robustesse avec l'AST (end_lineno).
"""
from __future__ import annotations
import ast
import argparse
import os
from pathlib import Path
import sys
from datetime import datetime

def is_main_if(node: ast.If) -> bool:
    cond = node.test
    if isinstance(cond, ast.Compare):
        left = cond.left
        if isinstance(left, ast.Name) and left.id == "__name__":
            for op, comparator in zip(cond.ops, cond.comparators):
                if isinstance(op, ast.Eq):
                    comp = comparator
                    if isinstance(comp, ast.Constant) and comp.value == "__main__":
                        return True
                    if isinstance(comp, ast.Str) and comp.s == "__main__":
                        return True
    return False

def src_segment(src_lines: list[str], node: ast.AST) -> str:
    if not hasattr(node, "lineno"):
        raise ValueError("Node has no lineno")
    start = node.lineno - 1
    end = getattr(node, "end_lineno", node.lineno)
    return "".join(src_lines[start:end])

def collect_from_file(path: Path):
    src = path.read_text(encoding="utf-8")
    src_lines = src.splitlines(keepends=True)
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        print(f"[ERROR] SyntaxError parsing {path}: {e}", file=sys.stderr)
        return {
            "imports": [],
            "bodies": [],
            "func_names": [],
            "skipped_calls": [f"PARSE_ERROR: {e}"],
        }

    imports = []
    bodies = []
    func_names = []
    skipped_calls = []

    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            try:
                snippet = src_segment(src_lines, node)
            except Exception:
                snippet = ast.get_source_segment(src, node) or ""
            imports.append(snippet.rstrip() + "\n")
            continue

        if isinstance(node, ast.If) and is_main_if(node):
            continue

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            try:
                snippet = src_segment(src_lines, node)
            except Exception:
                snippet = ast.get_source_segment(src, node) or ""
            bodies.append(snippet.rstrip() + "\n")
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                func_names.append(node.name)
            continue

        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            try:
                snippet = src_segment(src_lines, node)
            except Exception:
                snippet = ast.get_source_segment(src, node) or ""
            bodies.append(snippet.rstrip() + "\n")
            continue

        if isinstance(node, ast.Expr):
            value = node.value
            if isinstance(value, ast.Call):
                try:
                    snippet = src_segment(src_lines, node).strip()
                except Exception:
                    snippet = ast.get_source_segment(src, node) or "<expr>"
                skipped_calls.append(f"{path.name}: skipped top-level call -> {snippet}")
                continue
            else:
                try:
                    snippet = src_segment(src_lines, node)
                except Exception:
                    snippet = ast.get_source_segment(src, node) or ""
                bodies.append(snippet.rstrip() + "\n")
                continue

        try:
            snippet = src_segment(src_lines, node)
            bodies.append(snippet.rstrip() + "\n")
        except Exception:
            skipped_calls.append(f"{path.name}: skipped unknown top-level node of type {type(node).__name__}")

    return {
        "imports": imports,
        "bodies": bodies,
        "func_names": func_names,
        "skipped_calls": skipped_calls,
    }

def build_combined(src_dir: Path, out_file: Path, keep_order: bool = True):
    src_files = sorted([p for p in src_dir.glob("**/*.py") if p.name != out_file.name and p.name != "__init__.py"],
                       key=lambda p: p.name if keep_order else str(p))
    if not src_files:
        print(f"No .py files found in {src_dir}", file=sys.stderr)
        return 1

    collected_imports = []
    collected_imports_set = set()
    collected_bodies = []
    all_func_names = []
    all_skipped = []

    for path in src_files:
        print("Processing", path)
        info = collect_from_file(path)
        for imp in info["imports"]:
            key = imp.strip()
            if key not in collected_imports_set:
                collected_imports.append(imp.rstrip() + "\n")
                collected_imports_set.add(key)
        if info["bodies"]:
            header = f"\n# --- from {path.name} ---\n"
            collected_bodies.append(header)
            collected_bodies.extend(info["bodies"])
        all_func_names.extend(info["func_names"])
        all_skipped.extend(info["skipped_calls"])

    header = [
        f"# Auto-generated combined module",
        f"# Source folder: {src_dir}",
        f"# Generated: {datetime.utcnow().isoformat()}Z",
        "# NOTE: top-level calls have been skipped. Review warnings printed during generation.",
        "",
    ]
    out_lines = [line + "\n" for line in header]

    if collected_imports:
        out_lines.append("# ---- imports (deduplicated) ----\n")
        out_lines.extend(collected_imports)
        out_lines.append("\n")

    out_lines.append("# ---- collected definitions / assignments ----\n")
    out_lines.extend(collected_bodies)
    out_lines.append("\n")

    public_funcs = sorted(set(all_func_names))
    out_lines.append("# ---- exported names ----\n")
    out_lines.append("__all__ = [\n")
    for name in public_funcs:
        out_lines.append(f"    {name!r},\n")
    out_lines.append("]\n")

    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text("".join(out_lines), encoding="utf-8")
    print(f"Wrote combined module to {out_file}")

    if all_skipped:
        print("\nWARN: Some top-level calls or nodes were skipped (to avoid executing student code at import):", file=sys.stderr)
        for s in all_skipped:
            print(" -", s, file=sys.stderr)
        print("Recommendation: wrap tests/dessin calls in each source with `if __name__ == \"__main__\":`", file=sys.stderr)

    return 0

def main(argv=None):
    parser = argparse.ArgumentParser(description="Combine .py files from a folder into one module.")
    parser.add_argument("--src-dir", "-s", default="paysage", help="Source directory containing student .py files")
    parser.add_argument("--out-file", "-o", default="paysage_combined.py", help="Output combined file path")
    parser.add_argument("--in-package", action="store_true",
                        help="If set, write output into the package as __init__.py (overwrites).")
    args = parser.parse_args(argv)

    src_dir = Path(args.src_dir)
    if not src_dir.exists() or not src_dir.is_dir():
        print(f"Source directory not found: {src_dir}", file=sys.stderr)
        return 2

    out_path = Path(args.out_file)
    if args.in_package:
        out_path = src_dir / "__init__.py"

    return build_combined(src_dir, out_path)

if __name__ == "__main__":
    raise SystemExit(main())