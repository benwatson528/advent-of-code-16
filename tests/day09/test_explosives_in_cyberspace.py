import os
from pathlib import Path

from main.day09.explosives_in_cyberspace import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == "X(3x3)ABC(3x3)ABCY"


def test_p1_real():
    assert len(solve_p1(read_input("data/input.txt"))) == 110346


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == len("XABCABCABCABCABCABCY")


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 10774309173


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().strip()
