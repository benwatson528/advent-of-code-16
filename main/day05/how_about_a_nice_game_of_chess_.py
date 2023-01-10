import hashlib


def solve_p1(door_id) -> str:
    password = []
    last_val = -1
    for _ in range(8):
        last_val, hsh = find_hash_prefix(door_id, last_val + 1)
        password.append(hsh[5])
    return "".join(password)


def solve_p2(door_id) -> str:
    password = [""] * 8
    last_val = -1
    while True:
        last_val, hsh = find_hash_prefix(door_id, last_val + 1)
        position, val = hsh[5], hsh[6]
        if position.isnumeric() and int(position) < 8 and not password[int(position)]:
            password[int(position)] = val
        if len("".join(password)) == 8:
            return "".join(password)


def find_hash_prefix(door_id, i):
    while True:
        if (hsh := hashlib.md5(f"{door_id}{i}".encode()).hexdigest()).startswith("00000"):
            return i, hsh
        i += 1
