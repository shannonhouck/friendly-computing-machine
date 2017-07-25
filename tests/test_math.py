"""
Testing the math.py module!
"""

import friendly_computing_machine as fcm
import pytest

# Testing....
def test_add():
    assert fcm.math.add(5, 2) == 7
    assert fcm.math.add(5, 5) == 10

def test_mult():
    assert fcm.math.mult(5, 2) == 10
    assert fcm.math.mult(5, 5) == 25
