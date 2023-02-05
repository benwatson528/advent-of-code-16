def solve_p1(end, designer_num) -> int:
    return move((1, 1), end, designer_num)


def solve_p2(designer_num) -> int:
    return move_most_steps((1, 1), designer_num)


def move(start, end, designer_num):
    to_visit = [(start, 0)]
    min_to_coord = {start: 0}
    min_steps = 9999
    while to_visit:
        current, num_steps = to_visit.pop()
        if current in min_to_coord and min_to_coord[current] < num_steps:
            continue
        min_to_coord[current] = num_steps
        if num_steps >= min_steps:
            continue
        if current == end:
            min_steps = min(min_steps, num_steps)
            continue
        cx, cy = current
        if cx < 0 or cy < 0:
            continue
        if f"{(cx * cx + 3 * cx + 2 * cx * cy + cy + cy * cy) + designer_num:b}".count("1") % 2 != 0:
            continue
        to_visit.extend(
            ((cx + nx, cy + ny), min_to_coord[current] + 1) for (nx, ny) in [(-1, 0), (0, -1), (1, 0), (0, 1)])
    return min_steps


def move_most_steps(start, designer_num):
    to_visit = [(start, 0)]
    min_to_coord = {start: 0}
    while to_visit:
        current, num_steps = to_visit.pop()
        cx, cy = current
        if cx < 0 or cy < 0:
            continue
        if f"{(cx * cx + 3 * cx + 2 * cx * cy + cy + cy * cy) + designer_num:b}".count("1") % 2 != 0:
            continue
        if current in min_to_coord and min_to_coord[current] < num_steps:
            continue
        min_to_coord[current] = num_steps
        if num_steps == 50:
            continue
        to_visit.extend(
            ((cx + nx, cy + ny), min_to_coord[current] + 1) for (nx, ny) in [(-1, 0), (0, -1), (1, 0), (0, 1)])
    return len(min_to_coord)
