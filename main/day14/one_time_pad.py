import hashlib


def solve(salt, key_to_find, stretch_factor=0) -> int:
    hashes = {}
    keys = []
    i = 0
    while len(keys) < key_to_find:
        hsh = create_hash(salt, i, stretch_factor, hashes)
        if repeated := contains_in_row(hsh, 3):
            if find_inner(salt, repeated, i, stretch_factor, hashes):
                keys.append(i)
        i += 1

    return keys[-1]


def contains_in_row(s, n, repeat=None):
    last = s[0]
    counter = 1
    for c in s[1:]:
        if c == last:
            counter += 1
            if counter == n:
                if repeat:
                    if c == repeat:
                        return c
                else:
                    return c
        else:
            counter = 1
            last = c
    return None


def find_inner(salt, repeated, starting_idx, stretch_factor, hashes):
    for i in range(starting_idx + 1, starting_idx + 1001):
        if contains_in_row(create_hash(salt, i, stretch_factor, hashes), 5, repeated):
            return True
    return False


def create_hash(salt, i, stretch_factor, hashes):
    if i in hashes:
        return hashes[i]
    hsh = hashlib.md5(f"{salt}{i}".encode()).hexdigest()
    for _ in range(stretch_factor):
        hsh = hashlib.md5(hsh.encode()).hexdigest()
    hashes[i] = hsh
    return hsh
