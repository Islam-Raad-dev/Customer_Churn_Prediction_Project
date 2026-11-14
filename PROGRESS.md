# PROGRESS
Updated: 2026-11-14 20:05
Last completed task: T1.3 — Negative/impossible values
Current task: T1.4 — Outliers & skew   | status: [~] in progress (auditing p1/p50/p99/max and skewness across numeric columns)
Next concrete action: Compute p1, p50, p99, max, and skewness across numeric columns, audit extreme cases (`uniqsubs`, `totcalls`, `totmou`, `rev_Mean`, `mou_Mean`, `hnd_price`), and update Section 3.4 of `Islam-Raad.ipynb` and `outputs/results.json`.
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Audited dtypes (`69 float64`, `10 int64`, `21 object/str`), deep memory (`158.88 MB`), and confirmed `0` duplicate rows.
- Completed missingness audit (T1.2) and saved `outputs/figures/fig_04_missing.png`.
- Completed negative values audit (T1.3): logged keep/clip/flag rules for `change_mou`/`change_rev` (keep), `eqpdays` (`133` negatives, min `-5`, `35.34%` churn → clip to `0` + flag), and `totmrc_Mean` (`23` negatives, min `-26.91`), `rev_Mean` (`5` negatives, min `-6.17`), `avg6rev` (`3` negatives, min `-2.00`); explained `np.log1p` `RuntimeWarning` in `tutorial.ipynb`.
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.dtypes`: `float64 = 69`, `int64 = 10`, `object = 21`; `memory_mb = 158.88`.
- `data.missing_summary`: `43` cols with missing values (`numbcars = 49.37%`, `dwllsize = 38.31%`); co-missing demographic block = `1,732` rows (`47.86%` churn); missing `change_mou` = `891` rows (`76.09%` churn).
- `data.negatives`: `eqpdays = 133` (min `-5.0`, churn `35.34%`), `totmrc_Mean = 23` (min `-26.91`, churn `47.83%`), `rev_Mean = 5` (min `-6.17`, churn `40.00%`), `avg6rev = 3` (min `-2.0`, churn `66.67%`), `change_rev = 56,150`, `change_mou = 53,651`.
- `tutorial_baseline.test_acc`: `0.6357`, `test_auc`: `0.6938`, `train_acc`: `0.7349`, `majority_test_acc`: `0.5044`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/figures/fig_04_missing.png`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders to be replaced by Islam before submission.
