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

---

## 2. Assumptions
*(To be populated in Phase 3 & Phase 8 — every input marked `SOURCED [ID]` or `ASSUMPTION`.)*

---

## 3. Hypotheses
*(To be populated in Phase 2 — ranked by actionability.)*

---

## 4. Feature Dictionary
*(To be populated in Phase 5 — name, formula, business reason, leakage check, kept?)*

---

## 5. Data-Doc Discrepancies
*(To be populated in T1.6 — comparing `ENG_Company _A_ Dataset Overview.docx` against `telecom/*.csv`.)*

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
