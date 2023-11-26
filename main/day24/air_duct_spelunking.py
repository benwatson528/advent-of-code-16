import sys

sys.setrecursionlimit(150000)


def solve_p1(walkable, poi) -> int:
    shortest_paths = find_shortest_paths(poi, walkable)
    return move_between_nodes(0, shortest_paths, set(), 0, len(poi))


def solve_p2(walkable, poi) -> int:
    shortest_paths = find_shortest_paths(poi, walkable)
    return move_between_nodes_return(0, shortest_paths, set(), 0, len(poi))


def find_shortest_paths(poi, walkable):
    shortest_paths = {}
    for start_coord, start_value in poi.items():
        for dest_coord, dest_value in poi.items():
            if start_value != dest_value and (start_value, dest_value) not in shortest_paths.keys() and (
                    dest_value, start_value) not in shortest_paths.keys():
                shortest_paths[(start_value, dest_value)] = move_one_step(start_coord, dest_coord, walkable)
    return shortest_paths


def move_one_step(start, dest, walkable):
    to_visit = [(start, [])]
    visited = set(start)

    while to_visit:
        current, path = to_visit.pop(0)
        if current == dest:
            return len(path)
        path.append(current)

        for next_step in ((current[0], current[1] + 1),
                          (current[0] + 1, current[1]),
                          (current[0] - 1, current[1]),
                          (current[0], current[1] - 1)):
            if next_step in walkable and next_step not in visited:
                visited.add(next_step)
                to_visit.append((next_step, path.copy()))


def move_between_nodes(current, paths, visited, distance, num_pois):
    if len(visited) == num_pois - 1:
        return distance
    return min(
        move_between_nodes(possible[0], paths, visited | {current}, distance + possible[1], num_pois) for possible in
        find_possible_moves(current, paths, visited))


def move_between_nodes_return(current, paths, visited, distance, num_pois):
    if len(visited) == num_pois - 1:
        return distance + paths.get((current, 0), paths.get((0, current)))
    return min(
        move_between_nodes_return(possible[0], paths, visited | {current}, distance + possible[1], num_pois) for
        possible in find_possible_moves(current, paths, visited))


def find_possible_moves(current, paths, visited):
    possibles = set()  # destination, distance to get there
    for path_points, path_distance in paths.items():
        if current == path_points[0] and path_points[1] not in visited:
            possibles.add((path_points[1], path_distance))
        elif current == path_points[1] and path_points[0] not in visited:
            possibles.add((path_points[0], path_distance))
    return possibles
