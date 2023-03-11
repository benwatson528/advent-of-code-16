def solve(start_row, num_rows) -> int:
    row_len = len(start_row)
    above = start_row
    total_safe = start_row.count(".")
    for _ in range(num_rows - 1):
        above = process_row(above, row_len)
        total_safe += above.count(".")
    return total_safe


def process_row(above, row_len):
    current = []
    for i in range(row_len):
        neighbours = process_tile(above, i, row_len)
        if neighbours[0] and neighbours[1] and not neighbours[2]:
            current.append("^")
        elif not neighbours[0] and neighbours[1] and neighbours[2]:
            current.append("^")
        elif neighbours[0] and not neighbours[1] and not neighbours[2]:
            current.append("^")
        elif not neighbours[0] and not neighbours[1] and neighbours[2]:
            current.append("^")
        else:
            current.append(".")
    return "".join(current)


def process_tile(above, i, row_len):
    neighbours = []
    for j in range(i - 1, i + 2):
        if j < 0:
            neighbours.append(False)
        elif j == row_len:
            neighbours.append(False)
        else:
            neighbours.append(above[j] == "^")
    return neighbours
