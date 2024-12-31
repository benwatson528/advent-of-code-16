import os
import re
from pathlib import Path

import pytest

from main.day22.grid_computing import solve_viable, solve_traverse


def test_p1_real():
    assert solve_viable(read_input("data/input.txt")) == 960


@pytest.mark.skip("Requires using the gui")
def test_p2_real():
    assert solve_traverse(read_input("data/input.txt")) == 225


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        parsed = {}
        for l in f.readlines():
            nums = [int(x) for x in re.findall(r"\d+", l)]
            parsed[(nums[0], nums[1])] = tuple(nums[2:])
        return parsed
