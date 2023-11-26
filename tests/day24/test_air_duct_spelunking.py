import os
from pathlib import Path

from main.day24.air_duct_spelunking import solve


def test_p1_simple():
    walkable, poi = read_input("data/test_input.txt")
    assert solve(walkable, poi) == 456


def test_p1_real():
    walkable, poi = read_input("data/input.txt")
    assert solve(walkable, poi) == 0


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        walkable = set()
        poi = {}
        for i, x in enumerate(f.read().splitlines()):
            for j, y in enumerate(x):
                if y != '#':
                    walkable.add((i, j))
                if y.isdigit():
                    poi[(i, j)] = int(y)
        return walkable, poi
