import hashlib

DIRECTIONS = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
HASH_ORDER = "UDLR"
OPEN_DOORS = "bcdef"


def solve_shortest(passcode) -> str:
    shortest_path_len = 9999
    shortest_path = None
    to_visit = [((0, 0), [])]

    while to_visit:
        current, visited = to_visit.pop()
        if len(visited) >= shortest_path_len:
            continue
        if current == (3, 3):
            if len(visited) < shortest_path_len:
                shortest_path_len = len(visited)
                shortest_path = visited
            continue
        elif current[0] < 0 or current[0] > 3 or current[1] < 0 or current[1] > 3:
            continue

        hsh = generate_hash(passcode, visited)
        for direction, coords in DIRECTIONS.items():
            if hsh[HASH_ORDER.index(direction)] in OPEN_DOORS:
                to_visit.append(((current[0] + coords[0], current[1] + coords[1]), visited + [direction]))
    return "".join(shortest_path)


def solve_longest(passcode) -> int:
    longest_path = 0
    to_visit = [((0, 0), [])]

    while to_visit:
        current, visited = to_visit.pop()
        if current == (3, 3):
            longest_path = max(longest_path, len(visited))
            continue
        elif current[0] < 0 or current[0] > 3 or current[1] < 0 or current[1] > 3:
            continue

        hsh = generate_hash(passcode, visited)
        for direction, coords in DIRECTIONS.items():
            if hsh[HASH_ORDER.index(direction)] in OPEN_DOORS:
                to_visit.append(((current[0] + coords[0], current[1] + coords[1]), visited + [direction]))
    return longest_path


def generate_hash(passcode, visited):
    return hashlib.md5(f'{passcode}{"".join(visited)}'.encode()).hexdigest()[:4]
