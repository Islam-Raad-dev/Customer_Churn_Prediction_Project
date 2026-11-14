# PROGRESS
Updated: 2026-11-14 20:21
Last completed task: T1.6 — Documentation vs data
Current task: T1.7 — Target audit   | status: [~] in progress (auditing churn target distribution and realism implications)
Next concrete action: Audit `churn` target counts (`49,562` churn vs. `50,438` stayed, `49.562%`), explain why accuracy is meaningful on the balanced sample but misleading at realistic `5%–10%` telecom churn, update Section 3.7 of `Islam-Raad.ipynb` and `outputs/results.json`.
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Completed T1.1–T1.5 audits (dtypes, missingness + `fig_04_missing.png`, negatives, outliers/skew, near-duplicates & 5-fold CV check).
- Completed T1.6 documentation-vs-data audit: proved `change_mou` (`22,585` rows `< -100`, `22.79%` of non-null; Spearman $\rho = 0.9881$ with `mou_Mean - avg3mou`) and `change_rev` ($\rho = 0.9561$ with `rev_Mean - avg3rev`) are absolute changes, not percentages; logged exact slide wording in `docs/NOTES.md → Data-Doc Discrepancies`.
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.missing_summary`: `43` cols with missing values (`numbcars = 49.37%`, `dwllsize = 38.31%`); co-missing demographic block = `1,732` rows (`47.86%` churn); missing `change_mou` = `891` rows (`76.09%` churn).
- `data.negatives`: `eqpdays = 133` (min `-5.0`, churn `35.34%`), `totmrc_Mean = 23` (min `-26.91`), `rev_Mean = 5` (min `-6.17`), `avg6rev = 3` (min `-2.0`).
- `data.near_duplicates`: `20` pairs with Spearman $|\rho| > 0.97$; `11` columns $\ge 90\%$ zeros; dropping 10 duplicates keeps 5-fold CV AUC at `0.6944 ± 0.0019` (vs `0.6937 ± 0.0019`).
- `data.doc_vs_data`: `change_mou < -100` in `22,585` rows (`22.79%`); `Spearman(change_mou, mou_Mean - avg3mou) = 0.9881`; `Spearman(change_rev, rev_Mean - avg3rev) = 0.9561`; `iwylis_vce_Mean` $\rho = 0.9687$ with `mouiwylisv_Mean`.
- `tutorial_baseline.test_acc`: `0.6357`, `test_auc`: `0.6938`, `train_acc`: `0.7349`, `majority_test_acc`: `0.5044`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/figures/fig_04_missing.png`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders to be replaced by Islam before submission.
