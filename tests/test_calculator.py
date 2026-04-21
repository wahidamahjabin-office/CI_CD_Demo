import pytest
import sys
import os

# Make sure the src folder is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.calculator import add, subtract, multiply, divide


# ── Test 1: Basic arithmetic ──────────────────────────────────────────────────

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


# ── Test 2: Edge cases ────────────────────────────────────────────────────────

def test_divide_by_zero_raises_error():
    """Dividing by zero should raise a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

def test_add_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000

def test_multiply_by_zero():
    assert multiply(999, 0) == 0
