"""
pytest companion for 01_pandas_foundations.ipynb
Run: pytest test_01_pandas_foundations.py -v
"""
import pytest
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml

@pytest.fixture(scope="module")
def hr():
    return fetch_openml(name='ibm-employee-attrition', version=1, as_frame=True, parser='auto').frame

# ---------------------------------------------------------------------------
# Import student solutions — students must save their functions in solutions_01.py
# ---------------------------------------------------------------------------
try:
    from solutions_01 import (
        get_sales_high_earners,
        data_quality_report,
        get_compensation_summary,
        merge_employee_reviews,
        enrich_hr_data,
        build_income_pivot,
        get_pay_outlier_summary,
        get_categorical_summary,
    )
    SOLUTIONS_AVAILABLE = True
except ImportError:
    SOLUTIONS_AVAILABLE = False

pytestmark = pytest.mark.skipif(not SOLUTIONS_AVAILABLE, reason="solutions_01.py not found — export your functions first")

# ---------------------------------------------------------------------------
# Exercise 1
# ---------------------------------------------------------------------------
def test_sales_high_earners_columns(hr):
    result = get_sales_high_earners(hr)
    assert list(result.columns) == ['EmployeeNumber', 'Department', 'JobRole', 'MonthlyIncome', 'Attrition']

def test_sales_high_earners_filter(hr):
    result = get_sales_high_earners(hr)
    assert (result['Department'] == 'Sales').all()
    assert (result['MonthlyIncome'] > hr['MonthlyIncome'].median()).all()

def test_sales_high_earners_index(hr):
    result = get_sales_high_earners(hr)
    assert result.index.tolist() == list(range(len(result)))

# ---------------------------------------------------------------------------
# Exercise 2
# ---------------------------------------------------------------------------
def test_data_quality_report_columns(hr):
    report = data_quality_report(hr)
    assert list(report.columns) == ['dtype', 'null_count', 'null_pct', 'n_unique']

def test_data_quality_report_index(hr):
    report = data_quality_report(hr)
    assert report.index.tolist() == list(hr.columns)

def test_data_quality_report_sorted(hr):
    report = data_quality_report(hr)
    assert report['null_pct'].is_monotonic_decreasing

# ---------------------------------------------------------------------------
# Exercise 3
# ---------------------------------------------------------------------------
def test_compensation_summary_columns(hr):
    result = get_compensation_summary(hr)
    expected = ['Department', 'JobLevel', 'MonthlyIncome_mean', 'MonthlyIncome_median',
                'MonthlyIncome_std', 'MonthlyIncome_min', 'MonthlyIncome_max', 'MonthlyIncome_count']
    assert list(result.columns) == expected

# ---------------------------------------------------------------------------
# Exercise 5
# ---------------------------------------------------------------------------
def test_enrich_hr_new_columns(hr):
    result = enrich_hr_data(hr)
    for col in ['salary_band', 'tenure_group', 'income_vs_avg']:
        assert col in result.columns

def test_enrich_hr_salary_bands(hr):
    result = enrich_hr_data(hr)
    assert set(result['salary_band'].unique()).issubset({'Low', 'Mid', 'High', 'Executive'})

def test_enrich_hr_income_vs_avg(hr):
    result = enrich_hr_data(hr)
    dept_check = result.groupby('Department')['income_vs_avg'].mean().abs()
    assert (dept_check < 0.01).all()

# ---------------------------------------------------------------------------
# Exercise 6
# ---------------------------------------------------------------------------
def test_income_pivot_structure(hr):
    result = build_income_pivot(hr)
    assert 'Overall_Mean' in result.columns
    assert result.index.name == 'Department'
    assert result['Overall_Mean'].is_monotonic_decreasing
    assert result.isna().sum().sum() == 0

# ---------------------------------------------------------------------------
# Exercise 7
# ---------------------------------------------------------------------------
def test_outlier_summary_structure(hr):
    result = get_pay_outlier_summary(hr)
    assert list(result.columns) == ['total_employees', 'n_outliers', 'outlier_pct']
    assert result['outlier_pct'].is_monotonic_decreasing
    assert result['total_employees'].sum() == len(hr)

# ---------------------------------------------------------------------------
# Exercise 8
# ---------------------------------------------------------------------------
def test_categorical_summary(hr):
    freq_tables, high_cardinality_cols = get_categorical_summary(hr)
    obj_cols = hr.select_dtypes(include='object').columns.tolist()
    assert set(freq_tables.keys()) == set(obj_cols)
    assert high_cardinality_cols == sorted(high_cardinality_cols)
