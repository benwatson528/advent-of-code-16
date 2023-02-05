from main.day13.a_maze_of_twisty_little_cubicles import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1((7, 4), 10) == 11


def test_p1_real():
    assert solve_p1((31, 39), 1362) == 82


def test_p2_real():
    assert solve_p2(1362) == 138
