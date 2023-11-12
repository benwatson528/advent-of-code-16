import os
from pathlib import Path

from main.day23.safe_cracking import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 3


def test_p1_real():
    assert solve(read_input("data/input.txt"), 7) == 11424


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        return lines
