"""
tests_1c.py

This module contains unit tests for the `max_subarray_sum` function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_exampleUsage():
    assert two_sum([2, 7, 11, 15], 9) == [0,1] # from the file itself

def test_sameNum():
    assert two_sum([1,1,5,5], 10) == [2,3] # using the same number, different index

def test_sameIndex():
    assert two_sum([2,3,5], 10) == [] # doesnt use the same index twice

def test_positiveNegative():
    assert two_sum([-2,-3,10], -5) == [0,1] # negative numbers
    assert two_sum([-2,-3,10], 7) == [1,2] # negative and positive numbers
    assert two_sum([10,-3,-2], 8) == [0,2] # positive and negative numbers

def test_bigList():
    assert two_sum([694, 1155, 1690, 1778, 2265, 2910], 3420) == [1,4] # big list

def test_firstAnswer():
    assert two_sum([1,1,1], 2) == [0,1] # first answer

if __name__ == "__main__":
    pytest.main()