import re


def solve(instructions, width, height) -> int:
    # yuck
    turned_on = set()
    for instruction in instructions:
        new = set()
        regex = re.findall(r"\d+", instruction)
        pixels = int(regex[0]), int(regex[1])
        if instruction.startswith("rect"):
            for i in range(pixels[1]):
                for j in range(pixels[0]):
                    turned_on.add((i, j))
        elif instruction.startswith("rotate row"):
            for on in turned_on.copy():
                if on[0] == pixels[0]:
                    turned_on.remove(on)
                    new.add((on[0], (on[1] + pixels[1]) % width))
        elif instruction.startswith("rotate column"):
            for on in turned_on.copy():
                if on[1] == pixels[0]:
                    turned_on.remove(on)
                    new.add(((on[0] + pixels[1]) % height, on[1]))
        turned_on.update(new)
    return len(turned_on)
