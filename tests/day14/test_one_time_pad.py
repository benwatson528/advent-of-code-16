import pytest

from main.day14.one_time_pad import solve


def test_p1_simple():
    assert solve("abc", 64) == 22728


def test_p1_real():
    assert solve("jlmsuwbz", 64) == 35186


@pytest.mark.skip("Takes 22s to run")
def test_p2_simple():
    assert solve("abc", 64, 2016) == 22551


@pytest.mark.skip("Takes 22s to run")
def test_p2_real():
    assert solve("jlmsuwbz", 64, 2016) == 22429
