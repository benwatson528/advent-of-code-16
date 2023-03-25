from main.day19.an_elephant_named_joseph import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(5) == 3


def test_p1_real():
    assert solve_p1(3004953) == 1815603


def test_p2_simple():
    assert solve_p2(5) == 2


def test_p2_real():
    assert solve_p2(3004953) == 1410630
