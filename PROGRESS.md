# PROGRESS
Updated: 2026-11-14 21:41
Last completed task: T5.3 — Leakage review (max single-feature train AUC = `0.5817` on `dev_age_gt_300`, `0.5751` on `eqpdays`)
Current task: T5.4 — Fairness variants   | status: [~] in progress (evaluating Full 126, No-`ethnic` 125, and No-Socioeconomic-Proxies 117 feature sets)
Next concrete action: Evaluate and document the 3 fairness feature-set variants (`T5.4`), then append the Phase 5 Arabic walkthrough to `docs/UNDERSTANDING_AR.md` and tag `phase-5-done` (`T5.5`).
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Completed Phase 1 Data Audit (`T1.1`–`T1.8`, tagged `phase-1-done`).
- Completed Phase 2 Exploratory Data Analysis (`T2.1`–`T2.12`, tagged `phase-2-done`).
- Completed Phase 3 Market Research (`T3.1`–`T3.6`, tagged `phase-3-done`).
- Completed Phase 4 Problem Definition & Decision Gate (`T4.1`–`T4.5`, tagged `phase-4-done`).
- Completed `T5.1` (leakage-safe preprocessing pipelines), `T5.2` (engineered 28 domain features and populated Feature Dictionary), and `T5.3` (verified zero target leakage; max single-feature train AUC = `0.5817` for `dev_age_gt_300` and `0.5751` for `eqpdays`).
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.churn_count`: `49,562` (`49.562%`), `data.stayed_count`: `50,438` (`50.438%`), `data.imbalance_ratio`: `1.0177`.
- `eda.device_age_summary`: train `<=300d` churn `39.40%` (`n=28,131`) vs `>300d` churn `56.39%` (`n=41,868`, `+16.99 pp`).
- `eda.jump_ci`: `260–300d` (`36.85%`) vs `301–340d` (`60.69%`), `+23.83 pp` (`95% CI [+22.12, +25.62] pp`), local linear jump `+23.22 pp`, `months >= 10` jump `+19.46 pp`.
- `eda.tenure_summary`: month 9 `29.25%` $\rightarrow$ month 10 `40.18%` $\rightarrow$ month 11 `64.57%` $\rightarrow$ month 12 `61.49%` $\rightarrow$ `37+` months `47.15%`.
- `eda.zero_usage`: `mou_Mean == 0` has `n=1,120` train (`1,600` all), churn `78.48%` (`79.81%` all), mean `rev_Mean = 22.89 MU` (`0.62%` revenue share).
- `tutorial_baseline.test_acc`: `0.6357`, `test_auc`: `0.6938`, `train_acc`: `0.7349`, `majority_test_acc`: `0.5044`.
- `preprocessing.xgb_leakage_safe_ordinal_nan.cv_auc_mean`: `0.6938` (`±0.0016`).
- `feature_engineering.n_engineered_features`: `28` (max single-feature train AUC: `dev_age_gt_300` at `0.5817`, raw `eqpdays` at `0.5751`).
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/figures/fig_04_missing.png`, `outputs/figures/fig_05_device_age.png`, `outputs/figures/fig_06a_tenure.png`, `outputs/figures/fig_06b_entanglement.png`, `outputs/figures/fig_06c_usage_collapse.png`, `outputs/figures/fig_06_tenure_usage.png`, `submission/references.txt`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders (`[15]`, `[16]`) to be replaced by Islam before submission.
