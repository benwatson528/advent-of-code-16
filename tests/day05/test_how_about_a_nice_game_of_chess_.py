import pytest

from main.day05.how_about_a_nice_game_of_chess_ import solve_p1, solve_p2


@pytest.mark.skip("Takes 5s to run")
def test_p1_simple():
    assert solve_p1("abc") == "18f47a30"


@pytest.mark.skip("Takes 5s to run")
def test_p1_real():
    assert solve_p1("wtnhxymk") == "2414bc77"


@pytest.mark.skip("Takes 8s to run")
def test_p2_simple():
    assert solve_p2("abc") == "05ace8e3"


@pytest.mark.skip("Takes 17s to run")
def test_p2_real():
    assert solve_p2("wtnhxymk") == "437e60fc"
