import os
from pathlib import Path

from main.day06.signals_and_noise import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), True) == "easter"


def test_p1_real():
    assert solve(read_input("data/input.txt"), True) == "qoclwvah"


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), False) == "advent"


def test_p2_real():
    assert solve(read_input("data/input.txt"), False) == "ryrgviuv"


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
