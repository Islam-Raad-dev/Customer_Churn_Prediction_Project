# tasks.md v2 — Execution Plan for the Antigravity (Gemini) Agent
## GCI World 2026 — Final Assignment (Company A Telecom Churn PoC)

> Read `prd.md` once at the start (it defines *what/why*). This file defines *what to do next*, in strict order.
> Workspace: **the current folder opened in Antigravity** (project root; relative paths only; fresh folder containing only `prd.md`, `tasks.md`, `telecom/`, and the 5 course documents) · Interpreter: **`/home/islam-raad/ai_workspace/bin/python3.12`** (use it for everything) · Omnicampus account: **`Islam-Raad`** · Deadline: Sat 28 Nov 2026, 11:30 UTC (14:30 Iraq).
> **No time pressure and no priority tiers.** Execute **every task, in order, one at a time, at full quality.** Do not skip, merge or reorder tasks.

---

## ⚙️ The step ritual (do this for EVERY task)
1. **Resume check:** read only `PROGRESS.md`, this task's block, the PRD section it cites, and `git log --oneline -10`. Never re-read everything.
2. **Mark start:** change the task to `[~]` (add one indented line describing what's being done).
3. **Do the work** with the venv interpreter; **run → read real output → decide**. Charts: matplotlib only (PRD §10).
4. **Add/update the matching section of `Islam-Raad.ipynb`** (always runnable) and write any numbers into `outputs/results.json`.
5. **Verify** the "Done when" condition by reading actual outputs/files.
6. **Mark done:** change to `[x] ✔ YYYY-MM-DD HH:MM`.
7. **Rewrite `PROGRESS.md`** (last completed, current/next task, key decisions, key numbers, files, Slides URL, open issues).
8. **Commit:** `git status` (no CSVs/keys staged) → `git add -A` → commit with the format in PRD §0.3:
   `<type>(<phase>): T<id> <summary>` + body lines `What / Result / Files`.
9. **At the end of each phase:** append that phase's Arabic section to `docs/UNDERSTANDING_AR.md` (what · why · how · result · pitfalls · what to say), commit it, then `git tag phase-<n>-done`.

**Legend:** `[ ]` not started · `[~]` in progress · `[x] ✔ <timestamp>` done.
**Interruption safety:** if you stop suddenly, the next session resumes from `PROGRESS.md` and the first `[ ]`/`[~]` task here. Use `wip(...)` commits inside long tasks.

---

## Phase 0 — Setup and baseline  (commit type: `chore`/`data`)
- [x] **T0.1 Read the five workspace documents once** (README, tutorial PDF, tutorial notebook, dataset overview, guide PDF). Write a short **Requirements digest** section in `docs/NOTES.md` (7 requirements, deliverable rules, citation/AI rules, deadlines, any conflicts with the PRD). *Done when:* every PRD rule traces to a source file or is marked "PRD-only". ✔ 2026-11-14 19:48
- [x] **T0.2 Check the environment.** Run `/home/islam-raad/ai_workspace/bin/python3.12 -m pip list`; confirm pandas, numpy, scikit-learn, xgboost, matplotlib, scipy, jupyter/nbconvert, nbformat, joblib. Install **only missing** packages into this env (log in `docs/NOTES.md → Environment`); never upgrade existing ones. Check matplotlib fonts (`Open Sans` available? else DejaVu Sans) and log. Create a Jupyter kernel entry pointing to this interpreter if needed. *Done when:* all imports work and versions are logged. ✔ 2026-11-14 19:50
- [x] **T0.3 Initialize git (local only).** `git init`, branch `main`, identity (existing global, else repo-local `Islam-Raad`), `.gitignore` per PRD §0.3, first commit. **No remote, no push.** *Done when:* `git log` shows the first commit and `git status` is clean. ✔ 2026-11-14 19:51
- [x] **T0.4 Create the lean workspace** from PRD §3 only: `PROGRESS.md`, `docs/NOTES.md` (sections: Decision log · Assumptions · Hypotheses · Feature dictionary · Data-doc discrepancies · Environment · Slides), `docs/UNDERSTANDING_AR.md` (empty skeleton), `outputs/{figures,tables,models}`, `research/sources_log.md`, `scripts/`, `submission/`, and the notebook skeleton `Islam-Raad.ipynb` (sections 0–11 headers + helper section stubs). *Done when:* only those files/folders exist (no extra stubs). ✔ 2026-11-14 19:54
- [x] **T0.5 Load and merge.** Read both CSVs; **print `df.columns`**; assert shapes (100000×50, 100000×51), `Customer_ID` unique, 1-to-1 inner merge → (100000, 100). Add to notebook section 2. *Done when:* assertions pass in the notebook. ✔ 2026-11-14 19:55
- [x] **T0.6 Reproduce the tutorial baseline exactly** (LabelEncoder on text columns; `XGBClassifier(n_estimators=300, learning_rate=0.05, max_depth=6, eval_metric='logloss', random_state=42)`; stratified 70/30, seed 42). Record test accuracy (expect ≈ 0.636; Islam's run 0.6357), **AUC (≈ 0.694), train accuracy (≈ 0.735)**, precision/recall/F1, confusion matrix, majority baseline (≈ 0.504) in `results.json`. *Done when:* within ±0.01 of expectations, or the difference is explained in the Decision log. ✔ 2026-11-14 19:57
- [x] **T0.7 Consolidate leftovers.** (In a fresh folder this is just a check that nothing extra exists.) If any extra files exist (stubs, digests, logs, `src/`, `config.py`, duplicate notebooks…), **merge useful content into `docs/NOTES.md` / the notebook and delete the rest**, so the workspace matches PRD §3. Reconstruct `PROGRESS.md` from what exists. *Done when:* `ls -R` matches PRD §3 (plus outputs). ✔ 2026-11-14 19:57
- [x] **T0.8 Phase wrap-up:** Arabic section "Phase 0" in `docs/UNDERSTANDING_AR.md`; commit; `git tag phase-0-done`. ✔ 2026-11-14 19:58

## Phase 1 — Data audit  (type: `data`)
- [x] **T1.1 Structure & types:** dtype counts (expect float64 69 / int64 10 / object 21), memory, duplicates, ID checks. Notebook §3. ✔ 2026-11-14 20:00
- [x] **T1.2 Missing values:** full table, **matplotlib** bar of top 20 (`fig_04_missing.png`), the "same rows missing across demographic columns" block (~1.7%), and **churn rate when missing vs present** for the top missing columns. ✔ 2026-11-14 20:03
- [x] **T1.3 Negative/impossible values** in `rev_Mean, mou_Mean, totmrc_Mean, eqpdays, avg6rev` etc.: counts, minima, churn rate of those rows; Decision-log entry per column (clip/flag/keep). Explain the tutorial's `log1p` RuntimeWarnings. ✔ 2026-11-14 20:05
- [x] **T1.4 Outliers & skew:** p1/p50/p99/max for numeric columns; list extreme cases (`uniqsubs`, `totcalls`, `totmou`). ✔ 2026-11-14 20:07
- [x] **T1.5 Near-duplicates & near-empty columns:** Spearman |ρ| > 0.97 pairs (top 20), columns ≥ 90% zeros; quick CV test of whether dropping duplicates changes AUC. ✔ 2026-11-14 20:19
- [x] **T1.6 Documentation vs data:** test the "percent" claim for `change_mou/change_rev`; check `recv_sms_Mean`, `iwylis_vce_Mean`, `infobase`; fill **Data-doc discrepancies** in `docs/NOTES.md` with the wording to use on slides. ✔ 2026-11-14 20:21
- [x] **T1.7 Target audit:** churn counts/rate (expect 49.56%); why accuracy is meaningful here but misleading at 5% churn; store in `results.json → data`. ✔ 2026-11-14 20:23
- [x] **T1.8 Phase wrap-up** (Arabic section, commit, tag `phase-1-done`). *Done when:* all tables/figures/numbers saved, anomalies explained. ✔ 2026-11-14 20:25

## Phase 2 — Exploratory data analysis  (type: `eda`)
Split first (stratified 70/30, seed 42); **discover thresholds on the training part only**; replicate on all rows only descriptively. Each analysis = one matplotlib chart + one-sentence finding (in the notebook and `docs/NOTES.md → Hypotheses`).
- [x] **T2.1 `eqpdays` vs churn:** bins ≤ 25 days with CI bands; negatives handled per T1.3; `fig_05_device_age.png`. ✔ 2026-11-14 20:31
- [x] **T2.2 Robustness of the ~300-day jump:** bootstrap 95% CI of churn(301–340) − churn(260–300); local linear fit on each side; repeat within tenure ≥ 10, by `area`, by `crclscod`; **covariate-balance check** at 300 days (`rev_Mean, hnd_price, months, mou_Mean, uniqsubs`). Write a verdict: *real-looking / uncertain / likely artifact* + reasons. **This verdict drives T4.2.** ✔ 2026-11-14 20:34
- [x] **T2.3 `months` vs churn:** per-month rate 6–61 with counts; locate the cliff (~10–12). ✔ 2026-11-14 20:36
- [x] **T2.4 Entanglement:** matplotlib heat-map (`imshow`) of churn by tenure bucket × device-age bucket with counts; device-age effect within tenure ≥ 10 only. ✔ 2026-11-14 20:39
- [x] **T2.5 Usage-collapse segments:** `mou_Mean` = 0, ≤ 10, ≤ 30, ≤ 65, missing `change_mou`: size, churn, mean revenue, revenue share, lifetime totals; stand-alone target or "already gone"? ✔ 2026-11-14 20:44
- [x] **T2.6 Revenue and "value":** distributions/medians by class; implication for defining a valuable customer. ✔ 2026-11-14 20:46
- [x] **T2.7 Customer-care calls vs churn:** buckets; ≥ 3 competing explanations (hypotheses only). ✔ 2026-11-14 20:47
- [x] **T2.8 Call quality, overage, roaming vs churn.** ✔ 2026-11-14 20:49
- [x] **T2.9 Demographics vs churn** + fairness note for `ethnic` and proxies. ✔ 2026-11-14 20:50
- [x] **T2.10 Select 4–6 final EDA charts** for slides 4–6 (PRD §10 style; exact placement sizes; PNG 200 dpi; open each PNG and inspect). ✔ 2026-11-14 20:53
- [x] **T2.11 Write 3 hypotheses** (full sentences, ranked by actionability) in `docs/NOTES.md → Hypotheses`; store key stats in `results.json → eda`. ✔ 2026-11-14 20:54
- [x] **T2.12 Phase wrap-up** (Arabic section, commit, tag `phase-2-done`). ✔ 2026-11-14 20:57

## Phase 3 — Market research  (type: `research`)
- [x] **T3.1 Search plan:** queries per PRD §7 question (Iraq mobile market, subscribers/penetration, operators, CMC, ITU/GSMA/DataReportal, retention vs acquisition, handset cycle & churn, campaign success rates, academic churn-prediction papers). ✔ 2026-11-14 20:59
- [x] **T3.2 Collect ≥ 8 sources (target 10–12):** open each page, verify the fact, log in `research/sources_log.md` (ID · title · publisher · publication date · URL · access date · fact used · reliability). Paraphrase; quotes ≤ 15 words only if essential. ✔ 2026-11-14 21:05
- [x] **T3.3 Answer each research question** in 3–6 lines with `[ID]` citations; where Iraqi data are missing, say so and label regional/global data. ✔ 2026-11-14 21:06
- [x] **T3.4 Choose 3 facts for slide 3** and numeric inputs for the impact model (churn prior, success rate, offer cost, margin, horizon); anything unsourced → **ASSUMPTION** in `docs/NOTES.md → Assumptions`. ✔ 2026-11-14 21:08
- [x] **T3.5 Draft `references.txt`** (order = citation order; stable IDs). ✔ 2026-11-14 21:09
- [x] **T3.6 Phase wrap-up** (Arabic section, commit, tag `phase-3-done`). ✔ 2026-11-14 21:11

## Phase 4 — Problem definition / Decision Gate  (type: `docs`)
- [x] **T4.1 Decision matrix** for options A–E (1–5 on evidence, actionability, measurability, risk, market fit) in `docs/NOTES.md`. ✔ 2026-11-14 21:13
- [x] **T4.2 Decide:** (i) default two-lane proposal, or (ii) risk ranking + value-at-risk only (if T2.2 says "likely artifact"). Log decision and reasons. ✔ 2026-11-14 21:14
- [x] **T4.3 Write the problem paragraph (3–5 sentences):** problem · for whom · target · ML task type and why · expected decision/action. *If it isn't clear to a non-technical manager, do not proceed to modeling.* ✔ 2026-11-14 21:15
- [x] **T4.4 Define KPI and decision owner** (e.g., incremental retention in a pilot; owner = retention/CRM). ✔ 2026-11-14 21:16
- [x] **T4.5 Phase wrap-up** (Arabic section, commit, tag `phase-4-done`). ✔ 2026-11-14 21:18

## Phase 5 — Preprocessing and feature engineering  (type: `feat`)
- [x] **T5.1 Leakage-safe preprocessing pipelines:** trees (native NaN + categorical handling) and logistic regression (median impute + missing flags + scaling + one-hot); compare vs tutorial LabelEncoder. ✔ 2026-11-14 21:32
- [x] **T5.2 Engineer ≥ 10 features** (PRD §8.3); safe division with epsilon; negatives per T1.3; fill **Feature dictionary** (name · formula · business reason · leakage check · kept?). ✔ 2026-11-14 21:40
- [x] **T5.3 Leakage review:** each feature available before the churn window; none uses `churn`; target statistics only inside CV folds; no single feature gives unexpectedly high AUC (prior max ≈ 0.57). ✔ 2026-11-14 21:41
- [x] **T5.4 Fairness variants:** feature sets with/without `ethnic, income, marital, kid*, dwllsize`. ✔ 2026-11-14 21:47
- [x] **T5.5 Phase wrap-up** (Arabic section, commit, tag `phase-5-done`). ✔ 2026-11-14 21:48

## Phase 6 — Modeling and experiments  (type: `model`)
- [x] **T6.1 Split:** stratified 70/30, seed 42 (identical to the tutorial); save indices. ✔ 2026-11-14 21:49
- [x] **T6.2 Models (≥ 4):** M0 majority · M1 logistic regression · M2 decision tree depth ≤ 4 (explanation) · M3 XGBoost tutorial params · M4 XGBoost + features · M5 XGBoost tuned (≤ 30 random configs, ≤ 20 min) · optional M6 LightGBM/RandomForest. ✔ 2026-11-14 22:08
- [x] **T6.3 5-fold stratified CV on the 70% only;** log every experiment in `outputs/tables/experiment_log.csv` (id · change · features · params · CV AUC · std · accuracy); differences < 1 std = noise. ✔ 2026-11-14 22:08
- [x] **T6.4 Choose the final model** (best CV AUC; ties → simpler); log reasoning. ✔ 2026-11-14 22:15
- [x] **T6.5 Final test evaluation (≤ 2 touches, logged):** AUC, accuracy, precision, recall, F1, confusion matrix, train–test gap; accuracy ≥ 0.75 or AUC ≥ 0.80 ⇒ leakage hunt first. ✔ 2026-11-14 22:15
- [x] **T6.6 Save** the model (`outputs/models/`, git-ignored) and `outputs/tables/test_predictions.csv` (row id · y_true · p_churn); fill `results.json → models, final_model`. ✔ 2026-11-14 22:15
- [x] **T6.7 Phase wrap-up** (Arabic section, commit, tag `phase-6-done`). ✔ 2026-11-14 22:15

## Phase 7 — Evaluation and interpretation  (type: `eval`)
- [x] **T7.1 Confusion matrix** at the stated threshold (matplotlib), explained in words (FP = wasted offer; FN = lost customer). ✔ 2026-11-14 22:20
- [x] **T7.2 Top-k table** k ∈ {1,2,5,10,15,20,30,50} (customers, precision, recall, lift) + gain/lift curve (matplotlib) → `results.json → topk`. ✔ 2026-11-14 22:20
- [x] **T7.3 Calibration** curve (matplotlib); isotonic calibration if probabilities enter money terms. ✔ 2026-11-14 22:20
- [x] **T7.4 Importance:** gain **and** permutation (held-out); explain gain vs weight; optional SHAP. ✔ 2026-11-14 22:42
- [x] **T7.5 Partial dependence** for `eqpdays` and `months` (matplotlib) — do thresholds show in the model? ✔ 2026-11-14 22:42
- [x] **T7.6 Ablation:** drop the top feature, retrain, compare CV AUC; conclude "one strong signal" vs "many weak ones". ✔ 2026-11-14 22:42
- [x] **T7.7 Lever table:** top 3–5 drivers → can the company change it? → implied action. ✔ 2026-11-14 22:42
- [x] **T7.8 Fairness check:** AUC with vs without sensitive/proxy fields; final feature-set decision. ✔ 2026-11-14 22:42
- [x] **T7.9 Phase wrap-up** (Arabic section, commit, tag `phase-7-done`). ✔ 2026-11-14 22:42

## Phase 8 — Business impact model  (type: `impact`)
- [x] **T8.1 Assumptions table** in `docs/NOTES.md`: ARPU (mean & median of `rev_Mean`, unit MU), margin, horizon H, success rate `s`, cost `c`, base N = 100,000, churn priors π_r ∈ {5%, 10%} — each **SOURCED [ID]** or **ASSUMPTION** with rationale. ✔ 2026-11-14 23:00
- [x] **T8.2 Re-basing function** (label shift): positives × π_r/π_s, negatives × (1−π_r)/(1−π_s); weighted precision@k and lift@k on test predictions; **unit-test with a toy example** inside the notebook; keep raw vs re-based side by side. ✔ 2026-11-14 23:00
- [x] **T8.3 Net-impact function** `Net = n·p_adj·s·V − n·c`, `V = ARPU × margin × H`; conservative/base/optimistic scenarios → `results.json → impact`. ✔ 2026-11-14 23:00
- [x] **T8.4 Optimal k\*** per scenario and **break-even** `s* = c/(p_adj·V)`; matplotlib net-vs-k chart. ✔ 2026-11-14 23:00
- [x] **T8.5 Sensitivity:** matplotlib tornado over `s, c, V, π_r, k`. ✔ 2026-11-14 23:00
- [x] **T8.6 Lane 2 sizing** (only if the threshold survived T2.2): window size × churn gap × closable share (scenarios), labelled *hypothesis → pilot*; design the A/B pilot (treatment vs holdout, duration, KPI = incremental retention). ✔ 2026-11-14 23:00
- [x] **T8.7 Sanity checks:** units (MU), no double counting, seed-independence beyond rounding, scenarios ordered logically. ✔ 2026-11-14 23:00
- [x] **T8.8 One-paragraph impact statement** ("estimated … under stated assumptions") with the range and key assumptions. ✔ 2026-11-14 23:00
- [x] **T8.9 Phase wrap-up** (Arabic section, commit, tag `phase-8-done`). ✔ 2026-11-14 23:00

## Phase 9 — Notebook finalization  (type: `notebook`)
- [x] **T9.1 Review the notebook as a whole:** headers mirror slides; first cell explains purpose, folder structure, how to run; each section ends with a one-line "so what"; helper functions (incl. matplotlib style) in section 1. ✔ 2026-11-15 06:34
- [x] **T9.2 Self-containment:** `DATA_DIR` auto-detection (`./telecom/` → `../telecom/` → Colab path, with a clear error message if none found; PRD §3); seed once; no absolute paths (except documented interpreter notes outside the notebook); optional libs guarded; no web calls; **no keys/personal data**. ✔ 2026-11-15 06:34
- [x] **T9.3 Export check:** the notebook writes `results.json`, figures and tables; every figure on a slide exists as `fig_<slide>_<topic>.png` at the exact placement size. ✔ 2026-11-15 06:34
- [x] **T9.4 Restart-and-run-all** with `…python3.12 -m jupyter nbconvert --to notebook --execute`; runtime < ~10 min; regenerated `results.json` equals the previous one (up to float rounding). ✔ 2026-11-15 06:34
- [x] **T9.5 Clean-up:** remove dead cells and bulky outputs; keep outputs visible. ✔ 2026-11-15 06:34
- [x] **T9.6 Phase wrap-up** (Arabic section, commit, tag `phase-9-done`). ✔ 2026-11-15 06:34

## Phase 10 — Slides in Google Slides → PDF  (type: `slides`)
Follow PRD §11 exactly (canvas 720 × 405 pt, grid, Montserrat + Open Sans, palette, shapes, 15-slide order). All charts/diagrams = matplotlib PNGs; tables = native Slides tables.
- [x] **T10.1 Capability probe** of the connected Google Slides/Drive integration (create presentation, set size, text box, table, shape, insert image, read thumbnail, export PDF). Log what works and the chosen fallback (PRD §11.1 step 4) in `docs/NOTES.md → Slides`. ✔ 2026-11-15 07:10
- [~] **T10.2 Create the presentation** "Islam-Raad — GCI Final Assignment"; set 16:9; set theme fonts/colors (or apply directly); create reusable layouts (title, takeaway+chart, two-column, table, KPI cards, references); store URL/ID in `PROGRESS.md`.
  - Creating the production presentation "Islam-Raad — GCI Final Assignment", verifying 16:9 canvas, defining reusable Python slide-builder helpers matching PRD §11.2–11.4, and logging presentation URL/ID.
- [ ] **T10.3 Produce final matplotlib figures** for slides 4–13 at exact placement sizes (PRD §10); diagrams for slides 4, 7, 10, 12 also in matplotlib; open and inspect every PNG.
- [ ] **T10.4 Upload the PNGs** to a Drive folder, make link-viewable only while embedding; after embedding, **revert sharing to private**.
- [ ] **T10.5 Build slides 1–4** (title, executive summary, market context, the data).  *Commit after the group.*
- [ ] **T10.6 Build slides 5–8** (EDA #1, EDA #2, problem definition, features).
- [ ] **T10.7 Build slides 9–12** (experiments — **live-text table** with model · metric · value; how it works + learned; targeting power; recommendation).
- [ ] **T10.8 Build slides 13–15** (estimated impact; risks/ethics/next steps; references identical to `references.txt`).
- [ ] **T10.9 Footnotes:** every external fact has `[n]`; every `[n]` exists on slide 15 and in `references.txt`.
- [ ] **T10.10 Story test:** read only the 15 titles; rewrite until each leads to the next (problem → evidence → model → decision → impact → risks).
- [ ] **T10.11 Visual QA of every slide** via thumbnails: overflow, overlaps, clipped labels, fonts (body ≥ 14 pt, chart text ≥ 10 pt), contrast, alignment to the grid, consistent colors; fix all issues.
- [ ] **T10.12 Speaker notes** (60–90 s) in each slide's native notes pane; copy to `docs/UNDERSTANDING_AR.md`.
- [ ] **T10.13 Export PDF** → `submission/Islam-Raad.pdf` (Drive export or Islam: File → Download → PDF); confirm ≤ 15 pages, ≤ 10 MB.
- [ ] **T10.14 Run `scripts/check_submission.py`** (page count, size, `pdftotext` finds model name/metric/result on slide 9, numbers vs `results.json`, `[n]` tags vs references): **0 problems**.
- [ ] **T10.15 Phase wrap-up** (Arabic section, commit, tag `phase-10-done`).

## Phase 11 — References and AI disclosure  (type: `docs`)
- [ ] **T11.1 Finalize `references.txt`:** numbered, one per line; market/academic sources, libraries (scikit-learn, XGBoost, pandas, matplotlib), dataset line, **AI-chat-link placeholders**; re-open every URL; fix dead links.
- [ ] **T11.2 Cross-check** slide 15 ⇔ `references.txt` ⇔ `research/sources_log.md` ⇔ `[n]` tags (via `check_submission.py`).
- [ ] **T11.3 Draft the AI-survey answers** in `docs/UNDERSTANDING_AR.md` (PRD §13) with the reminder: Q4 honest; no transcripts/personal data.
- [ ] **T11.4 Phase wrap-up** (commit, tag `phase-11-done`).

## Phase 12 — Human-Understanding Pack  (type: `docs`)
- [ ] **T12.1 Glossary** (PRD §14 list) in Arabic with English terms.
- [ ] **T12.2 Numbers cheat-sheet:** every slide number → value · notebook section · meaning · sensitivity.
- [ ] **T12.3 Interview Q&A:** ≥ 30 questions (technical, business, ethics, limitations, "why not a better model?", "why this threshold?", "why re-basing?", "how did you use AI?") + 2-minute story.
- [ ] **T12.4 Self-test:** 20 questions with answers at the end (take it before survey Q4).
- [ ] **T12.5 Re-run guide:** exact commands/clicks (local with the venv, and Colab); how to rebuild charts and export the PDF.
- [ ] **T12.6 Phase wrap-up** (commit, tag `phase-12-done`).

## Phase 13 — Final QA and packaging  (type: `qa`)
- [ ] **T13.1 Requirements audit R1–R7** with evidence pointers (slide/section numbers) written into `docs/NOTES.md → Decision log`: R1 recommendation slide title states the decision + impact slide has numbers · R2 EDA charts specific to Company A + hypotheses · R3 model name/metric/result as **text** + why/how/learned · R4 documented market analysis with verified sources · R5 plain-language diagram + jargon defined · R6 multiple purposeful charts · R7 titles-only story coherent.
- [ ] **T13.2 Honesty audit:** search slides/notebook for causal language ("because", "causes", "drives") and revise to "indicator/hypothesis" unless tested; confirm "course project / estimated under assumptions" wording; no real-client claims.
- [ ] **T13.3 Privacy audit:** no CSV/keys/personal data in the notebook, `submission/`, or git history; Drive images private again; no remote configured.
- [ ] **T13.4 Package `submission/`:** copy the final `Islam-Raad.pdf`, the **executed** `Islam-Raad.ipynb` (outputs visible) and `references.txt` (exact names). The folder must contain **exactly these three files and nothing else**. Extend `scripts/check_submission.py` to fail if any other file is present, to confirm the notebook in `submission/` runs end-to-end from a clean kernel (it finds the data via `../telecom/`), and that PDF ⇔ `references.txt` ⇔ notebook numbers agree.
- [ ] **T13.5 Final clean run:** fresh kernel run of the notebook; rebuild/re-export PDF if charts changed; re-run `check_submission.py` — all pass.
- [ ] **T13.6 Submission steps for Islam** (in `docs/UNDERSTANDING_AR.md`): confirm the live Omnicampus course page; attach **all three** items every time; paste references (with the real AI chat links); answer the AI survey honestly; press the green **Submit**; reopen the page to verify status and attachments; **submit ≥ 1 day before 28 Nov**; re-submission before the deadline is allowed but must re-attach everything; no edits after the deadline.
- [ ] **T13.7 Final hand-off:** update `PROGRESS.md` with "ALL DONE" + the three things Islam reads first (§ numbers in the Understanding Pack); final commit; `git tag final-submission-ready`.
- [ ] **T13.8 Keep/delete guide for Islam** (print it in the final message and save it at the top of `docs/UNDERSTANDING_AR.md`). **Do NOT delete anything yourself.** Explain in Arabic: (1) **hand in** only `submission/` (3 files); (2) **keep** `docs/UNDERSTANDING_AR.md` (his study material; he needs it for the interview and survey Q4) and a backup copy of `submission/`; (3) **keep until he finishes verifying** `telecom/` and the notebook (needed to re-run/check numbers) and the Google Slides deck (editable source of the PDF; re-export if any change is needed); (4) **optional** `.git` history; (5) **safe to delete** everything else (`outputs/`, `research/`, `scripts/`, `docs/NOTES.md`, `PROGRESS.md`, the course documents, `tasks.md`, `prd.md`). Remind him that deleting `telecom/` means he can no longer re-run the notebook locally and that re-submission needs all three files again.

---

### Decision rules when blocked
- A source can't be verified → drop it and find another.
- Thresholds fail robustness → Lane 2 becomes a monitoring hypothesis; core = risk ranking + value-at-risk (log it).
- A package is missing → install it into the same venv (log) or use a fallback (e.g., `HistGradientBoostingClassifier`).
- Google Slides integration can't do an operation → use the PRD §11.1 fallback and record it in `PROGRESS.md`.
- Conflict between sources → follow PRD §0.4 precedence and log it.
