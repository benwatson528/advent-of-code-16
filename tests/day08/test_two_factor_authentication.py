import os
from pathlib import Path

from main.day08.two_factor_authentication import solve


def test_p1_test():
    assert solve(read_input("data/test_input.txt"), 7, 3) == 6


def test_p1_real():
    assert solve(read_input("data/input.txt"), 50, 6) == 115


# p2 real = EFEYKFRFIJ


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
