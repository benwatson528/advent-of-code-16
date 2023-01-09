import os
from pathlib import Path

from main.day02.bathroom_security import solve

FIRST_KEYPAD = {(0, 0): "1", (0, 1): "2", (0, 2): "3",
                (1, 0): "4", (1, 1): "5", (1, 2): "6",
                (2, 0): "7", (2, 1): "8", (2, 2): "9"}

RAW_SECOND_KEYPAD = """
    1
  2 3 4
5 6 7 8 9
  A B C
    D
""".splitlines()


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), FIRST_KEYPAD) == "1985"


def test_p1_real():
    assert solve(read_input("data/input.txt"), FIRST_KEYPAD) == "99332"


def test_p2_simple():
    keypad = parse_second_keypad()
    assert solve(read_input("data/test_input.txt"), keypad) == "5DB3"


def test_p2_real():
    keypad = parse_second_keypad()
    assert solve(read_input("data/input.txt"), keypad) == "DD483"


def parse_second_keypad():
    grid = {}
    for i in range(len(RAW_SECOND_KEYPAD)):
        for j in range(len(RAW_SECOND_KEYPAD[i])):
            if RAW_SECOND_KEYPAD[i][j] not in (" ", "\n"):
                grid[(i - 1, j // 2)] = RAW_SECOND_KEYPAD[i][j]
    return grid


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
