# Data Science Interview Exercise Set
## pandas · numpy · scikit-learn · scipy · statsmodels

---

## Purpose

Rebuild and sharpen Python data science skills for coding tests and technical interviews
(BCG X Data Analyst / Data Scientist, analytics engineering, quant roles).

**Constraint:** Official documentation only — no Stack Overflow, no LLM hints.

**Total: 96 exercises across 13 notebooks.**

---

## Full Curriculum

| # | Notebook | Topic | Exercises | Dataset |
|---|---|---|---|---|
| `00` | `data_cleaning` | String cleaning, dedup, outliers, date parsing, imputation pipeline | 8 | Synthetic hospital records |
| `00b` | `eda_and_statistics` | Distributions, correlations, cohort analysis, EDA automation | 8 | UK Online Retail |
| `01` | `pandas_foundations` | Indexing, GroupBy, merging, apply, pivot tables | 8 | IBM HR Analytics |
| `02` | `numpy_foundations` | Arrays, broadcasting, linear algebra, Monte Carlo, vectorization | 8 | Synthetic (finance/retail) |
| `03` | `pandas_advanced` | Window functions, MultiIndex, time series, reshape, RFM | 7 | UK Online Retail |
| `04` | `feature_engineering` | Encoding, scaling, binning, target encoding, feature selection | 7 | German Credit |
| `05` | `sklearn_pipelines` | ColumnTransformer, Pipeline, custom transformers | 7 | Titanic |
| `06` | `regression` | LinearReg, Ridge, Lasso, ElasticNet, CV, residual analysis | 7 | California Housing |
| `07` | `classification` | LogReg, Trees, RandomForest, SVM, ROC, imbalance | 7 | German Credit |
| `08` | `model_selection_tuning` | GridSearch, RandomSearch, nested CV, learning curves | 7 | Wine Quality |
| `09` | `unsupervised_learning` | KMeans, DBSCAN, PCA, silhouette analysis | 7 | Wholesale Customers |
| `10` | `capstone` | End-to-end churn prediction project (7 phases) | 7 phases | Telco Churn |
| `10b` | `statistical_modeling` | Hypothesis testing, A/B testing, OLS inference, ARIMA | 8 | Retail + Credit |

---

## Recommended Order

**Week 1 — Foundations**
```
00 → 00b → 01 → 02
```

**Week 2 — Feature Work**
```
03 → 04 → 05
```

**Week 3 — Modeling**
```
06 → 07 → 08 → 09
```

**Week 4 — Advanced & Integration**
```
10b → 10 (capstone)
```

---

## Workflow Per Notebook

1. **Read the business context** — understand what you're solving before touching code.
2. **Write the function** — implement inside the scaffold.
3. **Run the assert block** — silent = correct, AssertionError = fix and retry.
4. **Write the markdown interpretation** — mandatory for capstone and 10b.
5. **Export finished functions** to `solutions_XX.py` for pytest.

---

## How to Run Tests

```bash
# Single notebook test suite
pytest test_01_pandas_foundations.py -v

# All tests
pytest . -v

# With coverage
pytest . -v --tb=short
```

---

## Setup

```bash
pip install pandas numpy scikit-learn scipy statsmodels jupyter pytest
jupyter notebook
```

All datasets load from `sklearn.datasets.fetch_openml` — no manual downloads.
First run downloads to local cache (~200MB). Subsequent runs are instant.

---

## Interview Difficulty Map

| Notebook | Difficulty | Why |
|---|---|---|
| 00 data_cleaning | ⭐⭐ | Foundational but detail-heavy |
| 00b EDA | ⭐⭐⭐ | Cohort analysis is non-trivial |
| 01–02 pandas/numpy | ⭐⭐ | Core API, should feel comfortable |
| 03–04 advanced pandas / FE | ⭐⭐⭐ | Where mid-level candidates struggle |
| 05–07 sklearn | ⭐⭐⭐ | Pipeline patterns tested in every ML interview |
| 08 tuning | ⭐⭐⭐⭐ | Nested CV is a senior-level concept |
| 09 unsupervised | ⭐⭐⭐⭐ | Cluster interpretation is open-ended |
| 10b stats modeling | ⭐⭐⭐⭐ | ARIMA + post-hoc tests are advanced |
| 10 capstone | ⭐⭐⭐⭐⭐ | 4–6 hours, mirrors a real case |
