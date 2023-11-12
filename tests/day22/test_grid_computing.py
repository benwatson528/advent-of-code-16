import os
from pathlib import Path

from main.day22.grid_computing import solve_viable, solve_traverse


def test_p1_real():
    assert solve_viable(read_input("data/input.txt")) == 960


def test_p2_test():
    assert solve_traverse(read_input("data/test_input.txt")) == -1


def test_p2_real():
    assert solve_traverse(read_input("data/input.txt")) == -1


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        split = [line.split() for line in f.read().splitlines()[2:]]

        parsed = {}
        for s in split:
            x = int(s[0].split("-")[-2][1:])
            y = int(s[0].split("-")[-1][1:])
            parsed[(x, y)] = (int(s[1][:-1]), int(s[2][:-1]), int(s[3][:-1]), int(s[4][:-1]))
        return parsed
