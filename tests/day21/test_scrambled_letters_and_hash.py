import os
from pathlib import Path

from main.day21.scrambled_letters_and_hash import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), "abcde") == "decab"


def test_p1_real():
    assert solve(read_input("data/input.txt"), "abcdefgh") == "gcedfahb"


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
