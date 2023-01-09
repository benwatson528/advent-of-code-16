MOVEMENTS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def solve(instructions, keypad) -> str:
    current = list(keypad.keys())[list(keypad.values()).index("5")]
    key_code = []
    for line in instructions:
        for instruction in line:
            prev_current = current
            current = current[0] + MOVEMENTS[instruction][0], current[1] + MOVEMENTS[instruction][1]
            if current not in keypad:
                current = prev_current
        key_code.append(keypad[current])
    return "".join(key_code)
