from collections import Counter
from operator import itemgetter


def solve_validate(rooms) -> int:
    real_rooms = []
    for room in rooms:
        name, sector_id, checksum = room
        counter = [(k, v) for k, v in Counter(name).items()]
        sorted_counter = sorted(sorted(counter, key=itemgetter(0)), key=itemgetter(1), reverse=True)
        if is_valid_checksum(checksum, sorted_counter):
            real_rooms.append(int(sector_id))
    return sum(real_rooms)


def solve_decrypt(rooms) -> int:
    for room in rooms:
        name = room[0]
        sector_id = int(room[1])
        decyphered = []
        for c in name:
            decyphered.append(chr((((ord(c) - 97) + sector_id) % 26) + 97))
        if "northpole" in "".join(decyphered):
            return sector_id


def is_valid_checksum(checksum, counter):
    return not any(counter[i][0] != c for i, c in enumerate(checksum))
