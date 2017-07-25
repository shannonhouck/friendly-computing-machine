"""
Testing the math.py module!
"""

import friendly_computing_machine as fcm
import pytest

# Testing....
def test_add():
    assert fcm.math.add(5, 2) == 7
    assert fcm.math.add(5, 5) == 10

testdata  = [
    (2, 5, 10),
    (1, 2, 2),
    (11, 9, 99),
    (11, 0, 0),
    (0, 0, 0),
]
@pytest.mark.parametrize("a,b,expected", testdata)
def test_mult(a, b, expected):
    assert fcm.math.mult(a, b) == expected

def test_pow():
    assert fcm.math.pow(10, 3) == 1000
    assert fcm.math.pow(2, 4) == 16
    assert fcm.math.pow(2, 0.5) == 0

