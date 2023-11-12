from itertools import combinations


def solve_viable(grid) -> int:
    counter = 0
    for coord_pairs in list(combinations(grid.keys(), 2)):
        counter += 1 if is_viable(coord_pairs, grid) else 0
        counter += 1 if is_viable((coord_pairs[1], coord_pairs[0]), grid) else 0
    return counter


def solve_traverse(grid) -> int:
    end = max(x for x, _ in grid.keys()), 0
    return -1


#  0     1      2      3
# Size  Used  Avail  Use%


def is_viable(coord_pairs, grid):
    a_coords, a_props = coord_pairs[0], grid[coord_pairs[0]]
    b_coords, b_props = coord_pairs[1], grid[coord_pairs[1]]
    if a_props[1] == 0:
        return False
    if a_coords == b_coords:
        return False
    if a_props[1] > b_props[2]:
        return False
    return True
