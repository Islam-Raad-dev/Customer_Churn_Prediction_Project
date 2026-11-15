# PROGRESS
Updated: 2026-11-15 07:10
Last completed task: T10.1 — Capability probe of Google Slides integration
Current task: T10.2 — Create presentation "Islam-Raad — GCI Final Assignment"   | status: [~] in progress
Next concrete action: Create presentation "Islam-Raad — GCI Final Assignment" via `gslides`, confirm `720 × 405 pt` canvas, build reusable layout helpers for PRD §11.2–11.4, record URL/ID in `PROGRESS.md` and `docs/NOTES.md`, then confirm `T10.3`–`T10.4` figure readiness and build Slides 1–4 (`T10.5`).
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Completed Phases 1–9 (`phase-1-done` through `phase-9-done`). Clean-kernel `Islam-Raad.ipynb` execution runs in `68.83s` with 21 verified matplotlib PNGs and 100% consistent `outputs/results.json`.
- Completed T10.1 capability probe on `gslides` CLI (`cl/986250228`, signed in): verified native `create`, exact 16:9 `720 × 405 pt` canvas, `batch` (shapes, textboxes, native live-text tables, Montserrat/Open Sans fonts, notes), `insert-image-from-file` (local 200-DPI PNG upload/embedding without separate Drive sharing steps), `export-thumbnail`, and `export --format pdf` with live `pdftotext` output. No `python-pptx` fallback needed; documented in `docs/NOTES.md → 7. Slides`.
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.churn_count`: `49,562` (`49.562%`), `data.stayed_count`: `50,438` (`50.438%`), `data.imbalance_ratio`: `1.0177`.
- `eda.device_age_summary`: train `<=300d` churn `39.40%` (`n=28,131`) vs `>300d` churn `56.39%` (`n=41,868`, `+16.99 pp`).
- `eda.jump_ci`: `260–300d` (`36.85%`) vs `301–340d` (`60.69%`), `+23.83 pp` (`95% CI [+22.12, +25.62] pp`), local linear jump `+23.22 pp`, `months >= 10` jump `+19.46 pp`.
- `eda.tenure_summary`: month 9 `29.25%` $\rightarrow$ month 10 `40.18%` $\rightarrow$ month 11 `64.57%` $\rightarrow$ month 12 `61.49%` $\rightarrow$ `37+` months `47.15%`.
- `eda.zero_usage`: `mou_Mean == 0` has `n=1,120` train (`1,600` all), churn `78.48%` (`79.81%` all), mean `rev_Mean = 22.89 MU` (`0.62%` revenue share).
- `final_model`: `M5` (`cv_auc_mean`: `0.7020 ± 0.0013`, `test_auc`: `0.7029`, `test_acc`: `0.6409`, `test_precision`: `0.6382`, `test_recall`: `0.6360`, `test_f1`: `0.6371`, `test_brier`: `0.2180`).
- `topk[k=10%]`: `precision=0.8130` (`lift=1.6403`), `precision_rebased_10=0.3296` (`lift=3.2957`), `precision_rebased_5=0.1889` (`lift=3.7775`).
- `impact.scenarios.base_10pct`: `k=10%` Net = `+82,557 MU` (`s* = 9.84%`), `k*=15%` Net = `+90,940 MU`.
- `impact.scenarios.base_5pct`: `k=10%` Net = `+13,160 MU` (`s* = 17.17%`), `k*=4%` Net = `+23,955 MU`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/tables/experiment_log.csv`, `outputs/tables/test_predictions.csv`, `outputs/models/final_xgb_m5_pipeline.joblib`, `outputs/figures/` (21 matplotlib PNGs), `submission/references.txt`
Google Slides: probe verified (`1szrYGBAw5OcdDkLU3KIQFBlib_DtrRg_qrCEIMJ4NJQ`); production deck pending T10.2
Open issues / assumptions pending:
- AI chat link placeholders (`[15]`, `[16]`) to be replaced by Islam before submission.
