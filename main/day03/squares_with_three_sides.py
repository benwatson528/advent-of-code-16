def solve_rows(triangles) -> int:
    return sum(is_valid_triangle(t) for t in triangles)


def solve_columns(triangles) -> int:
    valid = 0
    for row in range(0, len(triangles), 3):
        for col in range(3):
            t = triangles[row][col], triangles[row + 1][col], triangles[row + 2][col]
            valid += 1 if is_valid_triangle(t) else 0
    return valid


def is_valid_triangle(t):
    return t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]
