def solve(discs) -> int:
    drop_time = 0
    while True:
        if is_valid_position(discs, drop_time):
            break
        drop_time += 1
    return drop_time


def is_valid_position(discs, drop_time):
    for disc in discs:
        position = (disc[0] + drop_time + disc[3]) % disc[1]
        if position != 0:
            return False
    return True
