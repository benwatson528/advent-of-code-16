from itertools import combinations


def solve(components) -> int:
    return move(components, 1, [])


# We keep recursing downwards, if we hit an endstate then we return how many steps it took
# at each node we return the minimum steps from that node
# finally we get the overall minimum to get the end state

# If we've found an end state, return the number of steps it took
# Otherwise see what can be in the lift, and for each of them move up and down
# Empty the lift and make sure it's a valid state

def move(components, lift_position, visited):
    visited.append((lift_position, frozenset(components)))
    if all(x[0] == 4 for x in components):
        if len(visited) <= 50:
            print(f"FOUND SOLUTION in steps = {len(visited)}")
            print(f"Visited = {visited}")
        return len(visited)

    min_moves = None
    # print(f"\nVisiting valid state {components} with lift on floor {lift_position}")
    for elevator_content in [lift_content for lift_content in get_lift_combinations(components, lift_position) if
                             can_be_in_lift(lift_content)]:
        for new_lift_position in [lift_position + 1, lift_position - 1]:
            # # don't move pairs down
            # if new_lift_position < lift_position \
            #         and elevator_content[1] is not None and elevator_content[0][1][:-1] == elevator_content[1][1][:-1]:
            #     continue
            if new_lift_position == 5 or new_lift_position == 0:
                continue
            new_components = move_components(components.copy(), elevator_content, new_lift_position)
            if not is_valid_placement(new_components):
                continue
            if (new_lift_position, frozenset(new_components)) in visited:
                continue
            if (num_moves := move(new_components, new_lift_position, visited.copy())) is not None:
                min_moves = num_moves if not min_moves else min(min_moves, num_moves)
    return min_moves


def move_components(components, elevator_content, new_lift_position):
    for e in elevator_content:
        if e is not None:
            components.remove(e)
            components.add((new_lift_position, e[1]))
    return components


def get_lift_combinations(components, lift_position):
    current_floor_components = [x for x in components if x[0] == lift_position]
    current_floor_singles = [(x, None) for x in current_floor_components]
    return current_floor_singles + list(combinations(current_floor_components, 2))


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


def can_be_in_lift(contents):
    if contents[0] is None or contents[1] is None:
        return True
    else:
        left_comp, right_comp = contents[0][1], contents[1][1]
        return left_comp[:-1] == right_comp[:-1] or (left_comp[-1] == right_comp[-1])
