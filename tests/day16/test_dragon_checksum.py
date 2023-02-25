from main.day16.dragon_checksum import solve


def test_p1_simple():
    assert solve("10000", 20) == "01100"


def test_p1_real():
    assert solve("10111100110001111", 272) == "11100110111101110"


def test_p2_real():
    assert solve("10111100110001111", 35651584) == "10001101010000101"
