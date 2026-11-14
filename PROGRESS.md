# PROGRESS
Updated: 2026-11-14 20:31
Last completed task: T2.1 — `eqpdays` vs churn (`fig_05_device_age.png`)
Current task: T2.2 — Robustness of the ~300-day jump   | status: [~] in progress (running bootstrap 95% CI, local linear fits, subgroup stability, and covariate balance at 300 days)
Next concrete action: Run bootstrap 95% CI of `churn(301–340) - churn(260–300)`, local linear fits on each side of 300 days, subgroup checks (`months >= 10`, `area`, `crclscod`), and covariate balance checks (`rev_Mean, hnd_price, months, mou_Mean, uniqsubs`), then write the verdict in `docs/NOTES.md` and `Islam-Raad.ipynb` Section 4.2.
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Completed Phase 1 Data Audit (`T1.1`–`T1.8`, tagged `phase-1-done`).
- Completed T2.1: discovered on the 70% training split (`n=69,999` valid) that churn jumps by `+23.75 pp` from `36.93%` (`261–300d`) to `60.69%` (`301–340d`), peaking at `64.34%` (`321–340d`); generated and verified `outputs/figures/fig_05_device_age.png`.
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.churn_count`: `49,562` (`49.562%`), `data.stayed_count`: `50,438` (`50.438%`), `data.imbalance_ratio`: `1.0177`.
- `eda.device_age_summary`: train `<=300d` churn `39.40%` (`n=28,131`) vs `>300d` churn `56.39%` (`n=41,868`, `+16.99 pp`); `261–300d` (`36.93%`) to `301–340d` (`60.69%`, `+23.75 pp`), peak `321–340d` (`64.34%`).
- `tutorial_baseline.test_acc`: `0.6357`, `test_auc`: `0.6938`, `train_acc`: `0.7349`, `majority_test_acc`: `0.5044`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/figures/fig_04_missing.png`, `outputs/figures/fig_05_device_age.png`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders to be replaced by Islam before submission.
