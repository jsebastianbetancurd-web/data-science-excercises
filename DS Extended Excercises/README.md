# Extended Data Science Exercise Set
## SQL (DuckDB) · XGBoost · LightGBM · Ensembles · ML Theory · Optimization · Causal Inference · NLP · Model Deployment

---

## Purpose

This set fills the gaps between the core DS curriculum and what senior data science roles actually test. Every notebook is built around the **learn-by-doing** philosophy: mathematical derivations are pre-written so you understand the theory, implementations are left blank so you build the intuition, and assertions verify your work against known references.

**Constraint:** Official documentation only — no Google, no AI assistance.

**Total: 136 exercises across 14 notebooks.**

---

## Full Curriculum

| # | Notebook | Topic | Exercises | Libraries |
|---|---|---|---|---|
| `S01` | `sql_foundations` | SELECT, WHERE, aggregation, JOINs, subqueries, NULL handling | 10 | `duckdb` |
| `S02` | `sql_window_functions` | ROW_NUMBER, RANK, LAG/LEAD, running totals, NTILE, gaps & islands, cohort retention | 10 | `duckdb` |
| `S03` | `sql_advanced` | Recursive CTEs, GROUPING SETS, PIVOT/UNPIVOT, set operations, ASOF JOIN, Parquet | 10 | `duckdb` |
| `S04` | `sql_data_science` | Feature engineering in SQL, A/B test analysis, funnel analysis, basket analysis, sessionization | 10 | `duckdb` |
| `M01` | `xgboost` | XGBoost classifier/regressor, DMatrix API, SHAP, monotone constraints, calibration | 10 | `xgboost` |
| `M02` | `lightgbm` | LightGBM native API, leaf-wise growth, DART, focal loss, interaction constraints | 10 | `lightgbm` |
| `M03` | `ensembles_stacking` | Voting, OOF stacking, sklearn StackingClassifier, diversity, optimal blend weights | 6+ | `xgboost`, `lightgbm` |
| `M04` | `algorithms_from_scratch` | Linear/Ridge regression, gradient descent, logistic regression, decision tree, KNN, Naive Bayes, PCA, K-Means | 10 | `numpy` |
| `M05` | `optimization_from_scratch` | SGD + schedules, Momentum, Nesterov, RMSProp, Adam, regularization, Newton's method, neural net | 10 | `numpy` |
| `C01` | `causal_inference_did_rdd` | Naive estimator bias, DiD, parallel trends, RDD, IV/2SLS, PSM, synthetic control, AIPW | 10 | `statsmodels` |
| `C02` | `causal_ml_econml` | Meta-learners (S/T/X), Double ML, Causal Forest, policy learning, CATE validation, sensitivity | 10 | `econml` |
| `N01` | `classical_nlp` | Text preprocessing, TF-IDF from scratch, n-grams, NB from scratch, spaCy features, LDA, retrieval | 10 | `spacy`, `sklearn` |
| `N02` | `embeddings_nlp` | Mean/weighted pooling, vector arithmetic, semantic search, LSA, NER, clustering, summarization | 10 | `spacy`, `sklearn` |
| `D01` | `model_deployment` | Model serialization, Pydantic validation, FastAPI, A/B testing, drift detection, retraining pipeline | 10 | `fastapi`, `joblib` |

---

## Recommended Order

**Week 1 — SQL (highest interview ROI)**
```
S01 → S02 → S03 → S04
```

**Week 2 — Gradient Boosting**
```
M01 → M02 → M03
```

**Week 3 — Theory (whiteboard readiness)**
```
M04 → M05
```

**Week 4 — Causal Inference (BCG X differentiator)**
```
C01 → C02
```

**Week 5 — NLP**
```
N01 → N02
```

**Week 6 — Deployment (portfolio differentiator)**
```
D01
```

---

## Setup

```bash
pip install duckdb xgboost lightgbm econml spacy fastapi uvicorn joblib httpx pydantic
python -m spacy download en_core_web_sm
jupyter notebook
```

---

## What Makes These Notebooks Different

### SQL notebooks
- Every query is tested against a pandas reference solution
- DuckDB runs entirely in-process — no database server needed
- Exercises progress from retrieval to full ML pipelines in SQL
- S04 covers patterns that appear in production data engineering roles

### Theory notebooks (M04, M05)
- Pre-written math derivations — read them before implementing
- Your scratch implementation is verified against sklearn within tolerance
- Teaches *why* each algorithm works, not just *how* to call it
- These are the exercises that prepare you for whiteboard rounds

### Causal Inference (C01, C02)
- The most underrepresented topic in standard DS curricula
- C01 covers the statistical methods (DiD, RDD, IV, PSM, synthetic control)
- C02 covers ML-based CATE estimation with EconML
- BCG X and consulting-oriented data science roles specifically probe this

### Deployment (D01)
- The full ML lifecycle: train → serialize → serve → monitor → retrain
- FastAPI app you write is production-runnable, not just a toy
- Covers drift detection, A/B testing, and SHAP explanations in an API context

---

## Difficulty Map

| Notebook | Difficulty | Key challenge |
|---|---|---|
| S01 | ⭐⭐ | DuckDB syntax, query structure |
| S02 | ⭐⭐⭐ | Frame semantics, gaps-and-islands |
| S03 | ⭐⭐⭐⭐ | Recursive CTEs, GROUPING SETS |
| S04 | ⭐⭐⭐⭐ | Full pipelines, basket analysis |
| M01 | ⭐⭐⭐ | API depth, SHAP, constraints |
| M02 | ⭐⭐⭐ | Custom loss derivation |
| M03 | ⭐⭐⭐⭐ | OOF implementation, diversity |
| M04 | ⭐⭐⭐⭐ | PCA + KMeans from scratch |
| M05 | ⭐⭐⭐⭐⭐ | Neural net backprop from scratch |
| C01 | ⭐⭐⭐⭐ | Synthetic control optimization |
| C02 | ⭐⭐⭐⭐⭐ | CATE estimation, policy learning |
| N01 | ⭐⭐⭐ | TF-IDF + NB from scratch |
| N02 | ⭐⭐⭐ | Vector operations, TextRank |
| D01 | ⭐⭐⭐⭐ | Full API + monitoring system |

---

## Combined Curriculum Summary

| Set | Notebooks | Exercises |
|---|---|---|
| Core DS (original set) | 13 | 96 |
| Visual Analytics | 8 | 75 |
| Extended DS (this set) | 14 | 136 |
| **Total** | **35** | **307** |
