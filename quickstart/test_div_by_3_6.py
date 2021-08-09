"""For executing fixtures"""
import pytest

# remove for using conftest!

# @pytest.fixture
# def input_value():
#    input = 39
#    return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0