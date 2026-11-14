# Project Notes — Company A Telecom Churn PoC (GCI World 2026)

---

## 0. Requirements Digest (T0.1)

### 0.1 Source Documents Reviewed
1. `README.docx` — Official assignment rules, scenario, 7 evaluation requirements, citation policy, submission instructions, and FAQs (*GCI World 2026 September Final Assignment README*).
2. `final_assignment_tutorial.pdf` — Official 18-slide tutorial deck covering completion/Honors/Outstanding criteria, workflow, and Omnicampus submission screenshots (*GCI World 2026 September*).
3. `tutorial.ipynb` — Reference walkthrough notebook (*GCI World 2026 Winter* header): loading/merging `Client.csv` and `Record.csv`, basic EDA, `LabelEncoder` preprocessing, baseline `XGBClassifier`, evaluation, feature importance (`gain`), and business-impact framing.
4. `ENG_Company _A_ Dataset Overview.docx` — Official column dictionary for the ~100,000-record × ~100-column dataset (*GCI World 2026 Winter Company A Dataset Overview*; note filename on disk has spaces around `_A_`).
5. `GCI_Final_Assignment_Guide.pdf` — 42-page Arabic study/analysis guide (prepared 10 Nov 2026). Used strictly as calibration hints per PRD §0.4; every statistic is recomputed from `telecom/*.csv`.

### 0.2 The 7 Grading Requirements (Traced to `README.docx` §2)
- **R1 — Business proposal, not a technical report:** Form a clear, actionable business proposal driven by data insights with quantified business impact (revenue lift, cost savings, or risk reduction) (`README.docx` §1, §2.1; `tutorial.ipynb` §8).
- **R2 — Actual EDA on client data:** Base the proposal on real exploratory data analysis highlighting Company A's specific challenges and hypotheses (`README.docx` §2.2; `tutorial.ipynb` §3; `final_assignment_tutorial.pdf` p. 17).
- **R3 — Appropriate ML/statistical model(s) with text reporting:** Build and report ≥ 1 appropriate model (comparing multiple models is preferred per `README.docx` §6 FAQ). **Must explicitly write the model name, evaluation metric, and score as text on the slide** (screenshots/figures alone do not satisfy the requirement), explain why each model was chosen, how it was built, and how its quantitative insights inform the proposal (`README.docx` §2.3 & Notes on req 3).
- **R4 — External sources & market analysis:** Conduct market analysis using external reports, data, and papers, and cite all sources clearly on slides and in the reference list (`README.docx` §2.4, §2-1; `tutorial.ipynb` §1.2).
- **R5 — Executive-friendly communication:** Make the deck understandable to executives without an ML background by translating technical methods into plain language and conceptual diagrams without omitting essential PoC validation details (`README.docx` §2.5, §7-2).
- **R6 — Multiple purposeful visualizations:** Use multiple well-designed charts (not raw numbers) with careful colors, labels, units, and outlier/binning treatment (`README.docx` §2.6, §7-2; `tutorial.ipynb` §8).
- **R7 — Logical consistency:** Maintain a coherent thread from market & EDA → problem definition → features → modeling → recommendation → quantified impact (`README.docx` §2.7, §7-1; `final_assignment_tutorial.pdf` p. 17).

### 0.3 Deliverable Rules & Deadlines (Traced to `README.docx` §3, §6 & `final_assignment_tutorial.pdf` p. 3, 12–16)
- **Submission Portal:** Omnicampus (`https://edu.omnicamp.us/en/courses/170/reports/125/`).
- **Submission Window:** Opens 8 Oct 2026 00:00 UTC; **Hard Deadline: Saturday, 28 Nov 2026, 11:30 UTC (14:30 Iraq time, UTC+3)**.
- **Late Policy:** Zero tolerance — no late submissions and no post-deadline edits to references or notebooks (`README.docx` §3, §6).
- **Resubmission Policy:** Unlimited resubmissions before the deadline; only the latest submission is evaluated; **all three deliverables must be re-attached on every resubmission** (`README.docx` §3, §6).
- **Three Required Deliverables (Omnicampus account: `Islam-Raad`):**
  1. `Islam-Raad.pdf` — Presentation slides exported to PDF, **≤ 15 slides total** (including cover, dividers, references; slides beyond 15 may be ignored), **≤ 10 MB**.
  2. `references.txt` — List of references pasted into the Omnicampus "References" field (one URL/citation per line), matching all on-slide citations and including **generative AI chat history URL(s)**.
  3. `Islam-Raad.ipynb` — Reproducible end-to-end Jupyter notebook named after the Omnicampus account (no size restriction in `README.docx`; self-contained single `.ipynb`).
- **Course Completion & Honors (`final_assignment_tutorial.pdf` p. 3, `README.docx` §4):** Submitting and passing the Final Assignment is mandatory for course completion (alongside ≥ 7/14 attendance surveys and ≥ 14/24 homework points). Honors requires Top 10% on Final Assignment + Top 20% on Competition; Outstanding Students are selected by overall score and announced via Slack.

### 0.4 Citation, Plagiarism & Generative AI Rules (Traced to `README.docx` §2-1, §3, §6 & `GCI_Final_Assignment_Guide.pdf` p. 6–7, 36–37)
- Every external datum, method, figure, or text must be cited on the slide (footnote/`[n]`) and listed in the Omnicampus References field (`README.docx` §2-1, §3).
- Direct quotation must remain `< 40%` of final material (`README.docx` §2-1); PRD enforces `≈ 0%` direct quotation (paraphrase + cite; quotes ≤ 15 words only if essential).
- Generative AI may be used for ideation, diagrams, coding, and editing, but raw AI output is not considered original work unless understood and synthesized by the student, and **the AI chat link(s) must be pasted into References** (`README.docx` §3, §6).
- The Omnicampus AI-usage survey (Q1–Q4, documented in `GCI_Final_Assignment_Guide.pdf` p. 36–37) does not affect grading but must be completed honestly without personal data or raw transcripts.

### 0.5 Conflicts, Discrepancies & Traceability (Source Files vs. `prd.md`)
- **Cohort naming across official files:** `README.docx` and `final_assignment_tutorial.pdf` p. 1 state *GCI World 2026 September*; `tutorial.ipynb` and `ENG_Company _A_ Dataset Overview.docx` state *GCI World 2026 Winter*; `final_assignment_tutorial.pdf` p. 12–14 screenshots show *GCI World 2026 April* (with April/June dates). **Decision:** Follow `README.docx` (highest precedence per PRD §0.4): cohort is **GCI World 2026 September** and deadline is **28 Nov 2026, 11:30 UTC**.
- **Dataset Overview filename & typos:** On disk the file is named `ENG_Company _A_ Dataset Overview.docx` (with spaces around `_A_`), and its introductory paragraph has a typo ("Company I's strict data protection policies" and `-100 columns`). **Decision:** Always use `Company A` and `~100 columns`; `.gitignore` uses `*.docx` which matches regardless of spacing.
- **Undocumented / misdescribed columns in Overview:** `change_mou` and `change_rev` are described as "Percentage change..." in `ENG_Company _A_ Dataset Overview.docx`, while `recv_sms_Mean`, `iwylis_vce_Mean`, and `Customer_ID` have `NaN` descriptions. Full empirical verification is scheduled in T1.6.
- **PRD-only rules (stricter engineering/quality rules defined by `prd.md` beyond official files):**
  - Interpreter locked to `/home/islam-raad/ai_workspace/bin/python3.12` with no package upgrades (**PRD-only**, §0.1).
  - `PROGRESS.md` single-file resume ritual, one local git commit per task, and phase tags (**PRD-only**, §0.2–0.3).
  - Lean directory layout, `outputs/results.json` single source of truth, and `scripts/check_submission.py` automated verifier (**PRD-only**, §0.5, §3).
  - Exclusive use of `matplotlib` for all charts and conceptual diagrams — prohibiting `seaborn` even though `tutorial.ipynb` uses `seaborn` (**PRD-only**, §10).
  - Google Slides 15-slide exact geometry/typography/color spec and Drive image-embedding privacy workflow (**PRD-only**, §11; `README.docx` allows PowerPoint/Keynote/Google Slides/Figma up to 15 slides).
  - Iraq mobile market lens with ≥ 8 verified sources (**PRD-only** count/choice in §6.3, §7, implementing `tutorial.ipynb` §1.2 advice to ground the proposal in a concrete local market).
  - Two-lane retention program with ~300-day device-age robustness gate (**PRD-only**, §6.2, §8.2).
  - Label-shift realism re-basing from 49.56% sample churn to 5%–10% realistic churn priors (**PRD-only** formula in §9.4, addressing the 5%–10% real-world churn note in `tutorial.ipynb` §3.3 and `GCI_Final_Assignment_Guide.pdf` p. 19, 28).
  - Arabic Human-Understanding Pack in `docs/UNDERSTANDING_AR.md` (**PRD-only**, §14).

---

## 1. Decision Log
- **2026-11-14 (T0.1):** Adopted `README.docx` as primary source of truth for cohort title (*GCI World 2026 September*) and deadline (*28 Nov 2026, 11:30 UTC*), resolving cohort-label inconsistencies in `tutorial.ipynb` (*Winter*) and tutorial PDF screenshots (*April*).
- **2026-11-14 (T0.1):** Enforced PRD §10 `matplotlib`-only rule across all notebook and slide figures, superseding `seaborn` usage in `tutorial.ipynb`.
- **2026-11-14 (T1.3 — Negative/impossible values handling):**
  - `change_mou` (`53,651` negatives, min `-3,875.00`) & `change_rev` (`56,150` negatives, min `-1,107.74`): **Keep as-is** (legitimate signed deltas vs. prior 3-month average).
  - `eqpdays` (`133` negatives, range `-5` to `-1`, `35.34%` churn): **Clip to `0` for age ratios/binning (`eqpdays_clean = clip(lower=0)`) and add binary flag `eqpdays_neg_flag`** so tree/linear models retain the low-churn (`35.34%`) pre-activation/recent-swap signal while avoiding negative equipment ages.
  - `totmrc_Mean` (`23` negatives, min `-26.91`, `47.83%` churn), `rev_Mean` (`5` negatives, min `-6.17`, `40.00%` churn), `avg6rev` (`3` negatives, min `-2.00`, `66.67%` churn): **Clip denominators at `0` (with epsilon) when computing revenue ratios (`recurring_share`, `overage_share`, `rev_trend`) and add `neg_bill_flag`**, while keeping raw values for tree splits (reflecting billing credits/adjustments).
  - **Explanation of `tutorial.ipynb` `np.log1p` `RuntimeWarning`:** `np.log1p(x) = ln(1 + x)` yields `-inf` (`divide by zero`) at `x = -1` (`34` rows in `eqpdays`) and `NaN` (`invalid value`) for `x < -1` (`99` rows in `eqpdays`, `14` rows in `totmrc_Mean`, `4` rows in `rev_Mean`).
- **2026-11-14 (T2.2 — Robustness verdict on the ~300-day `eqpdays` jump):**
  - **Verdict:** **Real-looking lifecycle effect (strongly coupled with the 10–12 month initial commitment/device-upgrade cycle; retains Lane 2 as a controlled A/B pilot in T4.2).**
  - **Evidence:** (1) Bootstrap 95% CI on `churn(301–340) − churn(260–300)` (`B = 2,000`, `seed = 42`, train) is **`+23.83 pp` (`[+22.12, +25.62] pp`)** (`36.85%` $\rightarrow$ `60.69%`), and local linear RDD jump at `300d` is **`+23.22 pp`** (`37.52%` $\rightarrow$ `60.74%`). (2) The jump is positive across **`19/19` geographic areas** (`+16.3 pp` to `+30.1 pp`) and **`8/8` major credit classes** (`+11.0 pp` to `+29.3 pp`), and persists within `months >= 10` (**`+19.46 pp`**). (3) Baseline customer covariates (`rev_Mean, hnd_price, months, mou_Mean, uniqsubs`) are smooth across `300d` (`|SMD| <= 0.12`), ruling out a corrupted join. (4) Decomposition shows the jump is concentrated in first-handset accounts (`phones == 1`: `+34.08 pp`; `months 10–12`: `+28.43 pp`, reflecting 1-year contract/promotional expiry), with a smaller residual device-aging effect among multi-handset accounts (`phones >= 2`: **`+5.60 pp`**; `months >= 13`: **`+2.98 pp`**). Therefore, we present the 300-day / 10–12-month lifecycle trigger honestly as an intertwined commitment/upgrade window and test it via a holdout A/B pilot (Lane 2).
- **2026-11-14 (T4.1 — Candidate Framing Decision Matrix, Options A–E):**
  | Candidate Framing (PRD §6.1) | Evidence in Data (1–5) | Actionability (1–5) | Measurability (1–5) | Low Risk / Robustness (1–5) | Iraq / MENA Market Fit (1–5) | Total (/25) | Role in Proposal |
  |---|---|---|---|---|---|---|---|
  | **A. Risk-Ranked Retention** (supervised binary classification / top-$k\%$ ranking) | `5` (top-10% lift `~1.6x`) | `5` (direct CRM call/offer list) | `5` (ROC-AUC, Precision@$k$, Lift@$k$, A/B holdout) | `5` (depends on overall ranking, not a single cutoff) | `5` (standard CVM workflow in Zain/Asiacell) | **`25 / 25`** | **Core Engine (Lane 1)** |
  | **D. Value-at-Risk ($P(\text{churn}) \times \text{Value}$)** | `5` (`rev_Mean` alone fails to separate classes: `58.26` vs. `59.38 MU`) | `5` (prioritizes high-margin active accounts, skips `22.89 MU` silent SIMs) | `5` (expected net margin in MU) | `5` (protects budget from low-ARPU false positives) | `5` (essential in multi-SIM prepaid/hybrid bases) | **`25 / 25`** | **Core Prioritization Rule (Lane 1)** |
  | **B. Lifecycle Triggers** (`~300d` handset age & `months 10–12` cliff) | `4` (`+23.83 pp` jump across 19/19 areas, `+12.95 pp` in `months >= 10`) | `5` (timed pre-300d handset refresh & month-9 loyalty check) | `4` (A/B pilot incremental retention) | `3` (observational entanglement with 1-year contract expiry; non-causal) | `4` (fits contract/bundle & device installment cycles) | **`20 / 25`** | **Complementary Pilot (Lane 2 — A/B Holdout)** |
  | **C. Early Warning on Usage Drop** (`change_mou < 0`, `10 < mou <= 65`) | `4` (`mou=0` churns `78.5%`, missing `change_mou` `76.0%`) | `4` (proactive bundle/voice bonus before SIM goes silent) | `4` (reactivation & retention rate) | `4` (must exclude `mou=0` already-gone lines) | `5` (directly targets multi-SIM silent switching) | **`21 / 25`** | **Integrated into Lane 1 Features & Offer Design** |
  | **E. Unsupervised Segmentation** (clustering) | `2` (continuous overlap across 98 features) | `2` (clusters lack direct 1-to-1 offer mapping without a risk score) | `2` (no ground-truth retention metric) | `3` (arbitrary cluster count $K$) | `3` (descriptive only) | **`12 / 25`** | **Rejected as standalone framing** |
- **2026-11-14 (T4.2 — Decision Gate Choice: Two-Lane Retention Program with Controlled A/B Pilot):**
  - **Decision:** Adopt **(i) the Two-Lane Retention Program** (PRD §6.2 Default Framing), combining **Lane 1 (Monthly ML Risk-Ranked + Value-at-Risk Targeting)** as the core production engine with **Lane 2 (Pre-300-Day Handset Refresh & Month-9 Commitment Check-in)** explicitly framed as a **randomized 90-day A/B holdout pilot**.
  - **Reasoning:**
    1. **Core Value comes from Lane 1 (Options A + D + C):** Because `rev_Mean` alone does not separate churners (`58.26 MU`) from non-churners (`59.38 MU`) and `mou_Mean == 0` lines (`78.48%` churn, `22.89 MU/mo`, `0.62%` of revenue) are already-gone silent SIMs (Ascarza 2018 `[9]`), the primary business lever must rank active customers by calibrated churn probability $\times$ recurring margin (`Value-at-Risk`) and intervene on active declining users (`change_mou < 0`, high `ovr_share`).
    2. **Lane 2 Survives `T2.2` as a Testable Hypothesis (Option B):** The `+23.83 pp` jump past `eqpdays = 300` (`[+22.12, +25.62] pp`) is consistent across `19/19` geographic areas and `8/8` credit classes, with smooth baseline covariates (`|SMD| <= 0.12`) and a `+12.95 pp` residual jump within `months >= 10` (`43.44%` $\rightarrow$ `56.39%`). However, because observational data cannot isolate handset aging from 1-year contract/promotional expiry (`months 10–12`), launching Lane 2 as a controlled 50/50 holdout A/B pilot captures the upside while protecting capital before full rollout.
- **2026-11-14 (T4.3 — Manager-Friendly Problem Definition Paragraph, 4 Sentences):**
  > **Problem Statement (Slide 7 & Notebook §5):** Company A's Customer Value Management (CVM) and Retention team loses thousands of wireless subscribers every month—representing millions of Monetary Units (MU) in recurring margin—yet cannot afford blanket retention discounts across all `100,000` accounts or rely on raw monthly bill size (`rev_Mean`), which is nearly identical between churners (`58.26 MU`) and staying customers (`59.38 MU`). Because historical records provide a verified outcome label (`churn ∈ {0, 1}`) measured 31–60 days after each customer snapshot (giving a 30-day operational intervention window), we formulate this as a **supervised binary classification and probability-ranking task** that predicts each customer's probability of leaving, $P(\text{churn})$. Multiplying the re-based churn probability $P_{\text{adj}}(\text{churn})$ by 6-month recurring margin ($V = \text{ARPU} \times \text{margin} \times 6$) produces an actionable **Value-at-Risk** score that prioritizes high-value active accounts showing usage decline (`change_mou < 0`, `10 < mou_Mean <= 65`) while excluding `1,600` silent `0 MOU` SIMs (`22.89 MU/mo`, `0.62%` of revenue) that have already effectively left. Using this score, CVM executes a **Two-Lane Retention Program**: **Lane 1** targets the top-10% (or budget-optimal top-$k^*$) highest Value-at-Risk active accounts each month with tailored plan right-sizing, call-quality care, or voice/data bonuses, while **Lane 2** tests a proactive Month-9 loyalty check-in (`months ∈ [8, 9]`) and a pre-300-day handset refresh voucher (`eqpdays ∈ [240, 290]`) in a randomized 90-day A/B holdout pilot.
- **2026-11-14 (T4.4 — KPI Hierarchy & Decision Owners):**
  - **Primary Business KPI (Online Pilot):** **Incremental Retention Rate ($\Delta r = r_{\text{treatment}} - r_{\text{control}}$)** and **Net Retained Margin in Monetary Units (MU)** (`Net = Saved Margin - Offer Cost`) over a 90-day randomized holdout pilot (Lane 1: 80% treatment / 20% holdout in top-$k\%$; Lane 2: 50% treatment / 50% holdout in `months 8–9` and `eqpdays 240–290`).
  - **Guardrail KPIs:** Offer backfire check ($\Delta r \ge 0$ across sub-segments, avoiding proactive-contact backfire `[9]`) and 6-month post-campaign ARPU retention.
  - **Offline ML KPIs:** **ROC-AUC** (primary model selection metric), **Precision@$10\%$** and **Lift@$10\%$** (reported both on raw $\pi_s = 49.562\%$ and re-based to $\pi_r \in \{5\%, 10\%\}$ `[11]`), and **Calibration Brier Score** (since $P(\text{churn})$ enters `Value-at-Risk` multiplication).
  - **Decision Owner:** **Head of Customer Value Management (CVM) & Retention** (budget & offer allocation owner), supported by **CRM Campaign Operations** (monthly batch scoring & outreach delivery), **Commercial / Device Product Team** (Lane 2 handset refresh & Month-9 loyalty offers), and **Customer Care / Network Quality** (care follow-up for high `drop_blk_rate` accounts).
- **2026-11-14 (T5.1 — Leakage-Safe Preprocessing Pipelines vs. Tutorial `LabelEncoder`):**
  - **Comparison (5-fold Stratified CV on 70% train, `n = 70,000`, `seed = 42`):**
    1. **Tutorial `LabelEncoder` (baseline):** Fits on full dataset before splitting and converts `NaN` via `.astype(str)` into a literal `'nan'` category $\rightarrow$ CV ROC-AUC = **`0.6935 ± 0.0024`**, CV Acc = **`0.6387`**.
    2. **Leakage-Safe Tree Pipeline (`OrdinalEncoder` inside `ColumnTransformer`):** Encodes the 21 categorical columns strictly inside each training fold with `handle_unknown='use_encoded_value'`, `unknown_value=-1`, and `encoded_missing_value=np.nan`, preserving true `np.nan` values so XGBoost/LightGBM learn optimal default split directions (`Chen & Guestrin 2016 [13]`) $\rightarrow$ CV ROC-AUC = **`0.6938 ± 0.0016`**, CV Acc = **`0.6392`**.
    3. **Leakage-Safe Linear Pipeline (`LogisticRegression`):** Applies `SimpleImputer(strategy='median', add_indicator=True)` + `StandardScaler()` to numeric columns and `SimpleImputer(strategy='constant', fill_value='MISSING')` + `OneHotEncoder(handle_unknown='ignore', min_frequency=0.01)` to categoricals strictly inside each fold $\rightarrow$ CV ROC-AUC = **`0.6321 ± 0.0037`**, CV Acc = **`0.5957`** on raw unengineered features (confirming `Grinsztajn et al. 2022 [12]` that linear models struggle with raw non-monotone thresholds like `eqpdays > 300` and `months 10–12` without explicit indicator features).
  - **Decision:** Adopt the **Leakage-Safe Tree Pipeline** (`OrdinalEncoder` preserving `np.nan` inside `Pipeline`) for all tree models and the **Leakage-Safe Linear Pipeline** for `M1 (Logistic Regression)`.
- **2026-11-14 (T5.2 — Domain Feature Engineering, 28 Features Across 6 Families):**
  - Engineered `28` domain features (`dev_age_gt_300`, `dev_age_301_360`, `eqpdays_neg_flag`, `tenure_le_9`, `tenure_10_12`, `eqp_per_tenure`, `months_per_phone`, `active_sub_ratio`, `zero_mou_flag`, `low_mou_flag`, `mou_ratio_3m`, `mou_ratio_6m`, `rev_ratio_3m`, `rev_ratio_6m`, `mou_delta_3v6`, `drop_rate`, `block_rate`, `drop_blk_rate`, `unanswered_rate`, `completion_rate`, `recurring_share`, `overage_share`, `roam_share`, `rev_per_mou`, `has_custcare`, `custcare_per_call`, `change_mou_missing_flag`, `n_missing_demographics`) using safe division (`+ 1.0` or `+ 1e-3`) and explicit clipping of negative values (`.clip(lower=0)` per `T1.3`); documented all 28 in `docs/NOTES.md → 4. Feature Dictionary`.

---

## 2. Assumptions
| Parameter | Symbol | Conservative | Base | Optimistic | Provenance (`SOURCED [ID]` vs. `ASSUMPTION`) & Rationale |
|---|---|---|---|---|---|
| Active customer base | $N$ | `100,000` | `100,000` | `100,000` | **SOURCED (Dataset)** — exact merged row count of `Client.csv` and `Record.csv`. |
| Monthly ARPU (Monetary Units) | $\text{ARPU}$ | `48.20 MU` (median `rev_Mean`) | `58.72 MU` (mean `rev_Mean`) | `58.72 MU` (mean `rev_Mean`) | **SOURCED (Dataset)** — empirical mean (`58.72 MU`) and median (`48.20 MU`) of `rev_Mean` across `99,643` non-null accounts. |
| Sample churn rate | $\pi_s$ | `49.562%` | `49.562%` | `49.562%` | **SOURCED (Dataset `[7]`)** — oversampled/balanced case-control rate (`49,562 / 100,000`). |
| Realistic operational churn prior | $\pi_r$ | `5.0%` | `10.0%` (also shown at `5.0%`) | `10.0%` | **SOURCED `[7, 10]` & Course Guide** — `tutorial.ipynb` §3.3 and `GCI_Final_Assignment_Guide.pdf` p. 19, 28 specify `5%–10%` realistic churn; Neslin et al. `[7]` report `~1.8%/mo` (`~5%–10%` over a 3–6 month campaign horizon). Re-based via Saerens et al. `[10]`. |
| Gross contribution margin | $m$ | `60%` (`0.60`) | `70%` (`0.70`) | `80%` (`0.80`) | **ASSUMPTION** — wireless gross service margin after interconnect/direct variable costs; sensitivity-tested in Phase 8. |
| Retained lifetime horizon | $H$ | `3 months` | `6 months` | `9 months` | **ASSUMPTION** — months of incremental cash flow preserved when a would-be churner is saved (anchored to Neslin et al. `[7]` 3–6 month model horizon). |
| Retained value per saved churner | $V = \text{ARPU} \times m \times H$ | `86.76 MU` (`48.20 × 0.60 × 3`) | `246.62 MU` (`58.72 × 0.70 × 6`) | `422.78 MU` (`58.72 × 0.80 × 9`) | **DERIVED (`SOURCED` ARPU × `ASSUMPTION` $m, H$)** — gross margin preserved per successfully retained true churner. |
| Retention offer success rate | $s$ | `10%` (`0.10`) | `20%` (`0.20`) | `30%` (`0.30`) | **ASSUMPTION** — fraction of targeted true churners persuaded to stay by the proactive offer (no Iraqi operator publishes internal save rates; anchored to literature ranges `[7, 8, 9]`). |
| Cost per targeted customer | $c$ | `12.00 MU` | `8.00 MU` | `5.00 MU` | **ASSUMPTION** — incentive + outreach cost incurred for **every** targeted customer ($n = k \cdot N$), including false positives who would have stayed anyway (`~8.5%–20.4%` of monthly ARPU). |

---

## 3. Hypotheses
*(Ranked by business actionability; discovered strictly on the 70% stratified training split `n = 70,000`.)*

1. **H1 — Pre-300-Day Handset & First-Year Commitment Expiry (Rank 1 — Highest Actionability, Lane 2 + Features):**
   - **Full-sentence hypothesis:** *"Customers whose current handset approaches or passes `300` days (`eqpdays` `301–340d` churn = `60.69%` vs. `260–300d` = `36.85%`, `+23.83 pp`, 95% CI `[+22.12, +25.62] pp`) and who enter months `10–12` of service (`57.83%` churn, peaking at `64.57%` in month 11 vs. `29.25%` in month 9) are substantially more likely to churn because their initial 12-month promotional commitment or handset replacement cycle expires (`+28.43 pp` jump in `months 10–12`, plus `+5.60 pp` among multi-handset upgraders `phones >= 2`); we test this by engineering threshold/ratio features (`dev_age_gt_300`, `tenure_10_12`, `eqp_per_tenure`), inspecting partial dependence and permutation importance, and designing a controlled holdout A/B pilot offering a pre-300-day device refresh / month-9 loyalty check."*
2. **H2 — Active Usage Drop Before Silent-SIM Abandonment (Rank 2 — High Actionability, Early Warning & Lane 1 Features):**
   - **Full-sentence hypothesis:** *"Customers whose monthly voice minutes drop sharply relative to their 3- and 6-month baseline (`change_mou < 0`, missing `change_mou` churn = `76.03%`, or `10 < mou_Mean <= 65` churn = `54.74%`) are more likely to churn because they are shifting primary call volume to a competing SIM before abandoning the line altogether (whereas `mou_Mean == 0` lines at `78.48%` churn contribute only `0.62%` of monthly revenue and are already silent); we test this by adding usage-trend ratios (`mou_trend_3m`, `mou_trend_6m`, `rev_trend_3m`), missingness flags, and zero/low-usage indicators in 5-fold cross-validation and prioritizing declining-usage accounts that still carry meaningful recurring revenue (`totmrc_Mean`)."*
3. **H3 — Bill Shock (Overage Share) & Uncapped Spend Exposure (Rank 3 — Medium-High Actionability, Tariff Right-Sizing):**
   - **Full-sentence hypothesis:** *"Customers whose overage charges exceed `40%` of their monthly bill (`ovrrev_Mean / rev_Mean > 0.40`, churn = `54.20%` vs. `47.44%` at `0%–20%`), who lack an Account Spending Limit (`asl_flag == 'N'` churn = `50.90%` vs. `41.37%` for `'Y'`), or who experience top-quartile call drop/block rates (`> 8.85%` of attempts, churn = `51.71%` vs. `46.75%` in Q1) are more likely to churn due to bill shock and service friction; we test this by engineering `recurring_share`, `overage_share`, `roam_share`, and `drop_blk_rate` features and evaluating their contribution to top-$k$ risk ranking and tariff-plan right-sizing."*

### Summary of All Section 4 EDA One-Sentence Findings
- **4.1 (`eqpdays`):** Churn stays around `36.9%–38.3%` up to `300` days (`39.40%` overall `<= 300d`), jumps **`+23.75 pp`** from `261–300d` (`36.93%`) to `301–340d` (`60.69%`), and peaks at **`64.34%`** in `321–340d`.
- **4.2 (Robustness):** The `+23.83 pp` jump (`260–300d` vs. `301–340d`, 95% CI `[+22.12, +25.62] pp`, local linear `+23.22 pp`) holds across `19/19` areas and `8/8` credit classes with smooth covariates (`|SMD| <= 0.12`), driven by first-year contract/device maturity (`+28.43 pp` in `months 10–12`) plus multi-handset replacement (`+5.60 pp` for `phones >= 2`).
- **4.3 (`months`):** Churn jumps from `29.25%` at month 9 to `40.18%` at month 10, peaks at **`64.57%` at month 11** and **`61.49%` at month 12**, and declines to `47.15%` at `37+` months.
- **4.4 (Entanglement):** Zero customers with `6–9` months of tenure have `eqpdays > 300`, yet within `months >= 10` (`n = 60,090`), churn still rises **`+12.95 pp`** from `43.44%` (`<= 300d`) to `56.39%` (`> 300d`) and increases with device age inside every tenure band.
- **4.5 (Usage Collapse):** `mou_Mean == 0` (`n = 1,120` train / `1,600` all) churns at `78.48%` (`79.81%` all) but represents only `0.62%` of monthly revenue (`22.89 MU`) — silent SIMs that are already gone — whereas declining active users (`change_mou < 0`, `10 < mou_Mean <= 65`) are actionable before silence.
- **4.6 (Revenue & Value):** `rev_Mean` barely separates stayers (`59.38 MU`) from churners (`58.26 MU`), while churners have lower `totmrc_Mean` (`44.59` vs. `47.87 MU`) and higher `ovrrev_Mean` (`14.30` vs. `12.90 MU`), requiring Value-at-Risk ($P(\text{churn}) \times \text{Value}$) targeting.
- **4.7 (Customer Care):** Zero-call customers (`55.72%`) churn at `51.70%` vs. `43.64%` for `> 6` calls, reflecting active-usage confounding (`mou_Mean = 1,135.5` vs. `336.4`), issue resolution/upgrades (`eqpdays = 255.8d` vs. `447.6d`), and self-selection.
- **4.8 (Quality, Overage, Roaming):** Bill shock (`ovrrev_Mean / rev_Mean > 40%`) raises churn to `54.20%` (vs. `47.44%` at `0%–20%`), top-quartile dropped/blocked call rate (`> 8.85%`) raises churn to `51.71%` (vs. `46.75%`), and `asl_flag == 'Y'` lowers churn by `-9.53 pp` (`41.37%` vs. `50.90%`).
- **4.9 (Demographics & Fairness):** Household demographics have narrow spread (`2.68–5.26 pp`) and heavy missingness (`22%–49%`), whereas `ethnic` spans `18.88 pp` (`39.20%–58.08%`) and is excluded per our behavior-not-identity policy.

---

## 4. Feature Dictionary
All `28` engineered features below are computed row-wise from pre-window customer history (`eps = 1e-3` or `+ 1.0` for safe division; negative billing/device anomalies clipped via `.clip(lower=0)` per `T1.3`), use **zero target information**, and are available before the 31–60 day churn outcome window:

| # | Feature Name | Formula (Safe Division & `T1.3` Negative Handling) | Business Reason & Hypothesis (`H1`–`H3`) | Leakage Check | Train 1-Feat AUC | Kept? |
|---|---|---|---|---|---|---|
| 1 | `dev_age_gt_300` | `(eqpdays > 300).astype(float)` | `H1`: Captures the `+23.83 pp` handset aging / commitment cliff past 300 days (`39.40%` $\rightarrow$ `56.39%`). | Pre-window snapshot; no target used | `0.5817` | **Yes** |
| 2 | `dev_age_301_360` | `((eqpdays > 300) & (eqpdays <= 360)).astype(float)` | `H1`: Isolates the acute 301–360 day window where churn peaks (`60.69%–64.34%`). | Pre-window snapshot; no target used | `0.5313` | **Yes** |
| 3 | `eqpdays_neg_flag` | `(eqpdays < 0).astype(float)` | `T1.3 / H1`: Flags recent handset replacement / pending activation (`n = 133` all, `35.34%` churn) before clipping `eqpdays` at `0`. | Pre-window snapshot; no target used | `0.5004` | **Yes** |
| 4 | `tenure_le_9` | `(months <= 9).astype(float)` | `H1`: Early onboarding / commitment lock-in period (`29.25%` churn at month 9). | Pre-window snapshot; no target used | `0.5498` | **Yes** |
| 5 | `tenure_10_12` | `((months >= 10) & (months <= 12)).astype(float)` | `H1`: First-year contract/promotional expiry cliff (`64.57%` churn at month 11, `61.49%` at month 12). | Pre-window snapshot; no target used | `0.5305` | **Yes** |
| 6 | `eqp_per_tenure` | `clip(eqpdays, 0) / (months * 30.4375 + 1e-3)` | `H1`: Share of total tenure spent on the current handset (`~1.0` = original signup phone; `< 0.5` = upgraded mid-tenure). | Pre-window snapshot; no target used | `0.5423` | **Yes** |
| 7 | `months_per_phone` | `months / (clip(phones, 1) + 1e-3)` | `H1`: Average months of service per handset issued on the account (distinguishes frequent upgraders from aging-device holders). | Pre-window snapshot; no target used | `0.5498` | **Yes** |
| 8 | `active_sub_ratio` | `actvsubs / (clip(uniqsubs, 1) + 1e-3)` | `H1 / H2`: Ratio of active lines to total unique lines on the account (`< 1.0` signals partial multi-line deactivation). | Pre-window snapshot; no target used | `0.5097` | **Yes** |
| 9 | `zero_mou_flag` | `(mou_Mean == 0).astype(float)` | `H2`: Flags silent SIMs (`78.48%` churn, `22.89 MU/mo`) that have already stopped all voice usage. | Pre-window snapshot; no target used | `0.5093` | **Yes** |
| 10 | `low_mou_flag` | `((mou_Mean > 0) & (mou_Mean <= 10)).astype(float)` | `H2`: Flags near-silent SIMs (`66.13%` churn) transitioning toward abandonment. | Pre-window snapshot; no target used | `0.5025` | **Yes** |
| 11 | `mou_ratio_3m` | `clip(mou_Mean, 0) / (clip(avg3mou, 0) + 1.0)` | `H2`: Relative voice usage trend vs. prior 3-month average (`< 1.0` captures acute multi-SIM usage drop). | Pre-window snapshot; no target used | `0.5544` | **Yes** |
| 12 | `mou_ratio_6m` | `clip(mou_Mean, 0) / (clip(avg6mou, 0) + 1.0)` | `H2`: Relative voice usage trend vs. prior 6-month baseline. | Pre-window snapshot; no target used | `0.5445` | **Yes** |
| 13 | `rev_ratio_3m` | `clip(rev_Mean, 0) / (clip(avg3rev, 0) + 1.0)` | `H2 / H3`: Relative monthly bill change vs. prior 3-month average (`> 1.0` = bill spike; `< 1.0` = spend drop). | Pre-window snapshot; no target used | `0.5147` | **Yes** |
| 14 | `rev_ratio_6m` | `clip(rev_Mean, 0) / (clip(avg6rev, 0) + 1.0)` | `H2 / H3`: Relative monthly bill change vs. prior 6-month baseline. | Pre-window snapshot; no target used | `0.5064` | **Yes** |
| 15 | `mou_delta_3v6` | `avg3mou - avg6mou` | `H2`: Medium-term usage trajectory (whether 3-month average was already falling below 6-month average). | Pre-window snapshot; no target used | `0.5206` | **Yes** |
| 16 | `drop_rate` | `clip(drop_vce_Mean, 0) / (clip(attempt_Mean, 0) + 1.0)` | `H3`: Dropped voice calls per attempted call (network quality friction). | Pre-window snapshot; no target used | `0.5084` | **Yes** |
| 17 | `block_rate` | `clip(blck_vce_Mean, 0) / (clip(attempt_Mean, 0) + 1.0)` | `H3`: Blocked voice calls per attempted call (congestion friction). | Pre-window snapshot; no target used | `0.5058` | **Yes** |
| 18 | `drop_blk_rate` | `clip(drop_blk_Mean, 0) / (clip(attempt_Mean, 0) + 1.0)` | `H3`: Combined dropped + blocked call rate (Q4 `> 8.85%` churns at `51.71%` vs. Q1 `46.75%`). | Pre-window snapshot; no target used | `0.5057` | **Yes** |
| 19 | `unanswered_rate` | `clip(unan_vce_Mean, 0) / (clip(attempt_Mean, 0) + 1.0)` | `H3`: Share of attempted calls that go unanswered. | Pre-window snapshot; no target used | `0.5070` | **Yes** |
| 20 | `completion_rate` | `clip(complete_Mean, 0) / (clip(attempt_Mean, 0) + 1.0)` | `H3`: Call completion efficiency (`complete_Mean / attempt_Mean`). | Pre-window snapshot; no target used | `0.5331` | **Yes** |
| 21 | `recurring_share` | `clip(clip(totmrc_Mean, 0) / (clip(rev_Mean, 0) + 1.0), 0, 2)` | `H3`: Predictable base-plan share of monthly bill (higher among stayers: `47.87` vs. `44.59 MU`). | Pre-window snapshot; no target used | `0.5324` | **Yes** |
| 22 | `overage_share` | `clip(clip(ovrrev_Mean, 0) / (clip(rev_Mean, 0) + 1.0), 0, 2)` | `H3`: Bill-shock share of monthly bill (`> 40%` overage share churns at `54.20%` vs. `47.44%`). | Pre-window snapshot; no target used | `0.5161` | **Yes** |
| 23 | `roam_share` | `clip(clip(roam_Mean, 0) / (clip(rev_Mean, 0) + 1.0), 0, 2)` | `H3`: Roaming revenue share of monthly bill. | Pre-window snapshot; no target used | `0.5032` | **Yes** |
| 24 | `rev_per_mou` | `clip(rev_Mean, 0) / (clip(mou_Mean, 0) + 1.0)` | `H2 / H3`: Effective price paid per minute of use (high values indicate poor plan fit or inactive fixed charges). | Pre-window snapshot; no target used | `0.5477` | **Yes** |
| 25 | `has_custcare` | `(custcare_Mean > 0).astype(float)` | `H3`: Indicator for any customer-care contact (`0` calls churns at `51.70%` vs. `43.64%` for `> 6` calls). | Pre-window snapshot; no target used | `0.5239` | **Yes** |
| 26 | `custcare_per_call` | `clip(custcare_Mean, 0) / (clip(attempt_Mean, 0) + 1.0)` | `H3`: Customer-care call intensity normalized by overall call volume. | Pre-window snapshot; no target used | `0.5248` | **Yes** |
| 27 | `change_mou_missing_flag` | `change_mou.isna().astype(float)` | `H2`: Captures the `0.89%` missing-trend block (`n = 891` all) that churns at `76.03%`. | Pre-window snapshot; no target used | `0.5048` | **Yes** |
| 28 | `n_missing_demographics` | `df[DEMO_COLS].isna().sum(axis=1).astype(float)` | Data-audit signal (`T1.2`): Counts missing demographic fields across the 22 demographic attributes. | Pre-window snapshot; no target used | `0.5154` | **Yes** |

---

## 5. Data-Doc Discrepancies
| Column / Item | `ENG_Company _A_ Dataset Overview.docx` Claim | Empirical Reality in `telecom/*.csv` | Exact Wording to Use on Slides & Notebook |
|---|---|---|---|
| `change_mou` | "Percentage change in monthly minutes of use vs previous three month average" | **`22,585` rows (`22.79%` of non-null / `22.59%` of total) are `< -100`** (min `-3,875.00`), which is impossible for a percentage decrease of non-negative minutes. Tracks `mou_Mean - avg3mou` (`Spearman ρ = 0.9881`, `Pearson r = 0.9025`). | **"Change in monthly minutes vs. 3-month average (minutes)"** — never say "%" or "percentage change". |
| `change_rev` | "Percentage change in monthly revenue vs previous three month average" | `1,108` rows (`1.12%`) are `< -100` (min `-1,107.74`, max `9,963.66`). Tracks `rev_Mean - avg3rev` (`Spearman ρ = 0.9561`, `Pearson r = 0.9440`). | **"Change in monthly revenue vs. 3-month average (MU)"** — never say "%". |
| `recv_sms_Mean` | `NaN` (undocumented) | Non-zero in only `872` of `100,000` rows (`0.87%`; `99.13%` zeros); churn `46.67%` when `> 0` vs. `49.59%` when `== 0`. | **"Mean received SMS count (99.1% zeros; near-empty)"**. |
| `iwylis_vce_Mean` | `NaN` (undocumented) | Correlates `ρ = 0.9687` with `mouiwylisv_Mean` (inbound wireless-to-wireless minutes) and `ρ = 0.8046` with `owylis_vce_Mean` (outbound wireless-to-wireless calls). | **"Mean inbound wireless-to-wireless voice calls (inferred from schema & correlation)"**. |
| `Customer_ID` | `NaN` (undocumented) | Unique primary join key (`1,000,001` to `1,100,000`), 1-to-1 across `Client.csv` and `Record.csv`. | **"Unique customer identifier (`Customer_ID`)"**. |
| `infobase` | "InfoBase match" | Categorical match flag: `M` (`77,697`, `48.92%` churn), `MISSING` (`22,079`, `51.98%` churn), `N` (`224`, `33.04%` churn). Captures whether customer record matched external demographic registry. | **"External demographic registry match indicator (`infobase`)"**. |
| `months` location | Listed in `tutorial.ipynb` §2.3 table under `Client.csv` | Actually stored in `Record.csv` (`min = 6`, `median = 16`, `max = 61`). | **"Service tenure in months (`months`, 6–61 months)"**. |
| Currency units | No currency symbol or country specified (`rev_Mean`, `totmrc_Mean`, `hnd_price`, etc.) | Undocumented currency scale (`rev_Mean` mean `58.72`, median `48.20`). | **"Monetary Units (MU)"**. |

---

## 6. Environment
- **Interpreter:** `/home/islam-raad/ai_workspace/bin/python3.12` — Python `3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0]`.
- **Required Packages (all pre-installed; 0 packages installed or upgraded):**
  - `pandas`: `3.0.2`
  - `numpy`: `2.4.4`
  - `scikit-learn` (`sklearn`): `1.8.0`
  - `xgboost`: `3.4.1`
  - `matplotlib`: `3.10.8`
  - `scipy`: `1.17.1`
  - `nbconvert`: `7.17.0`
  - `nbformat`: `5.10.4`
  - `joblib`: `1.5.3`
  - `ipykernel`: `7.2.0`
- **Optional Packages:**
  - `lightgbm`: `4.7.0` (available)
  - `shap`: not installed (guarded import with fallback per PRD §0.1; permutation + gain importance + partial dependence are primary per PRD §8.5)
  - `pymupdf` (`fitz`): `2.1` (available for PDF inspection/verification in `scripts/check_submission.py`)
- **Matplotlib Font Check (PRD §10):**
  - `Open Sans`: not installed locally (`False`)
  - `DejaVu Sans`: installed (`True`)
  - Configured `rcParams["font.sans-serif"] = ["Open Sans", "DejaVu Sans"]` so `DejaVu Sans` is used cleanly on this Linux workspace and `Open Sans` if available elsewhere.
- **Jupyter Kernel:** Registered `python3` kernelspec in `/home/islam-raad/ai_workspace/share/jupyter/kernels/python3/kernel.json` explicitly pointing to `/home/islam-raad/ai_workspace/bin/python3.12`.

---

## 7. Slides
*(To be populated in Phase 10 — capability probe results, Google Slides presentation ID/URL, layout notes.)*
