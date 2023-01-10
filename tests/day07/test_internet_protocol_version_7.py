import os
from pathlib import Path

from main.day07.internet_protocol_version_7 import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), True) == 2


def test_p1_real():
    assert solve(read_input("data/input.txt"), True) == 115


def test_p2_real():
    assert solve(read_input("data/input.txt"), False) == 231


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
