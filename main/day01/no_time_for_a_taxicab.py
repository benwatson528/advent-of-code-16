RIGHT_MOVES = {"N": "E", "E": "S", "S": "W", "W": "N"}
LEFT_MOVES = {v: k for k, v in RIGHT_MOVES.items()}
WALK = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def solve(movements, find_visited) -> int:
    current = (0, 0)
    visited = {current}
    facing = "N"
    for movement in movements:
        facing = RIGHT_MOVES[facing] if movement[0] == "R" else LEFT_MOVES[facing]
        for _ in range(int(''.join(movement[1:]))):
            current = current[0] + WALK[facing][0], current[1] + WALK[facing][1]
            if find_visited:
                if current in visited:
                    return abs(current[0]) + abs(current[1])
                else:
                    visited.add(current)
    return abs(current[0]) + abs(current[1])
