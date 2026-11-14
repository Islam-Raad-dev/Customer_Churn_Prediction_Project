# PROGRESS
Updated: 2026-11-14 20:50
Last completed task: T2.9 — Demographics vs churn + fairness note
Current task: T2.10 — Select 4–6 final EDA charts for slides 4–6   | status: [~] in progress (verifying and finalizing the 5 EDA charts + combined Slide 6 small-multiples figure `fig_06_tenure_usage.png`)
Next concrete action: Produce the combined Slide 6 2-panel small-multiples figure `outputs/figures/fig_06_tenure_usage.png` (`9.0 × 3.6` in, 200 DPI) alongside the individual panels (`fig_04_missing.png`, `fig_05_device_age.png`, `fig_06a_tenure.png`, `fig_06b_entanglement.png`, `fig_06c_usage_collapse.png`), inspect via `read_file`, and log in `Islam-Raad.ipynb`.
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Completed Phase 1 Data Audit (`T1.1`–`T1.8`, tagged `phase-1-done`).
- Completed T2.1–T2.9: device-age jump (`+23.83 pp` across `300d`, `fig_05_device_age.png`), robustness check (`95% CI [+22.12, +25.62] pp`), service tenure cliff (`29.25%` at month 9 $\rightarrow$ `64.57%` at month 11, `fig_06a_tenure.png`), tenure × device-age entanglement (`fig_06b_entanglement.png`), usage-collapse segments (`fig_06c_usage_collapse.png`), revenue/value distributions, customer-care calls, call quality/overage/roaming, and demographics + fairness policy (`ethnic` spread `18.88 pp` $\rightarrow$ excluded from targeting).
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.churn_count`: `49,562` (`49.562%`), `data.stayed_count`: `50,438` (`50.438%`), `data.imbalance_ratio`: `1.0177`.
- `eda.device_age_summary`: train `<=300d` churn `39.40%` (`n=28,131`) vs `>300d` churn `56.39%` (`n=41,868`, `+16.99 pp`).
- `eda.jump_ci`: `260–300d` (`36.85%`) vs `301–340d` (`60.69%`), `+23.83 pp` (`95% CI [+22.12, +25.62] pp`), local linear jump `+23.22 pp`, `months >= 10` jump `+19.46 pp`.
- `eda.tenure_summary`: month 9 `29.25%` $\rightarrow$ month 10 `40.18%` $\rightarrow$ month 11 `64.57%` $\rightarrow$ month 12 `61.49%` $\rightarrow$ `37+` months `47.15%`.
- `eda.zero_usage`: `mou_Mean == 0` has `n=1,120` train (`1,600` all), churn `78.48%` (`79.81%` all), mean `rev_Mean = 22.89 MU` (`0.62%` revenue share).
- `eda.demographics`: household spread `2.68–5.26 pp` vs `ethnic` spread `18.88 pp`.
- `tutorial_baseline.test_acc`: `0.6357`, `test_auc`: `0.6938`, `train_acc`: `0.7349`, `majority_test_acc`: `0.5044`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/figures/fig_04_missing.png`, `outputs/figures/fig_05_device_age.png`, `outputs/figures/fig_06a_tenure.png`, `outputs/figures/fig_06b_entanglement.png`, `outputs/figures/fig_06c_usage_collapse.png`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders to be replaced by Islam before submission.
