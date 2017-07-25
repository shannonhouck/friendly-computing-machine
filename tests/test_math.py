"""
Testing the math.py module!
"""

import friendly_computing_machine as fcm
import pytest

# Testing....
def test_add():
    assert fcm.math.add(5, 2) == 7
    assert fcm.math.add(2, 5) == 7

