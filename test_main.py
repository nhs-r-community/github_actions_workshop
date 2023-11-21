"""
Tests for main.py
"""

import pytest

import main


@pytest.mark.parametrize(
    ["num_1", "num_2", "expected"],
    [
        (0, 0, 0),
        (1, 1, 2),
        (1, -1, 0),
        (0.1, 0.1, 0.2),
    ]
)
def test_example_add(num_1, num_2, expected):
    """
    Tests main.example_add
    """
    actual = main.example_add(num_1, num_2)

    assert actual==expected


# @pytest.mark.parametrize(
#     ["num_1", "num_2", "expected"],
#     [
#         (0, 0, 0),
#         (1, 1, 2),
#         (1, -1, 0),
#         (0.1, 0.1, 0.2),
#     ]
# )
# def test_example_bad_add(num_1, num_2, expected):
#     """
#     Tests main.example_bad_add
#     """
#     actual = main.example_bad_add(num_1, num_2)

#     assert actual==expected
