import pytest

from main.day11.radioisotope_thermoelectric_generators import solve


def test_p1_simple():
    components = {(1, "HM"), (1, "LM"),
                  (2, "HG"),
                  (3, "LG")}
    assert solve(components) == 11


@pytest.mark.skip("Runs in 5.5s")
def test_p1_real():
    components = {(1, "PRG"), (1, "PRM"),
                  (2, "COG"), (2, "CUG"), (2, "RG"), (2, "PLG"),
                  (3, "COM"), (3, "CUM"), (3, "RM"), (3, "PLM")}
    assert solve(components) == 33


@pytest.mark.skip("Runs in 8m")
def test_p2_real():
    components = {(1, "PRG"), (1, "PRM"), (1, "ELG"), (1, "ELM"), (1, "DIG"), (1, "DIM"),
                  (2, "COG"), (2, "CUG"), (2, "RG"), (2, "PLG"),
                  (3, "COM"), (3, "CUM"), (3, "RM"), (3, "PLM")}
    assert solve(components) == 57
