# PROGRESS
Updated: 2026-11-14 20:07
Last completed task: T1.4 — Outliers & skew
Current task: T1.5 — Near-duplicates & near-empty columns   | status: [~] in progress (computing Spearman |ρ| > 0.97 pairs, zero-heavy columns, and 5-fold CV AUC test)
Next concrete action: Find all numeric column pairs with Spearman $|\rho| > 0.97$, list columns with $\ge 90\%$ (and $\ge 85\%$) zeros, run a 5-fold CV AUC comparison dropping the 10 redundant columns, and update Section 3.5 of `Islam-Raad.ipynb` and `outputs/results.json`.
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Audited dtypes (`69 float64`, `10 int64`, `21 object/str`), deep memory (`158.88 MB`), and confirmed `0` duplicate rows.
- Completed missingness audit (T1.2) and saved `outputs/figures/fig_04_missing.png`.
- Completed negative values audit (T1.3) and outliers/skew audit (T1.4): logged keep/clip/flag rules for negatives and documented heavy right-tail skew (`uniqsubs` max `196`, `totcalls` max `98,874`, `totmou` max `233,419.1`, `rev_Mean` median `48.20` vs `p99 = 227.89` and max `3,843.26`) and `17` discrete `hnd_price` tiers (`9.99`–`499.99`).
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.dtypes`: `float64 = 69`, `int64 = 10`, `object = 21`; `memory_mb = 158.88`.
- `data.missing_summary`: `43` cols with missing values (`numbcars = 49.37%`, `dwllsize = 38.31%`); co-missing demographic block = `1,732` rows (`47.86%` churn); missing `change_mou` = `891` rows (`76.09%` churn).
- `data.negatives`: `eqpdays = 133` (min `-5.0`, churn `35.34%`), `totmrc_Mean = 23` (min `-26.91`, churn `47.83%`), `rev_Mean = 5` (min `-6.17`, churn `40.00%`), `avg6rev = 3` (min `-2.0`, churn `66.67%`).
- `data.outliers_focus`: `rev_Mean` median `48.20` (`p99 = 227.89`, max `3,843.26`), `mou_Mean` median `355.50` (`p99 = 2,422.40`, max `12,206.75`), `uniqsubs` median `1` (`p99 = 5`, max `196`, `13` accounts > 10), `hnd_price` = `17` tiers.
- `tutorial_baseline.test_acc`: `0.6357`, `test_auc`: `0.6938`, `train_acc`: `0.7349`, `majority_test_acc`: `0.5044`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/figures/fig_04_missing.png`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders to be replaced by Islam before submission.
