import os
import re
from pathlib import Path

from main.day03.squares_with_three_sides import solve_rows, solve_columns


def test_p1_real():
    assert solve_rows(read_input("data/input.txt")) == 869


def test_p2_real():
    assert solve_columns(read_input("data/input.txt")) == 1544


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        nums = [re.findall(r"\d+", line) for line in f.read().splitlines()]
        return [(int(i[0]), int(i[1]), int(i[2])) for i in nums]
