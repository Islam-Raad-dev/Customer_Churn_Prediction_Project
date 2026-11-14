# PROGRESS
Updated: 2026-11-14 20:00
Last completed task: T1.1 — Structure & types
Current task: T1.2 — Missing values   | status: [~] in progress (auditing missingness, co-missing block, churn-when-missing, and plotting fig_04_missing.png)
Next concrete action: Compute missing value counts/rates across all 100 columns, verify the ~1.73% co-missing demographic block and churn rates when missing vs present, save `outputs/figures/fig_04_missing.png` (matplotlib), inspect the PNG, and update `Islam-Raad.ipynb` Section 3.2 and `outputs/results.json`.
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Audited dtypes (`69 float64`, `10 int64`, `21 object/str`), deep memory (`158.88 MB`), and confirmed `0` duplicate rows or feature rows.
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.dtypes`: `float64 = 69`, `int64 = 10`, `object = 21`; `memory_mb = 158.88`; `duplicate_rows = 0`.
- `data.months_min` / `median` / `max`: `6` / `16.0` / `61`.
- `tutorial_baseline.test_acc`: `0.6357`, `test_auc`: `0.6938`, `train_acc`: `0.7349`, `majority_test_acc`: `0.5044`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders to be replaced by Islam before submission.
