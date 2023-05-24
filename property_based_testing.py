#!/bin/python3
from hypothesis import given
import hypothesis.strategies as some

import awesome_math
import awesome_sort
import awesome_logger

# @given(a = some.integers(), b = some.integers())
# def test_add_must_return_sum_of_arguments(a, b):
#     assert(awesome_math.add(a,b) == a+b)

@given(list = some.lists(some.integers()))
def test_bubble_sort_list_size_is_invariant(list):
    initial_size = len(list)
    awesome_sort.bubble_sort(list)
    assert(len(list) == initial_size)

@given(list = some.lists(some.integers()))
def test_bubble_sort_list_is_sorted(list):
    awesome_sort.bubble_sort(list)
    for i in range(len(list)-1):
        assert(list[i] <= list[i+1])

@given(error_code = some.integers(min_value=0, max_value=(awesome_logger.NUMBER_OF_ERROR_MESSAGES-1)))
def test_awesome_logger_returns_valid_string(error_code):
    error_message = awesome_logger.get_error_code_message(error_code)
    assert(isinstance(error_message, str))
    assert(len(error_message) > 0)