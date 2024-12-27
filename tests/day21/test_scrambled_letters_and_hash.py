import itertools
import os
from pathlib import Path

import pytest

from main.day21.scrambled_letters_and_hash import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), "abcde") == "decab"


def test_p1_real():
    assert solve(read_input("data/input.txt"), "abcdefgh") == "gcedfahb"


@pytest.mark.skip("Takes 9s to run")
def test_p2_real():
    for permutation in itertools.permutations("abcdefgh"):
        if solve(read_input("data/input.txt"), permutation) == "fbgdceah":
            assert "".join(permutation) == "hegbdcfa"


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
