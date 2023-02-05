import os
from pathlib import Path

from main.day12.leonardo_s_monorail import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 42


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 318009


def test_p2_real():
    assert solve(read_input("data/input.txt"), True) == 9227663


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
