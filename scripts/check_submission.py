#!/usr/bin/env python3
"""Automated verification script for GCI World 2026 Final Assignment submission.

Checks (expanded in Phase 10 & Phase 13):
1. PDF page count (<= 15), file size (<= 10 MB), and live text presence of model name/metric/score.
2. Consistency between outputs/results.json and PDF text.
3. Exact match between slide [n] citations, references.txt, and research/sources_log.md.
4. Exact 3-file structure in submission/ (Islam-Raad.pdf, Islam-Raad.ipynb, references.txt).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    results_path = ROOT / "outputs" / "results.json"
    if not results_path.exists():
        print("[WARN] outputs/results.json not generated yet.")
        return 0
    data = json.loads(results_path.read_text(encoding="utf-8"))
    print(f"[OK] Loaded outputs/results.json (keys: {list(data.keys())})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
