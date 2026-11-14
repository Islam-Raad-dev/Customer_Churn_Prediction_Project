# PROGRESS
Updated: 2026-11-14 20:03
Last completed task: T1.2 — Missing values
Current task: T1.3 — Negative/impossible values   | status: [~] in progress (auditing negative values across numeric features and logging decisions)
Next concrete action: Audit all numeric columns for negative values (`eqpdays`, `rev_Mean`, `totmrc_Mean`, `avg6rev`, etc.), compute counts, minima, and churn rates, explain the tutorial's `np.log1p` RuntimeWarnings, and log per-column handling in `docs/NOTES.md → Decision Log`.
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Audited dtypes (`69 float64`, `10 int64`, `21 object/str`), deep memory (`158.88 MB`), and confirmed `0` duplicate rows.
- Completed missingness audit (T1.2): identified `43` columns with missing values, verified the `1,732`-row co-missing demographic block (`11` columns, `47.86%` churn) and high-signal missingness in `change_mou`/`change_rev` (`891` rows, `76.09%` churn) and `rev_Mean`/`mou_Mean` (`357` rows, `68.63%` churn).
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.dtypes`: `float64 = 69`, `int64 = 10`, `object = 21`; `memory_mb = 158.88`.
- `data.missing_summary`: `43` cols with missing values; top missing `numbcars = 49.37%`, `dwllsize = 38.31%`, `HHstatin = 37.92%`, `ownrent = 33.71%`, `dwlltype = 31.91%`, `lor = 30.19%`, `income = 25.44%`; co-missing demographic block = `1,732` rows (`1.73%`, `47.86%` churn); missing `change_mou` = `891` rows (`0.89%`, `76.09%` churn); missing `hnd_webcap` = `10,189` rows (`10.19%`, `59.15%` churn); missing `avg6*` = `2,839` rows (`2.84%`, `40.23%` churn).
- `tutorial_baseline.test_acc`: `0.6357`, `test_auc`: `0.6938`, `train_acc`: `0.7349`, `majority_test_acc`: `0.5044`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/figures/fig_04_missing.png`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders to be replaced by Islam before submission.
