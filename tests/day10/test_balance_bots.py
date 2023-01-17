import os
from pathlib import Path

from main.day10.balance_bots import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), (5, 2)) == 2


def test_p1_real():
    assert solve(read_input("data/input.txt"), (61, 17)) == 93


def test_p2_real():
    assert solve(read_input("data/input.txt")) == 47101


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
