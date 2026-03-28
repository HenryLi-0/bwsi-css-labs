"""
tests_1c.py

This module contains unit tests for the `max_subarray_sum` function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_exampleUsage():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6 # from the file itself

def test_consecutive():
    assert max_subarray_sum([-2, -1, 0, 1, 2]) == 3 # consecutive numbers (including negative, zero, and positive)

def test_elements():
    assert max_subarray_sum([5]) == 5 # single element
    assert max_subarray_sum([5, -3]) == 5 # two elements
    assert max_subarray_sum([5, -3, 9]) == 11 # three elements
    assert max_subarray_sum([5, -3, -1]) == 5 # three elements
    assert max_subarray_sum([5, -3, 3]) == 5 # three elements

def test_none():
    assert max_subarray_sum([]) == 0 # no elements??? where'd they go...

def test_withZeros():
    assert max_subarray_sum([-100, 0, 1, 2, 3, 0, 100]) == 106 # random zeros and bigger numbers

def test_withZerosBackwards():
    assert max_subarray_sum([100, 0, 1, 2, 3, 0, -100]) == 106 # swap -100 and 100 positions


if __name__ == "__main__":
    pytest.main()