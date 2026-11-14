# PROGRESS
Updated: 2026-11-14 20:19
Last completed task: T1.5 — Near-duplicates & near-empty columns
Current task: T1.6 — Documentation vs data   | status: [~] in progress (auditing change_mou/change_rev, recv_sms_Mean, iwylis_vce_Mean, infobase)
Next concrete action: Test the percentage claim for `change_mou`/`change_rev`, audit `recv_sms_Mean`, `iwylis_vce_Mean`, `infobase`, update Section 3.6 of `Islam-Raad.ipynb`, and populate `Data-Doc Discrepancies` in `docs/NOTES.md`.
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Audited dtypes (`69 float64`, `10 int64`, `21 object/str`), deep memory (`158.88 MB`), missingness (`43` cols, `fig_04_missing.png`), negatives (`eqpdays` 133, `totmrc_Mean` 23, `rev_Mean` 5, `avg6rev` 3), and extreme skew (`uniqsubs`, `totcalls`, `totmou`, `rev_Mean`).
- Completed T1.5 near-duplicate & zero-heavy audit: found `20` pairs with Spearman $|\rho| > 0.97$ and `11` columns with $\ge 90\%$ zeros; verified via 5-fold CV on the 70% training split that dropping 10 redundant near-duplicates slightly improves/maintains AUC (`0.6937 ± 0.0019` $\rightarrow$ `0.6944 ± 0.0019` with Ordinal+NaN; `0.6909` $\rightarrow$ `0.6910` with native categorical splits).
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.missing_summary`: `43` cols with missing values (`numbcars = 49.37%`, `dwllsize = 38.31%`); co-missing demographic block = `1,732` rows (`47.86%` churn); missing `change_mou` = `891` rows (`76.09%` churn).
- `data.negatives`: `eqpdays = 133` (min `-5.0`, churn `35.34%`), `totmrc_Mean = 23` (min `-26.91`), `rev_Mean = 5` (min `-6.17`), `avg6rev = 3` (min `-2.0`).
- `data.near_duplicates`: `20` pairs with Spearman $|\rho| > 0.97$; `11` columns $\ge 90\%$ zeros (`callfwdv_Mean = 99.57%`, `recv_sms_Mean = 99.13%`).
- `data.drop10_cv_check`: 98 features CV AUC `0.6937 ± 0.0019` vs. 88 features `0.6944 ± 0.0019`.
- `tutorial_baseline.test_acc`: `0.6357`, `test_auc`: `0.6938`, `train_acc`: `0.7349`, `majority_test_acc`: `0.5044`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/figures/fig_04_missing.png`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders to be replaced by Islam before submission.
