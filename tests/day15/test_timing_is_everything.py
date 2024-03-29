import os
import re
from pathlib import Path

from main.day15.timing_is_everything import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 5


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 203660


def test_p2_real():
    discs = read_input("data/input.txt")
    discs.append((len(discs) + 1, 11, 0, 0))
    assert solve(discs) == 2408135


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f.read().splitlines():
            raw_nums = re.findall(r"(\d+)", line)
            lines.append(tuple(int(num) for num in raw_nums))
    return lines
