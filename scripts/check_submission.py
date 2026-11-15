#!/usr/bin/env python3
"""Automated verification script for GCI World 2026 Final Assignment submission.

Checks:
1. PDF page count (<= 15), page dimensions (720 x 405 pts), file size (<= 10 MB).
2. Live selectable text in PDF via pdftotext (Slide 9 model/metric/score, Slide 15 refs, key results.json values).
3. Exact consistency of bracket citations [n] across Slides 1-14 vs Slide 15 vs submission/references.txt vs research/sources_log.md.
4. outputs/results.json completeness and sanity checks.
5. submission/ directory sanity (when --strict-submission is passed: exact 3 deliverables + executed notebook check).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBMISSION_DIR = ROOT / "submission"
PDF_PATH = SUBMISSION_DIR / "Islam-Raad.pdf"
NB_PATH = SUBMISSION_DIR / "Islam-Raad.ipynb"
REFS_PATH = SUBMISSION_DIR / "references.txt"
RESULTS_PATH = ROOT / "outputs" / "results.json"
SOURCES_LOG_PATH = ROOT / "research" / "sources_log.md"


def _expand_bracket_citations(text: str) -> set[int]:
    """Extract numeric citation IDs from bracket groups like [1], [1, 2], [7, 8, 9], or [7-9]."""
    cited: set[int] = set()
    for grp in re.findall(r"\[([0-9,\s\-–]+)\]", text):
        for part in grp.split(","):
            part = part.strip()
            if not part:
                continue
            if "-" in part or "–" in part:
                bounds = re.split(r"[-–]", part)
                if len(bounds) == 2 and bounds[0].strip().isdigit() and bounds[1].strip().isdigit():
                    a, b = int(bounds[0]), int(bounds[1])
                    if b - a <= 20:
                        cited.update(range(a, b + 1))
            elif part.isdigit():
                cited.add(int(part))
    return cited


def check_results_json(errors: list[str], warnings: list[str]) -> dict:
    if not RESULTS_PATH.exists():
        errors.append(f"Missing {RESULTS_PATH}")
        return {}
    data = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
    for key in ("data", "eda", "models", "final_model", "topk", "importance", "fairness", "impact"):
        if key not in data:
            errors.append(f"outputs/results.json missing top-level section '{key}'")
    m5 = next((m for m in data.get("models", []) if m.get("id") == "M5"), None)
    if not m5:
        errors.append("outputs/results.json missing M5 model entry")
    else:
        auc = m5.get("test_auc")
        if auc is None or not (0.69 < auc < 0.72):
            errors.append(f"Unexpected M5 test_auc in results.json: {auc}")
    print(f"[OK] outputs/results.json loaded ({len(data)} sections)")
    return data


def check_pdf(errors: list[str], warnings: list[str], results: dict) -> list[str]:
    if not PDF_PATH.exists():
        errors.append(f"Missing exported PDF: {PDF_PATH}")
        return []

    size_bytes = PDF_PATH.stat().st_size
    size_mb = size_bytes / (1024 * 1024)
    if size_mb > 10.0:
        errors.append(f"PDF size {size_mb:.2f} MB exceeds 10 MB limit")

    info_out = subprocess.check_output(["pdfinfo", str(PDF_PATH)], text=True)
    m_pages = re.search(r"Pages:\s+(\d+)", info_out)
    n_pages = int(m_pages.group(1)) if m_pages else -1
    if n_pages != 15:
        errors.append(f"Expected 15 PDF pages, found {n_pages}")

    m_size = re.search(r"Page size:\s+([\d.]+)\s+x\s+([\d.]+)\s+pts", info_out)
    if m_size:
        pw, ph = float(m_size.group(1)), float(m_size.group(2))
        if abs(pw - 720.0) > 2.0 or abs(ph - 405.0) > 2.0:
            errors.append(f"Unexpected PDF page size {pw}x{ph} pts (expected 720x405)")

    # Extract page-by-page text via pdftotext (form-feed separated)
    raw_txt = subprocess.check_output(["pdftotext", str(PDF_PATH), "-"], text=True)
    pages = raw_txt.split("\f")
    # Drop trailing empty element after final form feed
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    if len(pages) != 15:
        errors.append(f"pdftotext extracted {len(pages)} pages instead of 15")
        return pages

    # Slide 9 live text requirements (PRD §11.8 & T10.14)
    s9 = re.sub(r"\s+", " ", unicodedata.normalize("NFKC", pages[8]))
    for token in ("M5 XGBoost Tuned", "ROC-AUC", "0.7029"):
        if token not in s9:
            errors.append(f"Slide 9 live PDF text missing required token '{token}'")

    # Check key numbers from results.json appear across the PDF
    full_pdf_text = re.sub(r"\s+", " ", unicodedata.normalize("NFKC", "\n".join(pages)))
    expected_tokens = [
        "100,000",
        "49.56%",
        "64.6%",
        "0.703",
        "0.7029",
        "81.3%",
        "3.3×",
        "+82,557",
        "+13,160",
        "9.8%",
    ]
    missing_tokens = [tok for tok in expected_tokens if tok not in full_pdf_text]
    if missing_tokens:
        errors.append(f"PDF text missing expected numbers from results.json: {missing_tokens}")

    print(
        f"[OK] PDF check passed: {n_pages} pages (720x405 pts), {size_mb:.2f} MB, "
        f"Slide 9 live text verified, all key results.json tokens found"
    )
    return pages


def check_references_and_citations(errors: list[str], warnings: list[str], pdf_pages: list[str]) -> None:
    if not REFS_PATH.exists():
        errors.append(f"Missing {REFS_PATH}")
        return
    ref_lines = [line.strip() for line in REFS_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    ref_nums: set[int] = set()
    for idx, line in enumerate(ref_lines, start=1):
        m = re.match(r"^\[(\d+)\]\s+", line)
        if not m or int(m.group(1)) != idx:
            errors.append(f"references.txt line {idx} malformed or misnumbered: {line[:60]}")
        else:
            ref_nums.add(idx)

    # Verify research/sources_log.md lists [1]..[N]
    if not SOURCES_LOG_PATH.exists():
        errors.append(f"Missing {SOURCES_LOG_PATH}")
    else:
        log_text = SOURCES_LOG_PATH.read_text(encoding="utf-8")
        missing_in_log = [n for n in sorted(ref_nums) if f"[{n}]" not in log_text]
        if missing_in_log:
            errors.append(f"research/sources_log.md missing entries for reference IDs: {missing_in_log}")

    if len(pdf_pages) == 15:
        # Compare Slide 15 text against references.txt entries (NFKC + whitespace-normalized)
        s15_norm = re.sub(r"\s+", " ", unicodedata.normalize("NFKC", pdf_pages[14]))
        for line in ref_lines:
            # Check URL/title prefix (first 45 chars normalized + key URL if present)
            prefix = re.sub(r"\s+", " ", line[:45])
            if prefix not in s15_norm:
                errors.append(f"Slide 15 missing or altered reference entry starting with: {prefix}")

        # Collect all [n] tags on Slides 1-14
        cited_1_14 = _expand_bracket_citations("\n".join(pdf_pages[:14]))
        unknown_tags = cited_1_14 - ref_nums
        if unknown_tags:
            errors.append(f"Slides 1-14 contain unknown [n] tags absent from references.txt: {sorted(unknown_tags)}")

        # Check all non-AI refs ([1]..[14]) are cited somewhere on Slides 1-14
        non_ai_refs = {n for n, l in zip(range(1, len(ref_lines) + 1), ref_lines) if "Generative AI" not in l}
        uncited_non_ai = non_ai_refs - cited_1_14
        if uncited_non_ai:
            errors.append(f"Non-AI references not cited on Slides 1-14: {sorted(uncited_non_ai)}")

    print(f"[OK] References check passed: {len(ref_lines)} entries matched across Slide 15, references.txt, and sources_log.md")


def check_submission_folder(
    errors: list[str], warnings: list[str], strict: bool, execute_nb: bool = False
) -> None:
    expected_files = {"Islam-Raad.pdf", "Islam-Raad.ipynb", "references.txt"}
    if not SUBMISSION_DIR.exists():
        errors.append(f"Missing submission directory: {SUBMISSION_DIR}")
        return
    actual_files = {p.name for p in SUBMISSION_DIR.iterdir()}
    extra = actual_files - expected_files
    missing = expected_files - actual_files
    if extra:
        errors.append(f"Extra unexpected items in submission/: {sorted(extra)}")
    if strict and missing:
        errors.append(f"Missing deliverables in submission/: {sorted(missing)}")
    elif missing:
        warnings.append(f"Pending deliverables in submission/ (expected by Phase 13): {sorted(missing)}")

    # Warn if AI placeholders are still unreplaced
    if REFS_PATH.exists():
        txt = REFS_PATH.read_text(encoding="utf-8")
        if "[AI-CHAT-LINK:" in txt:
            warnings.append("submission/references.txt still contains [AI-CHAT-LINK: ...] placeholders (Islam must insert live URLs)")

    if execute_nb and NB_PATH.exists():
        print("[INFO] Executing submission/Islam-Raad.ipynb from submission/ using clean kernel...")
        subprocess.run(
            [
                sys.executable, "-m", "jupyter", "nbconvert",
                "--to", "notebook", "--execute", "--inplace",
                "--ExecutePreprocessor.timeout=600",
                NB_PATH.name,
            ],
            cwd=str(SUBMISSION_DIR),
            check=True,
        )
        post_files = {p.name for p in SUBMISSION_DIR.iterdir()}
        if post_files != expected_files:
            errors.append(f"Executing notebook changed submission/ contents: {sorted(post_files)}")

    if strict and NB_PATH.exists():
        nb_data = json.loads(NB_PATH.read_text(encoding="utf-8"))
        cells = nb_data.get("cells", [])
        code_cells = [c for c in cells if c.get("cell_type") == "code"]
        unexecuted = [i for i, c in enumerate(code_cells) if c.get("execution_count") is None]
        if unexecuted:
            errors.append(f"submission/Islam-Raad.ipynb has unexecuted code cells: {unexecuted[:10]}")
        nb_raw = NB_PATH.read_text(encoding="utf-8")
        if re.search(r"(/home/islam-raad|AIza[0-9A-Za-z_-]{20,}|\bsk-[A-Za-z0-9]{20,}|\bghp_[A-Za-z0-9]{20,})", nb_raw):
            errors.append("submission/Islam-Raad.ipynb contains potential personal path or secret token")
        # Verify notebook outputs contain the same core headline metrics as results.json & PDF
        out_chunks = []
        for c in code_cells:
            for o in c.get("outputs", []):
                if "text" in o:
                    out_chunks.append("".join(o["text"]))
                elif "data" in o and "text/plain" in o["data"]:
                    out_chunks.append("".join(o["data"]["text/plain"]))
        out_text = "\n".join(out_chunks)
        for tok in ("0.7029", "82,557", "13,160", "9.84%", "64.57%"):
            if tok not in out_text:
                errors.append(f"submission/Islam-Raad.ipynb outputs missing key metric '{tok}' (PDF <-> NB sync check)")
        print(f"[OK] Strict notebook check passed: {len(cells)} cells, {len(code_cells)} executed code cells, outputs synced with PDF/results.json")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify GCI Final Assignment deliverables.")
    parser.add_argument(
        "--strict-submission",
        action="store_true",
        help="Require all 3 final deliverables inside submission/ and verify executed notebook.",
    )
    parser.add_argument(
        "--execute-submission-nb",
        action="store_true",
        help="Execute submission/Islam-Raad.ipynb from inside submission/ via clean kernel before checking.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    results = check_results_json(errors, warnings)
    pdf_pages = check_pdf(errors, warnings, results)
    check_references_and_citations(errors, warnings, pdf_pages)
    check_submission_folder(
        errors, warnings, strict=args.strict_submission, execute_nb=args.execute_submission_nb
    )

    for w in warnings:
        print(f"[WARN] {w}")
    for e in errors:
        print(f"[FAIL] {e}")

    if errors:
        print(f"\nVerification FAILED with {len(errors)} problem(s).")
        return 1
    print("\nVerification PASSED: 0 problems.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
