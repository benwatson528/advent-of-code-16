from collections import deque
from itertools import combinations

LIFT_MOVEMENTS = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}


def solve(components) -> int:
    return move(components)


def move(components):
    global_visited = {}
    to_visit = deque()
    to_visit.append((frozenset(components), 1, 0))
    while to_visit:
        components, lift_level, num_steps = to_visit.popleft()
        if (components, lift_level) in global_visited and num_steps >= global_visited[(components, lift_level)]:
            continue
        global_visited[(components, lift_level)] = num_steps
        if all(level == 4 for level, component_name in components):
            return num_steps

        for lift_components in get_lift_combinations(components, lift_level):
            if not can_be_in_lift(lift_components):
                continue
            for next_level in LIFT_MOVEMENTS[lift_level]:
                new_components = move_components(components, lift_components, next_level)
                if is_valid_placement(new_components) and (new_components, next_level) not in global_visited:
                    to_visit.append((new_components, next_level, num_steps + 1))


def get_lift_combinations(components, lift_level):
    current_floor_components = [(l, n) for l, n in components if l == lift_level]
    current_floor_singles = [(x, None) for x in current_floor_components]
    return current_floor_singles + list(combinations(current_floor_components, 2))


def move_components(components, lift_components, new_lift_position):
    new_components = set(components)
    for e in lift_components:
        if e is not None:
            new_components.discard(e)
            new_components.add((new_lift_position, e[1]))
    return frozenset(new_components)


def is_valid_placement(components):
    for floor in (1, 2, 3, 4):
        generators = set()
        microchips = set()
        for obj in [x[1] for x in components if x[0] == floor]:
            if obj[-1] == "G":
                generators.add(obj[:-1])
            else:
                microchips.add(obj[:-1])
        for chip in microchips:
            if chip not in generators and len(generators) > 0:
                return False
    return True


def can_be_in_lift(lift_components):
    if not lift_components[1]:
        return True
    else:
        left_comp, right_comp = lift_components
        return left_comp[:-1] == right_comp[:-1] or (left_comp[-1] == right_comp[-1])
