"""
Unit tests — real companies mein tests zaroori hote hain!

Run karo:
    python tests/test_cleaner.py
    # ya pytest install ho toh:
    python -m pytest tests/ -v
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.data_loader  import load_raw
from src.data_cleaner import clean


def test_no_nulls():
    df = clean(load_raw())
    assert df.isnull().sum().sum() == 0, "Null values found after cleaning!"


def test_new_columns_exist():
    df = clean(load_raw())
    for col in ["pop_density", "pop_crore", "pop_share_pct"]:
        assert col in df.columns, f"Column '{col}' missing after cleaning!"


def test_pop_share_sums_to_100():
    df = clean(load_raw())
    total = df["pop_share_pct"].sum()
    assert abs(total - 100.0) < 0.1, f"pop_share_pct sums to {total}, expected ~100"


def test_sorted_by_population():
    df = clean(load_raw())
    assert df.iloc[0]["state"] == "Uttar Pradesh", "Rank 1 should be Uttar Pradesh!"


def test_row_count():
    df = clean(load_raw())
    assert len(df) == 30, f"Expected 30 rows, got {len(df)}"


def test_pop_density_positive():
    df = clean(load_raw())
    assert (df["pop_density"] > 0).all(), "Some pop_density values are <= 0!"


if __name__ == "__main__":
    tests = [
        test_no_nulls,
        test_new_columns_exist,
        test_pop_share_sums_to_100,
        test_sorted_by_population,
        test_row_count,
        test_pop_density_positive,
    ]
    print("\nRunning tests...\n")
    passed = 0
    for t in tests:
        try:
            t()
            print(f"  [PASS] {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  [FAIL] {t.__name__}: {e}")

    print(f"\n  {passed}/{len(tests)} tests passed\n")
