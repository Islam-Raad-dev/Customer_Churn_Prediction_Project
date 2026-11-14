# PRD v2 — GCI World 2026 Final Assignment
## "Company A" Telecom Churn — Data-Driven Business Proposal (PoC)

> **Audience:** an autonomous agent (Google Antigravity, Gemini) that builds the *entire* project: data audit, EDA, market research, modeling, business-impact model, Google Slides deck → PDF, one reproducible notebook, references, and a Human-Understanding Pack.
> **Owner / submitter:** Islam Raad (AI Engineering student, University of Mosul). He reviews and fully understands every step before submitting. **Omnicampus account name: `Islam-Raad`.** He alone clicks Submit.
> **Companion file:** `tasks.md` (ordered, checkable steps). This PRD = *what and why*; `tasks.md` = *what to do next*.
> **Deadline:** Saturday **28 Nov 2026, 11:30 UTC (14:30 Iraq, UTC+3)**. No late submission. Re-submission before the deadline is allowed (last one is graded; **all files must be re-attached every time**).
> **Pace:** there is no time pressure on the work itself. Execute **every phase, in order, one step at a time, with full quality.** No "MVP", no skipping.

---

## 0. Working protocol (read this first, obey always)

### 0.1 Environment — use the existing virtual environment
- Use **only** this interpreter for everything (scripts, notebook kernel, pip): `/home/islam-raad/ai_workspace/bin/python3.12`
  (pip: `/home/islam-raad/ai_workspace/bin/python3.12 -m pip …`; Jupyter: `/home/islam-raad/ai_workspace/bin/python3.12 -m jupyter …`).
- **Do not create a new venv/conda env.** First run `… -m pip list` and check which packages exist. Install a package **only if missing**, into this same env, and log it in `docs/NOTES.md`. **Never upgrade/downgrade existing packages** (it could break his other work).
- Needed: `pandas, numpy, scikit-learn, xgboost, matplotlib, scipy, jupyter/nbconvert, nbformat, joblib`. Optional (guarded imports with fallback): `lightgbm, shap`. **Do not use** seaborn, plotly, altair, bokeh or any plotting library other than matplotlib (see §10).
- Notebook kernel must be that interpreter. Record versions in `outputs/results.json → meta.versions`.

### 0.2 Resume protocol (so a sudden stop never forces a full re-read)
**`PROGRESS.md` (repo root) is the single resume file.** It must always contain:
```
# PROGRESS
Updated: <YYYY-MM-DD HH:MM>
Last completed task: T<id> — <title>
Current task: T<id> — <title>   | status: [~] in progress (what is already done inside it)
Next concrete action: <1–3 lines>
Key decisions so far: <≤10 bullets>
Key numbers so far (from results.json): <≤15 lines>
Files produced so far: <paths>
Google Slides: <presentation URL/ID, or "not created yet">
Open issues / assumptions pending: <bullets>
```
Rules:
1. **On start or after ANY interruption, read ONLY:** `PROGRESS.md` → the *single* next task block in `tasks.md` (search by ID) → only the PRD section number that task cites → `git log --oneline -10`. **Do not re-read all files.** (Re-read a document only when a task explicitly says so.)
2. **Task status marks in `tasks.md`:** `[ ]` not started · `[~]` in progress (add one indented line saying what is done) · `[x]` done, followed by ` ✔ YYYY-MM-DD HH:MM`.
3. **A task counts as done only when all five hold:** (a) its outputs exist and were verified by reading real outputs; (b) the matching section of `Islam-Raad.ipynb` is added/updated and runs; (c) `tasks.md` mark set to `[x] ✔ <timestamp>`; (d) `PROGRESS.md` rewritten; (e) a git commit was made (§0.3). **Order: work → verify → tick → update PROGRESS.md → commit.**
4. Long tasks (modeling, slide building): set `[~]`, add sub-state lines, and make `wip(...)` commits so nothing is lost.
5. If `PROGRESS.md` is missing or stale (e.g., Phase 0 was started earlier), **reconstruct it** from existing files, `git log` and notebook state, then continue from the first unchecked task.

### 0.3 Git — local version history, one clean commit per step
- Phase 0 initializes a **local** repo in the workspace (`git init`, branch `main`). **Never add a remote and never push** (data/course materials are not public).
- Use the existing global git identity if set; otherwise set repo-local `user.name "Islam-Raad"` and `user.email "islam-raad@users.noreply.local"`.
- `.gitignore` must contain: `telecom/*.csv`, `*.docx`, official course PDFs, `tutorial.ipynb`, `outputs/models/`, `*.joblib`, `.ipynb_checkpoints/`, `__pycache__/`, `.DS_Store`, any credentials/keys. **Never commit the CSVs, keys or personal data.** Before every commit run `git status` and confirm nothing forbidden is staged.
- **One commit per completed task** (plus optional `wip` commits). Message format:
  ```
  <type>(<phase>): <TaskID> <imperative summary, ≤72 chars>

  What: <1–2 lines>
  Result: <key numbers/verdict, if any>
  Files: <main paths>
  ```
  Types: `chore, data, eda, research, feat, model, eval, impact, notebook, slides, docs, qa, fix, wip`.
  Example: `eda(phase2): T2.2 test robustness of the ~300-day device-age jump` … `Result: churn 37.6% → 54.7%; bootstrap CI excludes 0; verdict: real-looking (hypothesis)`.
- Tag at the end of each phase: `git tag phase-<n>-done`. Fix mistakes with a new `fix(...)` commit or `git revert`; do not rewrite history.

### 0.4 Source-of-truth precedence
1. `README.docx` (official rules) · 2. `final_assignment_tutorial.pdf` + `tutorial.ipynb` (reference, not a template) · 3. `ENG_Company_A_Dataset Overview.docx` (some descriptions wrong/vague, §5.3) · 4. The actual data (`telecom/*.csv`) — ground truth for any number · 5. `GCI_Final_Assignment_Guide.pdf` (prior analysis by Claude — **calibration hints only; recompute every number**).
If a requirement appears in those files but not here, **the file wins**; log it in `docs/NOTES.md → Decision log`. Reading hints: `pandoc README.docx -t plain`, `python-docx`, `pdftotext -layout`.
If you need information not in this PRD → look in those files, then the data, then the web (external market facts only). Do not guess.

### 0.5 Integrity rules (non-negotiable)
1. **Never fabricate.** Every metric comes from code you ran and output you read. Every external number comes from a source you actually opened (log publisher, publication date, access date).
2. **One source of truth for numbers:** the notebook writes `outputs/results.json`; slides take numbers only from it; `scripts/check_submission.py` verifies the exported PDF against it.
3. **No leakage** (§8). The 30% test split is for final reporting only.
4. **Honest framing:** a *course project*, not a real engagement. Impact = *estimate under stated assumptions*. Causes = *hypotheses* unless tested.
5. **Cite everything borrowed.** Direct quotation target ≈ 0% (hard cap < 40%); paraphrase + cite; quotes ≤ 15 words and only if essential.
6. **Privacy:** never upload CSVs or paste data rows into external tools; no API keys/personal data in the notebook; nothing public. Aggregate charts only go to Google Drive/Slides.
7. **Reproducibility:** `random_state=42`, relative paths, Restart-and-Run-all passes.
8. **Do not interrupt the human** for choices: use the PRD default, log it, continue. Ask only for: AI-chat links and the final submission click.
9. **Work in verified steps:** run → read output → decide → log.

---

## 1. Context and objective
**Scenario (official):** a new *Associate* at an IT-consulting firm; the sales team won a **Proof-of-Concept** from **Company A**, an anonymous wireless telecom with ~100,000 customers' data and no ML team. Deliver: EDA, **≥ 1 ML model**, the client's **core problem** (from evidence + market analysis), and a **data-driven business proposal** with a **quantified estimated impact** (revenue ↑, cost ↓, or risk ↓).

> **The model supports a recommendation; it is not the recommendation.** "We built a model with X% accuracy" is a technical report and fails requirement R1. The deck must answer: *What is the problem? Why do we believe it (data + market)? What should the company do, for whom, when? How much will it gain/save under which assumptions, and how sure are we?*

**Goal:** a submission that is compliant, analytically honest, understandable by a non-ML manager, visually world-class, reproducible, and **fully understood by Islam**.
**Non-goals:** maximizing accuracy (cap tuning at ~20 min); deployment/dashboards; external customer data.

---

## 2. Deliverables and hard constraints

### 2.1 Files to submit (Omnicampus; Islam confirms the live course page — the README mentions the "170 course" page; some tutorial screenshots are from an older cohort)
| # | File | Rules |
|---|---|---|
| 1 | **Slides PDF** `Islam-Raad.pdf` | ≤ **15 slides** total (title, dividers, references included; extras may be ignored); ≤ **10 MB**; **made in Google Slides, exported to PDF** |
| 2 | **References** → `references.txt` (pasted into the Omnicampus "References" field) | One link/reference per line; **must match** slide citations; **paste AI chat link(s)** if generative AI was used |
| 3 | **Notebook** `Islam-Raad.ipynb` (or `.py`/`.zip`) | Reproducible, end-to-end; **self-contained single notebook** (helper functions live inside it) so no zip is needed |
- Also complete the **AI-usage survey** (draft §13). Do **not** submit the CSVs.

### 2.2 The 7 grading requirements
| # | Requirement | Evidence in this project |
|---|---|---|
| R1 | Business **proposal**, not a technical report | "Recommendation" slide titled with the decision + "Estimated impact" slide with numbers |
| R2 | **Real EDA** on this data, client-specific challenges | 4–6 purpose-built charts + 3 written hypotheses |
| R3 | **≥ 1 model**; **name, metric, result as live text**; why chosen, how built, what learned | Experiments table as a native Google Slides table (text) |
| R4 | **External sources & market analysis, documented** | ≥ 8 verified sources, `[n]` footnotes, matching reference list |
| R5 | Understandable to a **manager without ML background** | Plain headlines, "how it works" diagram, jargon defined |
| R6 | **Multiple charts** (not raw numbers) | One purposeful matplotlib chart per key idea |
| R7 | **Logical consistency** | problem → analysis → model → recommendation → impact, each slide answers the previous slide's question |
Notes: an obviously unsuitable model type does not count for R3; comparing several models is preferred. Honors/Outstanding depend on overall rankings with no published formula → only strategy: meet all 7 at high quality.

### 2.3 Citation & AI rules
Cite any external data/method/figure/text (even paraphrased); extra public data allowed if cited and its effect explained; slide footnote **and** reference list must match. AI output alone isn't "own work"; chat link is mandatory in references; organizers confirmed (via Islam, on Slack) that full AI use is fine **as long as he understands everything** → the Understanding Pack (§14) is required.

---

## 3. Workspace (lean by design — do NOT create extra files)
**Project root = the folder opened in Antigravity** (a fresh folder created by Islam; do not assume any fixed path; use **relative paths only**).
The fresh folder starts with exactly these files (do not modify them): `prd.md`, `tasks.md`, `telecom/Client.csv`, `telecom/Record.csv`, `ENG_Company_A_Dataset Overview.docx`, `final_assignment_tutorial.pdf`, `GCI_Final_Assignment_Guide.pdf`, `README.docx`, `tutorial.ipynb`. Start from scratch; do not look for or reuse files from any older folder.
**End-state rule:** when everything is verified, the folder `submission/` must contain **exactly three files** — `Islam-Raad.pdf`, `Islam-Raad.ipynb`, `references.txt` — and nothing else (no data, no images, no docs), so Islam can hand in that folder and delete the rest. The agent **never deletes** project files itself; it produces a keep/delete guide instead (tasks.md T13.8).
The agent maintains **only** these:
```
Final Assignment/
├── PROGRESS.md                  # resume file (§0.2)
├── prd.md, tasks.md             # do not edit content; tick marks in tasks.md only
├── Islam-Raad.ipynb             # THE notebook, built progressively, always runnable
├── outputs/
│   ├── figures/                 # matplotlib PNGs only (200 dpi)  fig_<slide>_<topic>.png
│   ├── tables/                  # experiment_log.csv, test_predictions.csv (only these)
│   ├── results.json             # SINGLE SOURCE OF TRUTH for numbers
│   └── models/                  # final model (.joblib, git-ignored)
├── research/sources_log.md      # every external source
├── docs/
│   ├── NOTES.md                 # sections: Decision log · Assumptions · Hypotheses · Feature dictionary · Data-doc discrepancies · Slides IDs
│   └── UNDERSTANDING_AR.md      # Arabic pack (§14), appended phase by phase
├── scripts/check_submission.py  # one script: PDF pages/size/text, numbers vs results.json, refs match
└── submission/                  # Islam-Raad.pdf, Islam-Raad.ipynb, references.txt
```
- **Not allowed:** separate stub/log files (work_log, decision_log, assumptions, digest, checklists, handoff…), `src/` modules, per-step markdown reports, duplicate notebooks, scratch dumps. Put such content as **sections inside `docs/NOTES.md`** or in `PROGRESS.md`.
- If extra files already exist from an earlier step, **consolidate** them (task T0.7) and delete the leftovers.
- `Islam-Raad.ipynb` runs locally and on Colab. `DATA_DIR` auto-detection tries, in order: `./telecom/`, `../telecom/` (works when the notebook sits in `submission/`), then Colab `/content/drive/MyDrive/Final Assignment/telecom/`; if none exists it stops with a clear message listing the two expected CSVs. Runtime < ~10 min; no web calls; no keys.

---

## 4. Definition of done (whole project)
1. All 7 requirements pass the checklist (tasks.md Phase 13). 2. `Islam-Raad.ipynb` passes *Restart & Run all* (nbconvert) and regenerates the same `results.json`. 3. `check_submission.py` reports 0 problems. 4. PDF ≤ 15 pages, ≤ 10 MB, every slide visually inspected, numbers legible. 5. Slide `[n]` tags ⇔ `references.txt` ⇔ `research/sources_log.md`, all URLs opened. 6. `docs/UNDERSTANDING_AR.md` covers every phase, slide, number, assumption. 7. Impact model has scenarios, sensitivity, break-even and the **49.6% realism adjustment** (§9.4). 8. Git history is clean: one meaningful commit per task, phase tags. 9. `submission/` contains **exactly** the three files (§3), the notebook inside it was executed end-to-end (outputs visible) from a clean kernel, and the PDF/notebook/references are mutually consistent. 10. The keep/delete guide for Islam exists (T13.8).

---

## 5. Data specification

### 5.1 Structure (verified earlier; re-verify)
- `Client.csv`: 100,000 × 50 (`Customer_ID` + 49 features; 21 text, 28 numeric). `Record.csv`: 100,000 × 51 (`Customer_ID` + 49 numeric features + `churn`).
- Key: `Customer_ID` (some docs say `ID_Customer`; **use the real column name**). Perfect 1-to-1, IDs 1000001–1100000, no duplicates. Merged: **100,000 × 100** (confirmed in Islam's run) → 98 features + ID + target.
- **Target `churn`:** left within **31–60 days after the observation date**; **≈ 49.56% churn vs 50.44% stayed** → unrealistically balanced (real ≈ 5–10% per the tutorial); sample likely resampled (reason undocumented). Raw precision/recall and money estimates on this sample are **overstated** → §9.4.
- `months` (tenure) is in `Record.csv` (not Client); range ≈ 6–61, median ≈ 16; nobody < 6 months. **Always print `df.columns` after merging.**

### 5.2 Column map (names indicative; verify)
Account (`actvsubs, uniqsubs, new_cell, crclscod, asl_flag`) · Device (`eqpdays, hnd_price, models, phones, refurb_new, hnd_webcap, dualband`) · Lifetime history (`totcalls, totmou, totrev, adjrev, adjmou, adjqty, avg*, avg3*, avg6*`) · Tenure (`months`) · Monthly revenue/usage (`rev_Mean, mou_Mean, totmrc_Mean, da_Mean, ovrmou_Mean, ovrrev_Mean, vceovr_Mean, datovr_Mean, roam_Mean, change_mou, change_rev`) · Call quality (`drop_*, blck_*, unan_*, plcd_*, recv_*, comp_*, attempt_Mean, complete_Mean, drop_blk_Mean`) · Care/patterns (`custcare_Mean, ccrndmou_Mean, cc_mou_Mean, callwait, callfwdv, threeway, inonemin`, peak/off-peak, `iwylis_vce_Mean`) · Demographics (`prizm_social_one, area, truck, rv, ownrent, lor, dwlltype, marital, adults, infobase, income, numbcars, HHstatin, dwllsize, forgntvl, ethnic, kid0_2…kid16_17, creditcd`) · Target (`churn`).

### 5.3 Data-quality hints (recompute!)
- **Missing:** `numbcars` ≈ 49%; `dwllsize, HHstatin, ownrent, dwlltype` ≈ 32–38%; `lor, income, adults, infobase` ≈ 22–30%; `hnd_webcap, prizm_social_one` ≈ 7–10%; `avg6*` ≈ 2.8%; a ≈ 1.7% block (~1,732 rows) missing across the same demographic columns; rows with missing `change_mou/change_rev` (~0.9%) churn ≈ 76% → **missingness can carry signal**.
- **Near-duplicates** (Spearman > 0.97, ~20 pairs, e.g. `totcalls~adjqty`, `totmou~adjmou`, `totrev~adjrev`, `attempt_Mean~plcd_vce_Mean`, `comp_vce_Mean~complete_Mean`); dropping 10 didn't change AUC (≈ 0.696).
- **Near-empty (≥ 97% zeros):** `callfwdv, recv_sms_Mean, blck_dat_Mean, drop_dat_Mean, unan_dat_Mean`; many data-call columns 85–93% zeros.
- **Odd values:** `eqpdays` has negatives (~133), `rev_Mean` ~5 negatives, `totmrc_Mean` ~23 negatives, `uniqsubs` max ≈ 196, `price_hnd` has ~17 distinct values (price tiers). The tutorial's pairplot raised `log1p` warnings → negatives/−1 values → handle explicitly (clip/flag/exclude) and log.
- **Doc vs data:** `change_mou/change_rev` are documented as *percent change* but ≈ 22.6% of `change_mou` < −100 (impossible for a percentage) and they track `mou_Mean − avg3mou` / `rev_Mean − avg3rev` (ρ ≈ 0.90–0.94) → treat as **absolute change vs previous 3-month average**; say "change in minutes/revenue", not "%". `recv_sms_Mean`, `iwylis_vce_Mean` undocumented.
- **Units:** no currency documented → write **monetary units (MU)**.

### 5.4 Calibration targets (re-run; never copy)
Tutorial config (LabelEncoder; `XGBClassifier(n_estimators=300, learning_rate=0.05, max_depth=6, eval_metric='logloss', random_state=42)`; stratified 70/30; seed 42): **accuracy ≈ 0.636** (Islam's run: **0.6357**), majority baseline ≈ 0.504, **AUC ≈ 0.694**, train accuracy ≈ 0.735 (overfit). ≥ 0.80 accuracy → suspect leakage; ≈ 0.50 → suspect a broken join. 5-fold CV AUC ≈ 0.697 → ≈ 0.7015 with ~17 engineered features; tuning ≈ +0; logistic regression ≈ 0.657; fold std ≈ 0.002–0.004 (differences < ~0.003 are noise). Prior top-k precision (sample base 49.6%): top 5% ≈ 85%, 10% ≈ 80% (lift ≈ 1.6), 20% ≈ 74%, 30% ≈ 70%, 50% ≈ 64%; bottom 10% churn ≈ 18%. Gain importance is flat (top ≈ 4.6%) → modest AUC expected.

### 5.5 Patterns to **test** (hypotheses, not facts)
1. **Device age ≈ 300 days:** churn ≈ 37–38% up to 300 days → ≈ 55% just above → peak ≈ 64% at 321–340. Causes unknown (upgrade eligibility, commitment end, or sampling artifact).
2. **Tenure months 10–12:** ≈ 29% at month 9 → ≈ 40% at 10 → ≈ 65% at 11 → ≈ 62% at 12 → ≈ 47% at 37+.
3. **Entanglement:** nobody with ≤ 9 months has a device > 300 days → separate effects (compare within tenure ≥ 10).
4. **Usage collapse:** `mou_Mean == 0` (~1,600) churn ≈ 80%; ≤ 10 ≈ 65%; missing `change_mou` ≈ 76%; check revenue share.
5. **Revenue doesn't separate classes** (mean `rev_Mean` ≈ 58.2 vs 59.2) → "valuable" ≠ revenue alone.
6. **More customer-care calls → less churn** (counter-intuitive) — don't claim causation.
7. **`ethnic`** differs strongly — never use for targeting (§8.7).
8. Demographics weak (48–51%); `infobase` appeared in importance — check meaning.

---

## 6. Strategy

### 6.1 Candidate framings (score in a decision matrix: evidence, actionability, measurability, risk, market fit)
A **Risk-ranked retention** (classification/ranking) · B **Lifecycle triggers** (device-age/tenure thresholds) · C Early warning on usage drop · D **Value-at-risk** (P(churn)×value) · E Segmentation (clustering; needs action mapping).

### 6.2 Default proposal (confirm or adjust at the Decision Gate, T4.2)
**A two-lane retention program:** **Lane 1** — monthly risk score; the retention team contacts only the riskiest k% (k chosen by net value, ranked by value-at-risk). **Lane 2** — lifecycle triggers: offer a device refresh before devices pass ~300 days; a loyalty check before the tenure cliff (~month 9–10); both launched as **A/B pilots with a holdout**.
Draft problem sentence: *"Company A loses customers it could keep, but retention spend is untargeted. Risk concentrates in identifiable moments (aging devices, early-tenure cliff, collapsing usage). We propose monthly scoring and timed, value-aware offers, validated by a controlled pilot."* Task type: supervised binary classification + rule-based triggers; action owner: retention/CRM; KPI: incremental retention in the pilot.
If thresholds **fail robustness** (T2.2) → Lane 2 becomes "monitoring hypotheses"; core = Lane 1 + value-at-risk. Log it.

### 6.3 Market lens
Use **Iraq's mobile market** (Zain Iraq, Asiacell, Korek; regulator CMC; ITU/GSMA/DataReportal) as the lens the tutorial rewards ("a local market you can describe concretely"). State explicitly that Company A is anonymous and its data are **not claimed to be Iraqi**. Use only verified numbers; where local numbers don't exist say so and label regional/global ones.

---

## 7. Market research (Phase 3)
Answer with citations: (1) market state (subscribers, penetration, players, shares); (2) local churn drivers (competition, multi-SIM, price/regulation, network quality, 5G/eSIM); (3) retention vs acquisition economics; (4) voluntary vs involuntary churn and what a model can influence; (5) handset-upgrade/commitment cycles vs churn; (6) retention-campaign success rates/offer costs (else label ASSUMPTION); (7) ≥ 1–2 credible papers on telecom churn prediction (why tree models on tabular data).
Bar: **≥ 8 sources** (regulator/ITU/GSMA/operator reports/credible media/peer-reviewed), prefer primary; **open each URL and verify the fact**; log in `research/sources_log.md` (ID · title · publisher · publication date · URL · access date · fact used · reliability note); `[n]` tags on slides.

---

## 8. Methodology

### 8.1 Data audit & preparation
Shape/dtypes/missingness/duplicates/ID checks/outliers/negatives/near-duplicates/zero-heavy columns/doc-vs-data (§5.3); log every decision. **Encoding:** compare tutorial `LabelEncoder` (turns `NaN` into the string `'nan'`, imposes order) vs leakage-safe alternatives (native categorical XGBoost `enable_categorical=True`, or ordinal/one-hot inside a `Pipeline`). **Missing:** trees take `NaN`; for logistic regression impute (median) **inside the pipeline** + missing flags; add `n_missing_demographics`. **Negatives/outliers:** decide per column, document why.

### 8.2 EDA (each = one matplotlib chart + one-sentence finding; thresholds discovered on the **training split only**)
Target balance · missingness + churn-when-missing · **`eqpdays` bins ≤ 25 days** with CI · **robustness of the ~300-day jump** (bootstrap CI of churn(301–340) − churn(260–300); local linear fit each side; repeat within tenure ≥ 10, `area`, `crclscod`; **covariate-balance check** at 300 days on `rev_Mean, hnd_price, months, mou_Mean, uniqsubs` — many covariates jumping ⇒ suspect sampling artifact) · `months` curve 6–61 · tenure×device heat-map with counts · usage-collapse segments (size, churn, revenue share) · revenue vs churn · care calls vs churn · quality/overage/roaming vs churn · demographics (+ethics note) · correlations/duplicates.
Outputs: **4–6 final charts** (slides 4–6) + **3 hypotheses** as full sentences ("Segment X is more likely to churn because Y; we test with Z"), ranked by actionability.

### 8.3 Feature engineering (hypothesis before experiment; ≥ 10 candidates, keep what helps or explains)
`dev_age_gt_300`, `tenure_le_9`, `tenure_10_12`, `eqp_per_tenure` · usage trend (`mou_Mean/avg3mou`, `mou_Mean/avg6mou`, `rev_Mean/avg3rev`, `rev_Mean/avg6rev`, `change_mou/change_rev`) · quality rates (`drop_rate, block_rate, unanswered_rate, completion_rate`) · economics (`recurring_share=totmrc_Mean/rev_Mean`, `overage_share`, `roam_share`) · care (`custcare_per_call`, `has_custcare`) · zero-usage flags · missingness flags. Document name · formula · business reason · leakage check in `docs/NOTES.md → Feature dictionary`. **Leakage rule:** computable before the churn window; never from `churn`; target statistics only inside CV folds.

### 8.4 Modeling protocol
Stratified **70/30**, seed 42 (as the tutorial). **5-fold stratified CV on the 70% only** for all selection. **Test set touched only for final candidates (≤ 2, logged).** Models (≥ 4): M0 majority baseline · M1 logistic regression (pipeline) · M2 shallow decision tree (depth ≤ 4, *explanation device*) · M3 XGBoost tutorial params · M4 XGBoost + engineered features · M5 XGBoost tuned (≤ 30 random configs, ≤ 20 min) · optional M6 LightGBM/RandomForest. Metrics: **ROC-AUC (primary)**, precision/recall/lift at top-k%, accuracy (comparability), F1, confusion matrix, calibration; report CV mean ± std and test score; train–test gap; log in `outputs/tables/experiment_log.csv`. Accuracy ≥ 0.75 or AUC ≥ 0.80 ⇒ hunt leakage. Final model = best CV AUC; ties within 1 std ⇒ simpler.

### 8.5 Interpretation
Gain **and** permutation importance (held-out) — explain gain ≠ weight; partial dependence for `eqpdays`, `months`; ablation (drop top feature, retrain); per-driver **lever table** (can the company change it?); cautious wording ("indicator", not "cause"). Optional SHAP.

### 8.6 Decision evaluation
Confusion matrix at a stated threshold (FP = wasted offer; FN = lost customer); **top-k table** k ∈ {1,2,5,10,15,20,30,50} with precision, recall, lift, customers; gain/lift curve; calibration (isotonic on a validation fold if probabilities enter money terms).

### 8.7 Ethics & fairness
Exclude `ethnic` from the final model; test excluding other proxies (`income, marital, kid*, dwllsize`) and report the AUC change; state on the risks slide: *"We target on behavior, not identity."*

---

## 9. Business-impact model
### 9.1 Formula
`Net = n × p_adj(k) × s × V − n × c`, with `n = k × N` (N = 100,000, stated), `p_adj` = precision in top-k after realism adjustment, `s` = retention-action success rate, `V = ARPU × margin × H` (ARPU from `rev_Mean` mean & median; margin and H are assumptions), `c` = cost per *targeted* customer (paid for everyone targeted, even those who would have stayed). The tutorial's toy example is for method explanation only.
### 9.2 Scenarios
Conservative / base / optimistic; vary `s, c, V (margin, H)` and the realistic churn prior; every input flagged **SOURCED [ID]** or **ASSUMPTION** in `docs/NOTES.md → Assumptions`.
### 9.3 Sensitivity & optimum
Tornado over `s, c, V, π_real, k`; net-vs-k curve → **k\***; **break-even** `s* = c / (p_adj × V)`. **Lane 2:** window size (e.g., customers 240–300 days) × observed churn gap × share of gap an offer could close (scenarios), labelled *hypothesis → pilot*, with pilot design (treatment/holdout, duration, KPI = incremental retention).
### 9.4 Realism adjustment for 49.6% (mandatory)
Label-shift re-weighting: positives × `π_r/π_s`, negatives × `(1−π_r)/(1−π_s)` (π_s ≈ 0.4956; π_r ∈ {5%, 10%}, cited); compute **weighted precision@k and lift@k** on test predictions; show *raw sample* vs *re-based* side by side. Unit-test the function on a toy example.
### 9.5 Never claim
Guaranteed savings · causal language for thresholds · sample precision as real-world precision · money without units (MU) and source.

---

## 10. Charts — **matplotlib only**
**Every chart and diagram in the project (slides and notebook) is created exclusively with `matplotlib`** (direct `plt`/`ax` API). **Forbidden:** seaborn, plotly, altair, bokeh, pandas `.plot()` shortcuts, Google Slides native charts, charts drawn from shapes. Conceptual diagrams (data-to-decision flow, "how the model works", two-lane program) are also drawn with matplotlib patches (`FancyBboxPatch`, `FancyArrowPatch`, `Circle`) and exported as PNG. Tables are native Google Slides tables (live text), not images.

**Style (implement once as a helper section inside the notebook and reuse):**
- Exact placement size: create each figure at the size it will have on the slide, so 1 pt in the figure = 1 pt on the slide. Standard sizes (inches): **full width 9.0 × 3.6**, **half width 4.4 × 3.3**, **wide-short 9.0 × 2.4**, **square-ish 4.4 × 4.0**.
- `fig.savefig(path, dpi=200, facecolor="white")` with `constrained_layout=True` (**no `bbox_inches="tight"`**, it changes the size). PNG only. Name `fig_<slide#>_<topic>.png`.
- rcParams: font family `["Open Sans","DejaVu Sans"]` (use Open Sans if installed, else DejaVu; log which), base size 11, axis labels 11, ticks 10, legend 10, annotations 10–11 (never < 10 pt at placed size), line width 2.2, markers 5–6.
- Look: white background, no top/right spines, light horizontal grid (`#D9E0E7`, 0.8 pt), no chart junk, **direct labels instead of legends where possible**, annotate the key insight (e.g., dashed vertical line + text at ~300 days), units in axis labels, thousands separators, percent formatting, sensible limits (don't truncate bar axes), sample size `n=` in a small caption.
- **Color roles (identical in every chart):** churn = coral `#E4572E`; stayed/baseline = blue `#3B7DD8`; highlight/accent = teal `#0F8B8D`; callout = amber `#F2A541`; neutral text `#1F2933`; secondary `#5B6B7B`; grid `#D9E0E7`. Colorblind-safe (coral vs blue, never red vs green). Sequential heat-maps use one hue (white→teal) via `LinearSegmentedColormap`.
- No chart title duplicating the slide title; a short in-figure subtitle only if needed. Every chart has axis labels with units.
- QA: open every PNG (`view`) before using it; reject overlapping labels, clipped text, unreadable fonts.

---

## 11. Slides — built in **Google Slides** (connected inside Antigravity)

### 11.1 Workflow
1. **T10.1 capability probe:** use the connected Google Slides/Drive integration to (a) create a presentation, (b) set page size, (c) add a text box, a table, a shape, (d) insert an image from a URL/Drive file, (e) read a slide thumbnail, (f) export to PDF. Log which operations work in `docs/NOTES.md → Slides`.
2. Create presentation **"Islam-Raad — GCI Final Assignment"**; keep its URL/ID in `PROGRESS.md` and `docs/NOTES.md`.
3. **Images:** matplotlib PNGs (200 dpi) must be reachable by the Slides API (Drive file or public URL). Upload PNGs to a Drive folder via the Drive integration, make them link-viewable only while inserting, embed, then **revert sharing to private** (the images are copied into the deck). Aggregate charts only; never raw data.
4. **Fallbacks (if an operation is unsupported):** (a) build the deck with `python-pptx` (same layout spec) and tell Islam to import it into Google Slides (File → Import slides) — then continue in Slides; (b) deliver an exact placement list (slide · file · x/y/w/h in pt) for manual insertion. Report the limitation in `PROGRESS.md`.
5. Build, inspect every slide via thumbnails, fix, export **PDF** (Drive export `application/pdf`, or Islam: File → Download → PDF), save to `submission/Islam-Raad.pdf`, run `scripts/check_submission.py`.

### 11.2 Canvas, grid, geometry (Google Slides 16:9 = 10 in × 5.625 in = 720 × 405 pt; 1 pt = 12,700 EMU; page 9,144,000 × 5,143,500 EMU)
| Zone | x (pt) | y (pt) | w × h (pt) |
|---|---|---|---|
| Section tag (teal, 10 pt caps) | 36 | 14 | 300 × 14 |
| **Title** (≤ 2 lines) | 36 | 30 | 648 × 58 |
| Content area | 36 | 100 | 648 × 262 |
| Footnote / source (9 pt) | 36 | 380 | 560 × 14 |
| Slide number (9 pt, right) | 640 | 380 | 44 × 14 |
Margins 36 pt; gutter between columns 18 pt; two-column split = 315 + 18 + 315 pt; vertical spacing multiples of 6 pt; everything left-aligned to the 36 pt edge. A short teal bar (36 × 3 pt) sits above each title as the only decoration. Keep ≥ 20% whitespace per slide.

### 11.3 Typography (all available in Google Slides)
| Role | Font | Size | Weight/color |
|---|---|---|---|
| Cover title | **Montserrat** | 34 pt | Bold, white on navy |
| Slide title | **Montserrat** | 26 pt (24 if needed; never smaller) | Bold, navy `#0B1F3A` |
| Section tag | Montserrat | 10 pt | Bold caps, teal |
| Body | **Open Sans** | 16 pt (min 14) | Regular, `#1F2933`; emphasis = Bold |
| Big numbers (KPIs) | Montserrat | 40–54 pt | Bold; teal (good), coral (risk) |
| Table header / cells | Open Sans | 12 / 12 pt | Header Bold white on navy; zebra rows `#F5F7FA` |
| Footnotes / sources | Open Sans | 9 pt | `#5B6B7B` |
Rules: ≤ 2 fonts in the deck; line spacing 1.15; paragraph spacing 6 pt; left-aligned (never justified); ≤ 3 bullets/slide, ≤ 14 words each; titles are **complete takeaway sentences** (≤ 14 words, ≤ 2 lines); numbers formatted consistently (thousands separators; one decimal for %).

### 11.4 Color and shapes
Backgrounds: slides white `#FFFFFF`; cover navy `#0B1F3A`; panels/cards `#F5F7FA`. Palette as §10 (navy `#0B1F3A`, teal `#0F8B8D`, coral `#E4572E`, blue `#3B7DD8`, amber `#F2A541`, slate `#5B6B7B`, grid `#D9E0E7`). Shapes: **rounded rectangles** (corner radius ≈ 8 pt) with fill `#F5F7FA`, no outline (or 0.75 pt `#D9E0E7`), no shadows/gradients/3-D; **callout boxes** with a 4 pt teal left bar; numbered **circle badges** (teal, white Montserrat Bold 12 pt) for steps; thin arrows (1.5 pt slate) for flows. No clip-art, stock photos, emojis or external icon packs. Every shape aligns to the grid; equal gaps (12–18 pt).

### 11.5 Slide order (exactly 15; titles = takeaways; numbers from `results.json`)
| # | Slide | Content | Visual |
|---|---|---|---|
| 1 | **Title** — "Keeping customers before they leave: a data-driven retention proposal for Company A" | GCI World 2026 September — Final Assignment (course project) · Islam Raad · University of Mosul · date | Navy cover, teal bar |
| 2 | **Executive summary** | Problem · Recommendation · Estimated impact range (MU) + key assumption · confidence | 3 cards with big numbers |
| 3 | **Market context** — why churn is the profit lever | 3 sourced facts + Iraq lens + "Company A is anonymous" note | 3 KPI cards, footnotes `[n]` |
| 4 | **The data** — what we have and what it can't tell us | 100,000 customers · 98 features · 2 tables · churn 49.6% (why unrealistic) · quality highlights · what is missing | matplotlib missingness bars + structure diagram (matplotlib) |
| 5 | **EDA #1** — risk jumps once a device passes ~300 days (verify wording) | churn by device-age bin, robustness note, hypothesis + caveat | matplotlib line with annotated threshold |
| 6 | **EDA #2** — churn also spikes at months 10–12 and when usage collapses | tenure curve, entanglement note, zero-usage segment | 2–3 matplotlib small multiples |
| 7 | **Problem definition** — we rank customers by risk so offers reach the right people | one-sentence question · target · task type · owner · action · KPI | matplotlib flow diagram |
| 8 | **Features** — we turned raw columns into behavior and lifecycle signals | prep decisions + key features table (name · idea · why) | native table |
| 9 | **Experiments** — a boosted-tree model ranks churners best; tuning adds little | **native table (live text):** model · metric · CV ± std · test result; baseline; lessons | table + small matplotlib bar |
| 10 | **How it works (for managers) + what it learned** | plain-language diagram; top 3–5 drivers with "can the company change it?" | matplotlib diagram + importance bars |
| 11 | **Targeting power** — contacting the riskiest 10% finds X× more churners | confusion matrix in words · top-k table (raw vs re-based) | matplotlib lift/gain curve |
| 12 | **Recommendation** — launch a two-lane retention program | who · what · when · owner · pilot with holdout | matplotlib lane/timeline diagram |
| 13 | **Estimated impact** — under stated assumptions the program nets X–Y MU | formula in words · scenario table · break-even `s*` · k\* · raw vs re-based | matplotlib scenario bars + tornado |
| 14 | **Risks, ethics, next steps** | limits (balanced sample, no causality, no offer/cost data) · fairness choice · 90-day pilot · monitoring | risk matrix (native shapes/table) |
| 15 | **References** | numbered list identical to `references.txt` (incl. AI chat link line) | text |
Speaker notes (60–90 s) go into each slide's **native speaker-notes pane** (not exported) and are copied into `docs/UNDERSTANDING_AR.md`.

### 11.6 Deck quality gates
Titles-only read-through tells a coherent story · every chart has a takeaway · every number has unit/definition · jargon defined (AUC = "how well the model puts churners above stayers"; lift = "× better than random") · body text ≥ 14 pt, chart text ≥ 10 pt at placed size · contrast ≥ 4.5:1 · no overlaps/clipping (check **every** slide thumbnail) · model name/metric/value are selectable text in the exported PDF (`pdftotext`) · `check_submission.py` passes.

---

## 12. Notebook specification (`Islam-Raad.ipynb`)
Sections mirror the slides: 0 Overview (purpose, folder structure, how to run, AI statement) · 1 Setup (seed, paths, versions, **matplotlib helper functions**) · 2 Load & merge (assertions) · 3 Data audit · 4 EDA (+ robustness) · 5 Problem definition (text) · 6 Preprocessing & features · 7 Modeling (experiment log) · 8 Evaluation & interpretation · 9 Business impact (assumptions cell with sources, scenarios, sensitivity, re-basing) · 10 Export (`results.json`, figures, tables) · 11 Conclusion & limits.
**Build it progressively:** after every task add/update its section so the notebook is always runnable. Each section ends with a one-line "so what". No dead cells, no keys/personal data, no absolute paths, relative `DATA_DIR` + Colab fallback, everything seeded, executes in < ~10 min via `nbconvert --execute`, outputs kept.

## 13. References & AI-usage survey
`references.txt`: numbered, one per line, **identical to slide 15**: market/academic sources; libraries (scikit-learn, XGBoost, pandas, matplotlib); dataset line ("Company A telecom dataset, GCI World 2026 September Final Assignment materials, Matsuo-Iwasawa Lab, University of Tokyo — not redistributed"); **AI chat link lines** as placeholders `[AI-CHAT-LINK: Claude planning conversation]`, `[AI-CHAT-LINK: Antigravity/Gemini session]` for Islam to replace (sharing steps are platform-specific and unverified; if sharing isn't possible Islam asks the organizers).
**Survey (draft in `docs/UNDERSTANDING_AR.md`):** Q1 used generative AI (1 yes/2 no) · Q2 parts (1 market research/ideas, 2 EDA/plots, 3 preprocessing/features, 4 model/interpretation, 5 ML→quantified proposal, 6 slides/writing/translation, 7 references, 8 other) · Q3 tools (1 ChatGPT, 2 Claude, 3 Gemini, 4 GitHub Copilot, 5 other, 6 can't recall) · Q4 share explainable in own words (1 = 100%, 2 = 75–99%, 3 = 51–74%, 4 = 25–50%, 5 = little, 6 = unsure). Each answer 1–500 chars (≤ 2000 total); no transcripts/personal data. Suggested: Q1 = 1; Q2 = what really happened; Q3 = 2,3 (+5 for Antigravity); **Q4 honest — "1" only if Islam passes the self-test.**

## 14. Human-Understanding Pack — one file: `docs/UNDERSTANDING_AR.md` (Arabic, simple Iraqi-friendly Modern Standard; English terms in parentheses)
**Appended at the end of every phase** (so it always exists): *what we did · why · how (plain words + tiny example) · real result with number · what could go wrong · what to say if asked.* At the end it also holds: **glossary** (churn, EDA, feature, leakage, overfitting, cross-validation, AUC, precision/recall, lift, confusion matrix, baseline, XGBoost, gain vs permutation importance, label-shift re-basing, break-even, sensitivity, A/B holdout) · **numbers cheat-sheet** (every slide number → value · notebook section · meaning · sensitivity) · **≥ 30 interview Q&A** + 2-minute story · **speaker notes** per slide · **20-question self-test** (answers at the end) · **how to re-run** (commands/clicks, local and Colab) · **submission steps** (see tasks.md T13.6).

## 15. Risks
Thresholds are artifacts → robustness checks, "hypothesis" wording, pilot framing, fall back to Lane 1 · weak AUC (~0.70) → sell ranking/lift, not accuracy · 49.6% inflates impact → re-basing shown beside raw · hallucinated sources/numbers → open-every-URL rule + `check_submission.py` · notebook fails elsewhere → relative paths, minimal dependencies, nbconvert test · slide overflow/size → thumbnail QA, image downsizing · Google Slides integration gaps → fallbacks (§11.1) · AI-disclosure concerns → Understanding Pack + honest Q4 + chat links.

## 16. Open items for the human (only these two)
1. Replace the AI-chat-link placeholders and answer the AI survey honestly. 2. Press **Submit** on Omnicampus (≥ 1 day before the deadline), re-open the page to confirm status and attachments.

## Appendix — `results.json` minimum keys
`data{n_rows,n_cols,churn_rate,missing_top[],negatives{}}` · `eda{device_age_bins[],tenure_curve[],jump_ci{},zero_usage{n,churn,rev_mean}}` · `models[{id,name,cv_auc_mean,cv_auc_std,cv_acc,test_auc,test_acc,test_precision,test_recall,test_f1}]` · `final_model{name,test_auc,test_acc,train_acc}` · `topk[{k,n,precision,recall,lift,precision_rebased_5,precision_rebased_10}]` · `importance{gain[],permutation[]}` · `impact{assumptions{},scenarios[{name,net,retained,cost}],k_star,breakeven_s,sensitivity[]}` · `meta{seed,versions,interpreter,run_time}`.
