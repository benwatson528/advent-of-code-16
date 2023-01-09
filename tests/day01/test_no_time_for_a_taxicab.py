import os
from pathlib import Path

from main.day01.no_time_for_a_taxicab import solve


def test_p1_simple():
    assert solve("R5, L5, R5, R3".split(", "), False) == 12


def test_p1_real():
    assert solve(read_input("data/input.txt"), False) == 273


def test_p2_simple():
    assert solve("R8, R4, R4, R8".split(", "), True) == 4


def test_p2_real():
    assert solve(read_input("data/input.txt"), True) == 115


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().strip().split(", ")
