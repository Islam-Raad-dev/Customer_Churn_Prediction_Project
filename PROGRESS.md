# PROGRESS
Updated: 2026-11-14 23:00
Last completed task: T8.9 — Phase 8 wrap-up (Arabic section, commit, tag `phase-8-done`)
Current task: T9.1 — Review and finalize `Islam-Raad.ipynb`   | status: [~] in progress (adding Sections 10 & 11, verifying `DATA_DIR` auto-detection, and running end-to-end `nbconvert --execute`)
Next concrete action: Complete `T9.1`–`T9.6` (add Sections 10 & 11, verify `DATA_DIR` auto-detection across `./telecom/`, `../telecom/`, and Colab, run full `nbconvert --to notebook --execute`, verify regenerated `results.json` matches, and tag `phase-9-done`).
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
- Completed Phase 5 Preprocessing & Feature Engineering (`T5.1`–`T5.5`, tagged `phase-5-done`).
- Completed Phase 6 Modeling & Experiments (`T6.1`–`T6.7`, tagged `phase-6-done`).
- Completed Phase 7 Evaluation & Interpretation (`T7.1`–`T7.9`, tagged `phase-7-done`).
- Completed Phase 8 Business-Impact Model (`T8.1`–`T8.9`, tagged `phase-8-done`): Unit-tested label-shift re-basing (`4/13` toy check), computed net impact across Conservative/Base/Optimistic scenarios (`Base @ k=10%, π_r=10%`: `+82,557 MU`, `s*=9.84%`, optimal `k*=15%` `+90,940 MU`; `Base @ k=10%, π_r=5%`: `+13,160 MU`, optimal `k*=4%` `+23,955 MU`; `Conservative @ k*=4%, π_r=10%`: `+15,349 MU`; `Optimistic @ k=10%`: `+368,006 MU`), generated `fig_13_scenarios.png`, `fig_13_tornado.png`, and `fig_13_impact.png`, and sized the non-overlapping Lane 2 90-day 50/50 holdout A/B pilot (`2,000` treatment vs `2,000` control, `96.88%` non-overlapping with Lane 1 Top-10%, Base pilot net return `+4,691 MU` / `+30,414 MU` at full non-overlapping scale).
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.churn_count`: `49,562` (`49.562%`), `data.stayed_count`: `50,438` (`50.438%`), `data.imbalance_ratio`: `1.0177`.
- `eda.device_age_summary`: train `<=300d` churn `39.40%` (`n=28,131`) vs `>300d` churn `56.39%` (`n=41,868`, `+16.99 pp`).
- `eda.jump_ci`: `260–300d` (`36.85%`) vs `301–340d` (`60.69%`), `+23.83 pp` (`95% CI [+22.12, +25.62] pp`), local linear jump `+23.22 pp`, `months >= 10` jump `+19.46 pp`.
- `eda.tenure_summary`: month 9 `29.25%` $\rightarrow$ month 10 `40.18%` $\rightarrow$ month 11 `64.57%` $\rightarrow$ month 12 `61.49%` $\rightarrow$ `37+` months `47.15%`.
- `eda.zero_usage`: `mou_Mean == 0` has `n=1,120` train (`1,600` all), churn `78.48%` (`79.81%` all), mean `rev_Mean = 22.89 MU` (`0.62%` revenue share).
- `final_model`: `M5` (`cv_auc_mean`: `0.7020 ± 0.0013`, `test_auc`: `0.7029`, `test_acc`: `0.6409`, `test_precision`: `0.6382`, `test_recall`: `0.6360`, `test_f1`: `0.6371`, `test_brier`: `0.2180`).
- `topk[k=10%]`: `precision=0.8130` (`lift=1.6403`), `precision_rebased_10=0.3296` (`lift=3.2957`), `precision_rebased_5=0.1889` (`lift=3.7775`).
- `impact.scenarios.base_10pct`: `k=10%` Net = `+82,557 MU` (`s* = 9.84%`), `k*=15%` Net = `+90,940 MU`.
- `impact.scenarios.base_5pct`: `k=10%` Net = `+13,160 MU` (`s* = 17.17%`), `k*=4%` Net = `+23,955 MU`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/tables/experiment_log.csv`, `outputs/tables/test_predictions.csv`, `outputs/models/final_xgb_m5_pipeline.joblib`, `outputs/figures/fig_04_missing.png`, `outputs/figures/fig_05_device_age.png`, `outputs/figures/fig_06a_tenure.png`, `outputs/figures/fig_06b_entanglement.png`, `outputs/figures/fig_06c_usage_collapse.png`, `outputs/figures/fig_06_tenure_usage.png`, `outputs/figures/fig_09_model_comparison.png`, `outputs/figures/fig_10_importance.png`, `outputs/figures/fig_10_pdp.png`, `outputs/figures/fig_11_confusion.png`, `outputs/figures/fig_11_lift.png`, `outputs/figures/fig_11_calibration.png`, `outputs/figures/fig_13_scenarios.png`, `outputs/figures/fig_13_tornado.png`, `outputs/figures/fig_13_impact.png`, `submission/references.txt`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders (`[15]`, `[16]`) to be replaced by Islam before submission.
