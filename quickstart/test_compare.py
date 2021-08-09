"""For executing markers"""
import pytest


@pytest.mark.xfail # for ignoring failure
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100


@pytest.mark.xfail # for ignoring failure
@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100


@pytest.mark.skip # for skipping test
@pytest.mark.others
def test_less():
   num = 100
   assert num < 200
