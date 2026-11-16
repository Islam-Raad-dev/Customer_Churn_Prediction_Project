# Customer Churn Prediction & Retention Strategy

End-to-end machine learning project for a telecom company (anonymized as **"Company A"**): predict which subscribers will churn, then decide with numbers whether a retention campaign is actually worth running.

Final project of the **GCI World Program** (Matsuo-Iwasawa Lab, University of Tokyo, 2026).

---

## Overview

A telecom operator loses subscribers every month, and a retention offer costs money even when it is sent to someone who would have stayed anyway. So the question is not only *"who will leave?"* but also *"is it profitable to spend on this segment?"*

This project answers both:

1. **Predict** the probability that each customer churns within 31–60 days after the observation date.
2. **Explain** the behavioral patterns behind churn (device age, subscription tenure, usage drop, bill shock).
3. **Convert** predictions into money: profit model, break-even analysis, sensitivity analysis.
4. **Recommend** a safe rollout: a narrow pilot plus a 90-day A/B test to measure the real effect of an offer.

## Key Results

| Item | Result |
|---|---|
| Data | 100,000 customers, 98 raw features + 28 engineered features |
| Final model | XGBoost (tuned, regularized) |
| ROC-AUC | **~0.70** (5-fold CV: 0.702 ± 0.001, held-out 30% test: ~0.703) |
| Improvement over logistic regression | +4.2 AUC points |
| Targeting power | Top 10% highest-risk customers are **3.3× more likely to churn** than average (after recalibration to a realistic 10% churn rate) |
| Break-even | Campaign is profitable only above **~4.2% true churn** (at top-10% targeting) |
| Recommendation | Start with a narrow top 1–2% pilot, then expand based on A/B test results |

### Main Findings

- **Device age threshold:** churn jumps by about **+24 percentage points** once the phone is older than ~300 days, validated with bootstrap confidence intervals, a local regression discontinuity check, and consistency across all 19 regions.
- **First-year cliff:** churn peaks at about **65% in month 11** of the subscription, which is consistent with a first-year contract or offer ending.
- **Usage collapse:** customers whose usage drops relative to their 3-month average are at much higher risk. This became the most important feature (`mou_ratio_3m`).
- **Missing data is informative:** a missing `change_mou` value is associated with ~76% churn, so missingness flags were added instead of blind imputation.
- **Fairness:** sensitive attributes (e.g., ethnicity) were removed from the final model with negligible loss in performance (~0.001 AUC).

> These are observational patterns, not proof of causation. This is why the plan includes a randomized A/B test.

## Methodology

| Stage | What was done |
|---|---|
| Data loading | Merged `Client.csv` and `Record.csv` on customer ID (validated one-to-one) |
| Data audit | Missing values, impossible values, outliers, duplicated columns, documentation vs. reality |
| EDA | Churn rate by bins with Wilson confidence intervals, heatmaps, robustness tests |
| Split | Stratified 70/30 train/test split (seed 42); all decisions made on training data only |
| Feature engineering | 28 behavioral features (thresholds, ratios, shares, missing flags) with a per-feature leakage check |
| Pipeline | Leakage-safe scikit-learn `Pipeline` + `ColumnTransformer` |
| Modeling | 7 models (M0–M6) compared with stratified 5-fold cross-validation |
| Evaluation | ROC-AUC, Precision@k, Lift@k, calibration (ECE, Brier), permutation importance, PDP, ablation |
| Recalibration | Label-shift correction (Saerens et al., 2002) because the sample has ~49.6% churners while real telecom churn is far lower |
| Financial model | Net profit = n × p_adj × s × V − n × c, break-even rate, scenarios, tornado sensitivity |
| Experiment design | 90-day A/B test with a holdout group and a clear expansion rule |

### Model Ladder

| ID | Model | CV AUC | Test AUC |
|---|---|---|---|
| M0 | Majority-class baseline | 0.5000 | 0.5000 |
| M1 | Logistic Regression + 28 features | 0.6603 | 0.6614 |
| M2 | Decision Tree (depth 4) | 0.6400 | 0.6401 |
| M3 | XGBoost on raw features | 0.6925 | 0.6936 |
| M4 | XGBoost + 28 engineered features | 0.7002 | 0.6992 |
| **M5** | **XGBoost tuned (final)** | **0.7020** | **0.7029** |
| M6 | LightGBM + 28 features | 0.7010 | 0.7021 |

M5 was selected using cross-validation, not the test set, to keep the test estimate honest. Values are rounded as reported in the project slides; re-running the notebook in a different environment may change the last digits slightly.

### Financial Assumptions

The data contains no cost, margin, or offer-success information, so these are **explicit assumptions**, not measured values:

| Parameter | Base value |
|---|---|
| Margin | 70% |
| Time horizon | 6 months |
| Offer save rate (s) | 20% |
| Offer cost per customer (c) | 8 monetary units (MU) |
| Customer value (V) | ARPU × margin × months |

Because the outcome depends strongly on the real churn rate in the market (profitable at 10%, loss-making at 2% with broad targeting), the project reports a range of scenarios rather than a single number.

## Repository Structure

```
Customer_Churn_Prediction_Project/
├── README.md
├── requirements.txt
├── dataset/
│   ├── Client.csv
│   ├── Record.csv
│   └── Company _A_ Dataset Overview.docx
├── docs/
│   └── UNDERSTANDING_AR.md          # Detailed project guide (Arabic)
├── notebooks/
│   └── churn_prediction.ipynb       # Full analysis, modeling, and financial model
├── outputs/
│   ├── figures/                     # Charts used in the report
│   ├── models/
│   │   └── final_xgb_m5_pipeline.joblib
│   └── tables/
│       ├── experiment_log.csv
│       └── test_predictions.csv
└── reports/
    ├── Project-overview.pdf         # Final 15-slide presentation
    └── references.txt
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Islam-Raad-dev/Customer_Churn_Prediction_Project.git
cd Customer_Churn_Prediction_Project
```

### 2. Create an environment and install dependencies

```bash
python -m venv env
source env/bin/activate        # Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the notebook

```bash
jupyter notebook notebooks/churn_prediction.ipynb
```

Run the cells from top to bottom. The notebook reads the data from `dataset/` and writes figures, tables, and the trained model into `outputs/`.

### 4. Load the trained model (optional)

```python
import joblib
model = joblib.load("outputs/models/final_xgb_m5_pipeline.joblib")
# model.predict_proba(X)[:, 1] -> churn probability
```

## Tech Stack

- **Language:** Python
- **Data:** Pandas, NumPy
- **Modeling:** scikit-learn, XGBoost, LightGBM
- **Statistics:** SciPy
- **Visualization:** Matplotlib
- **Persistence:** joblib
- **Environment:** Jupyter Notebook

## Data

The data comes from the GCI World 2026 course material: an anonymized telecom dataset (`Client.csv` with 50 columns and `Record.csv` with 51 columns, 100,000 customers each). It is **not** data from an Iraqi or any specific real company, and it is used here for educational purposes only. Column names closely resemble the public Cell2Cell churn dataset, but this was not confirmed by the course. See `dataset/Company _A_ Dataset Overview.docx` for the official description.

## Limitations

- The sample is nearly balanced (~49.6% churners), which is unrealistic; this is handled with recalibration, but the real churn rate is still an assumption.
- Financial results depend on assumed margin, save rate, and offer cost, which are not in the data.
- Patterns such as the 300-day threshold are correlational. Only the A/B test can prove that an offer actually retains customers.
- ROC-AUC of ~0.70 is typical for noisy human-behavior data: the model ranks customers usefully, but it does not predict each individual with high accuracy.

## Documentation

- **Presentation:** [`reports/Project-overview.pdf`](reports/Project-overview.pdf)
- **References:** [`reports/references.txt`](reports/references.txt)
- **Detailed guide (Arabic):** [`docs/UNDERSTANDING_AR.md`](docs/UNDERSTANDING_AR.md)

## Disclosure

AI assistants were used during development, as permitted by the program, and are disclosed in the references. All results and decisions in this repository were reviewed and are understood by the author.

## Author

**Islam Raad Fathi**
AI Engineering Student, University of Mosul

- GitHub: [Islam-Raad-dev](https://github.com/Islam-Raad-dev)
- LinkedIn: [islam-raad](https://www.linkedin.com/in/islam-raad/)