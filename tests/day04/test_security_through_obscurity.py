import os
from pathlib import Path

from main.day04.security_through_obscurity import solve_validate, solve_decrypt


def test_p1_real():
    assert solve_validate(read_input("data/input.txt")) == 173787


def test_p2_real():
    assert solve_decrypt(read_input("data/input.txt")) == 548


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        rooms = []
        for line in f.read().splitlines():
            name = "".join(line.split("-")[:-1])
            sector_id = "".join("".join(line.split("-")[-1:]).split("[")[0])
            checksum = "".join("".join(line.split("[")[1:])[:-1])
            rooms.append((name, sector_id, checksum))
        return rooms
