import pytest

from main.day18.like_a_rogue import solve


def test_p1_simple():
    assert solve(".^^.^.^^^^", 10) == 38


def test_p1_real():
    assert solve("^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.",
                 40) == 1926


@pytest.mark.skip("Takes 12s to run")
def test_p2_real():
    assert solve("^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.",
                 400000) == 19986699
