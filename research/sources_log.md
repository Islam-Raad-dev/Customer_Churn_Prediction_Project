# External Sources Log — Company A Telecom Churn PoC

> **Rule (PRD §0.5 & §7):** Every external statistic, market fact, benchmark, or academic method cited in the slides or notebook must come from a source actually opened and verified during Phase 3, logged below with full provenance, and matched 1-to-1 with `[n]` slide tags and `references.txt`.

## 1. Phase 3 Search Plan (T3.1 — Mapped to PRD §7 Questions)

| Research Question (PRD §7) | Target Authorities / Venues | Planned Search Queries |
|---|---|---|
| **Q1. Iraq mobile market state** (subscribers, penetration, operators, shares) | DataReportal (*Digital 2024/2025: Iraq*), GSMA Intelligence, ITU, CMC Iraq (Communications and Media Commission), Zain Group / Ooredoo (Asiacell) Annual Reports | `"Digital 2024 Iraq" OR "Digital 2025 Iraq" DataReportal mobile connections penetration` · `"Zain Iraq" subscribers market share 2024 2025 Zain Group annual report` · `"Asiacell" subscribers Ooredoo annual report 2024` · `"Korek Telecom" CMC Iraq subscribers` |
| **Q2. Local churn drivers** (competition, multi-SIM, price/regulation, network quality, 4G/5G/eSIM) | CMC Iraq, GSMA *Mobile Economy MENA*, Zain / Ooredoo reports | `Iraq telecom multi-SIM prepaid competition 4G 5G CMC Zain Asiacell` · `GSMA Mobile Economy MENA mobile penetration SIM connections` |
| **Q3. Retention vs. acquisition economics & realistic churn benchmarks** | Peer-reviewed telecom churn literature, Harvard Business Review / Bain, industry telecom reports | `telecom customer churn rate benchmark monthly annual 1.5% 2% wireless` · `customer retention vs acquisition cost telecommunications Reichheld Bain` |
| **Q4. Voluntary vs. involuntary churn & what ML can influence** | Telecom churn literature (Verbeke et al., Neslin et al.) | `voluntary vs involuntary churn telecommunications predictive modeling` |
| **Q5. Handset-upgrade / commitment cycles vs. churn** | Telecom industry / academic studies on contract expiry and handset replacement cycles | `handset replacement cycle contract expiration telecom churn cliff` |
| **Q6. Retention-campaign success rates & offer costs** | Academic empirical studies (Neslin et al. *Journal of Marketing Research*; Ascarza *Journal of Marketing Research*; Verbeke et al. *European Journal of Operational Research*) | `Neslin Gupta Kamakura Lu Mason customer churn tournament telecom retention` · `Ascarza 2018 retention futility proactive churn intervention` · `Verbeke Dejaeger Martens Hur Baesens 2012 profit driven churn prediction` |
| **Q7. Peer-reviewed papers on telecom churn prediction & why gradient-boosted trees win on tabular data** | *European Journal of Operational Research*, *Information Sciences*, KDD (Chen & Guestrin XGBoost; Grinsztajn et al. NeurIPS 2022) | `Verbeke 2012 new insights into churn prediction in the telecommunication sector` · `Chen Guestrin 2016 XGBoost KDD` · `Grinsztajn Oyallon Varoquaux 2022 why do tree-based models still outperform deep learning on typical tabular data` · `Saerens Latinne Decaestecker 2002 adjusting the outputs of a classifier to new a priori probabilities` |

---

## 2. Verified Sources Table (T3.2)

| ID | Title | Publisher / Venue | Publication Date | URL | Access Date | Specific Fact / Metric Used | Reliability Note |
|---|---|---|---|---|---|---|---|
