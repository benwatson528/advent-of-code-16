import os
from pathlib import Path

import pytest

from main.day25.clock_signal import solve


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 175


# @pytest.mark.skip(reason="It's pretty slow")
# def test_p2_real():
#     assert solve(read_input("data/input.txt"), 12) == 479007984


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        return lines
