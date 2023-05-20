import os
from pathlib import Path

from main.day20.firewall_rules import solve_lowest, solve_allowed


def test_p1_simple():
    assert solve_lowest(read_input("data/test_input.txt")) == 3


def test_p1_real():
    assert solve_lowest(read_input("data/input.txt")) == 17348574


def test_p2_real():
    assert solve_allowed(read_input("data/input.txt")) == 104


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [range(int(line.split("-")[0]), int(line.split("-")[1])) for line in f.read().splitlines()]
