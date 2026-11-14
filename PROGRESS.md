# PROGRESS
Updated: 2026-11-14 19:55
Last completed task: T0.5 — Load and merge
Current task: T0.6 — Reproduce the tutorial baseline exactly   | status: [~] in progress (running tutorial XGBClassifier baseline)
Next concrete action: Run the exact tutorial baseline (`LabelEncoder` on object columns + `XGBClassifier(n_estimators=300, learning_rate=0.05, max_depth=6, eval_metric='logloss', random_state=42)` on stratified 70/30 split with `seed=42`), add to `Islam-Raad.ipynb`, and record metrics in `outputs/results.json`.
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Logged matplotlib font fallback (`DejaVu Sans`) and pinned `python3` Jupyter kernelspec to `/home/islam-raad/ai_workspace/bin/python3.12`.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.id_min`–`id_max`: `1,000,001`–`1,100,000`.
- `data.months_min` / `median` / `max`: `6` / `16.0` / `61`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders to be replaced by Islam before submission.
