# PROGRESS
Updated: 2026-11-14 20:39
Last completed task: T2.4 — Entanglement (`fig_06b_entanglement.png`)
Current task: T2.5 — Usage-collapse segments   | status: [~] in progress (analyzing `mou_Mean` = 0, ≤10, ≤30, ≤65, and missing `change_mou` segments)
Next concrete action: Compute size, churn rate, mean revenue, revenue share, and lifetime totals (`totmou, totcalls, totrev`) for each usage-collapse segment on the 70% training split, assess whether `mou_Mean == 0` is "already gone" vs. `1–65` / negative `change_mou` as actionable early-warning segments, plot `outputs/figures/fig_06c_usage_collapse.png`, and update `Islam-Raad.ipynb` Section 4.5 and `outputs/results.json`.
Key decisions so far:
- Traced all 7 grading requirements, deliverable rules, and deadlines to `README.docx` (GCI World 2026 September, deadline 28 Nov 2026 11:30 UTC).
- Verified `/home/islam-raad/ai_workspace/bin/python3.12` (Python 3.12.3) has all required packages; 0 packages installed or upgraded.
- Initialized local-only git repository on `main` with strict `.gitignore` and PRD §3 lean workspace.
- Verified 1-to-1 inner merge of `Client.csv` (100,000 × 50) and `Record.csv` (100,000 × 51) on `Customer_ID` (`1000001`–`1100000`) → `(100000, 100)`.
- Reproduced exact tutorial baseline (`0.6357` test accuracy, `0.6938` test AUC).
- Completed Phase 1 Data Audit (`T1.1`–`T1.8`, tagged `phase-1-done`).
- Completed T2.1–T2.4: device-age jump (`+23.83 pp` across `300d`, `fig_05_device_age.png`), robustness check (`95% CI [+22.12, +25.62] pp`, `19/19` areas, `8/8` credit classes), service tenure cliff (`29.25%` at month 9 $\rightarrow$ `64.57%` at month 11, `fig_06a_tenure.png`), and tenure × device-age entanglement (`n=0` at `6–9m × >300d`; within `months >= 10`, `<=300d` is `43.44%` vs `>300d` `56.39%`, `+12.95 pp`, `fig_06b_entanglement.png`).
Key numbers so far (from results.json):
- `data.n_rows`: `100,000`, `data.n_cols`: `100`, `data.n_features_raw`: `98`.
- `data.churn_count`: `49,562` (`49.562%`), `data.stayed_count`: `50,438` (`50.438%`), `data.imbalance_ratio`: `1.0177`.
- `eda.device_age_summary`: train `<=300d` churn `39.40%` (`n=28,131`) vs `>300d` churn `56.39%` (`n=41,868`, `+16.99 pp`); `261–300d` (`36.93%`) to `301–340d` (`60.69%`, `+23.75 pp`), peak `321–340d` (`64.34%`).
- `eda.jump_ci`: `260–300d` (`36.85%`) vs `301–340d` (`60.69%`), `+23.83 pp` (`95% CI [+22.12, +25.62] pp`), local linear jump `+23.22 pp`, `months >= 10` jump `+19.46 pp`.
- `eda.tenure_summary`: month 9 `29.25%` (`28.80%` all) $\rightarrow$ month 10 `40.18%` $\rightarrow$ month 11 `64.57%` (`65.13%` all) $\rightarrow$ month 12 `61.49%` (`61.86%` all) $\rightarrow$ `37+` months `47.15%`.
- `eda.entanglement`: `n=0` in `6–9m × >300d`; within `months >= 10`, `<=300d` churn `43.44%` vs `>300d` `56.39%` (`+12.95 pp`), peaking at `63.7%` in `10–12m × 301–360d` (`n=7,456`).
- `tutorial_baseline.test_acc`: `0.6357`, `test_auc`: `0.6938`, `train_acc`: `0.7349`, `majority_test_acc`: `0.5044`.
Files produced so far:
- `.gitignore`, `PROGRESS.md`, `Islam-Raad.ipynb`, `docs/NOTES.md`, `docs/UNDERSTANDING_AR.md`, `research/sources_log.md`, `scripts/check_submission.py`, `outputs/results.json`, `outputs/figures/fig_04_missing.png`, `outputs/figures/fig_05_device_age.png`, `outputs/figures/fig_06a_tenure.png`, `outputs/figures/fig_06b_entanglement.png`
Google Slides: not created yet
Open issues / assumptions pending:
- AI chat link placeholders to be replaced by Islam before submission.
