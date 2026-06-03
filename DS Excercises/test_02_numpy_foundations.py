"""
pytest companion tests for notebooks 02–09.
Run all: pytest . -v
Run one file: pytest test_02_numpy_foundations.py -v
"""

# ============================================================
# test_02_numpy_foundations.py
# ============================================================
import pytest
import numpy as np

try:
    from solutions_02 import (
        array_summary, clv_loop, clv_vectorized
    )
    SOLUTIONS_AVAILABLE = True
except ImportError:
    SOLUTIONS_AVAILABLE = False

pytestmark_02 = pytest.mark.skipif(not SOLUTIONS_AVAILABLE, reason="solutions_02.py not found")

@pytest.fixture(scope="module")
def revenue_fixture():
    np.random.seed(42)
    return np.random.randint(10_000, 500_001, size=(5, 36))

@pytest.fixture(scope="module")
def growth_fixture():
    return np.linspace(0.98, 1.05, 36)

def test_array_summary_keys(revenue_fixture):
    s = array_summary(revenue_fixture)
    assert set(s.keys()) == {'shape', 'dtype', 'min', 'max', 'mean', 'std'}

def test_array_summary_shape(revenue_fixture):
    s = array_summary(revenue_fixture)
    assert s['shape'] == (5, 36)

def test_growth_rates_endpoints(growth_fixture):
    assert abs(growth_fixture[0] - 0.98) < 1e-6
    assert abs(growth_fixture[-1] - 1.05) < 1e-6

def test_clv_results_match():
    np.random.seed(1)
    rev = np.random.uniform(50, 500, size=(100, 24))
    churn = np.random.uniform(0.01, 0.15, size=(100,))
    result_loop = clv_loop(rev, churn, 0.01)
    result_vec = clv_vectorized(rev, churn, 0.01)
    assert np.allclose(result_loop, result_vec, atol=1e-6)

def test_clv_shape():
    np.random.seed(1)
    rev = np.random.uniform(50, 500, size=(100, 24))
    churn = np.random.uniform(0.01, 0.15, size=(100,))
    assert clv_vectorized(rev, churn, 0.01).shape == (100,)
