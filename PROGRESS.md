# PROGRESS
Updated: 2026-11-15 07:35
Last completed task: T10.8 — Built and visually verified Slides 13–15 in Google Slides
Current task: T10.9–T10.11 — Footnotes, story test & full thumbnail QA   | status: [~] in progress
Next concrete action: Programmatically audit all `[n]` tags across Slides 1–14 against Slide 15 & `submission/references.txt`, review the 15-title narrative flow, and complete full 15-slide visual QA (`T10.9`–`T10.11`).
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Completed Phases 1–9 (`phase-1-done` through `phase-9-done`). Clean-kernel `Islam-Raad.ipynb` execution runs in `68.83s` with 21 verified matplotlib PNGs and 100% consistent `outputs/results.json`.
- Completed T10.1–T10.4: Verified native `gslides` capabilities, created production deck `"Islam-Raad — GCI Final Assignment"`, tuned and visually verified all 11 slide charts/diagrams (`fig_04`–`fig_13`) at exact 1:1 placement dimensions (`200 DPI`, `>= 10 pt` fonts), and verified direct local PNG upload via `gslides mutate insert-image-from-file`.
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`, `data.churn_count`: `49,562` (`49.562%`).
- `eda.jump_ci`: `260–300d` (`36.85%`) vs `301–340d` (`60.69%`), `+23.83 pp` (`95% CI [+22.12, +25.62] pp`), `months 11`: `64.57%`, `mou_Mean == 0`: `n=1,615` all (`79.81%` all / `n=1,120` train `78.48%`).
- `final_model`: `M5` (`cv_auc_mean`: `0.7020 ± 0.0013`, `test_auc`: `0.7029`, `test_acc`: `0.6409`, `test_brier`: `0.2180`).
- `topk[k=10%]`: `precision=0.8130` (`lift=1.6403`), `precision_rebased_10=0.3296` (`lift=3.2957`), `precision_rebased_5=0.1889` (`lift=3.7775`).
- `impact.scenarios.base_10pct`: `k=10%` Net = `+82,557 MU` (`s* = 9.84%`), `k*=15%` Net = `+90,940 MU`.
- `impact.scenarios.base_5pct`: `k=10%` Net = `+13,160 MU` (`s* = 17.17%`), `k*=4%` Net = `+23,955 MU`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/tables/experiment_log.csv`, `outputs/tables/test_predictions.csv`, `outputs/models/final_xgb_m5_pipeline.joblib`, `outputs/figures/` (21 matplotlib PNGs), `submission/references.txt`
Google Slides: ID `1AoRnogsahX7MrPD5clmipkLutkvfTW_5UuV4rFMhJqA` | URL `https://docs.google.com/presentation/d/1AoRnogsahX7MrPD5clmipkLutkvfTW_5UuV4rFMhJqA/edit`
Open issues / assumptions pending:
- AI chat link placeholders (`[15]`, `[16]`) to be replaced by Islam before submission.
