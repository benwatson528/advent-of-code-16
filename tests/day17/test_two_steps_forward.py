from main.day17.two_steps_forward import solve_shortest, solve_longest


def test_p1_simple():
    assert solve_shortest("ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"


def test_p1_real():
    assert solve_shortest("mmsxrhfx") == "RLDUDRDDRR"


def test_p2_simple():
    assert solve_longest("ulqzkmiv") == 830


def test_p2_real():
    assert solve_longest("mmsxrhfx") == 590
