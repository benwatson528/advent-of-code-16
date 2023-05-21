import re


def solve(commands, password) -> str:
    for cmd in commands:
        if cmd.startswith("swap position"):
            password = swap(cmd, "position", password)
        elif cmd.startswith("swap letter"):
            password = swap(cmd, "letter", password)
        elif cmd.startswith("rotate left"):
            password = rotate(cmd, "left", password)
        elif cmd.startswith("rotate right"):
            password = rotate(cmd, "right", password)
        elif cmd.startswith("rotate based"):
            password = rotate(cmd, "based", password)
        elif cmd.startswith("reverse"):
            password = reverse(cmd, password)
        elif cmd.startswith("move"):
            password = move(cmd, password)
    return password


def swap(cmd, op_type, password):
    match op_type:
        case "position":
            positions = re.findall(r'swap position (.) with position (.)', cmd)[0]
            i1, i2 = int(positions[0]), int(positions[1])
        case "letter":
            positions = re.findall(r'swap letter (.) with letter (.)', cmd)[0]
            i1, i2 = password.index(positions[0]), password.index(positions[1])

    password_list = list(password)
    password_list[i1], password_list[i2] = password_list[i2], password_list[i1]
    return "".join(password_list)


def rotate(cmd, op_type, password):
    match op_type:
        case "left":
            n = int(re.findall(r'rotate left (.) step|steps', cmd)[0][0])
        case "right":
            n = -int(re.findall(r'rotate right (.) step|steps', cmd)[0][0])
        case "based":
            letter = re.findall(r'rotate based on position of letter (.)', cmd)[0][0]
            i = password.index(letter)
            n = -(i + 1) if i < 4 else -(i + 2)

    n %= len(password)
    rotated = password[n:] + password[:n]
    return rotated


def reverse(cmd, password):
    positions = re.findall(r'reverse positions (.) through (.)', cmd)[0]
    i1, i2 = int(positions[0]), int(positions[1])
    return password[:i1] + "".join(reversed(password[i1:i2 + 1])) + password[i2 + 1:]


def move(cmd, password, reversed=False):
    positions = re.findall(r'move position (.) to position (.)', cmd)[0]
    i1, i2 = int(positions[0]), int(positions[1])
    if reversed:
        i2, i1 = i1, i2
    to_move = password[i1]
    password = password[:i1] + password[i1 + 1:]
    return password[:i2] + to_move + password[i2:]
