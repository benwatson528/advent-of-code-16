def solve(cmds, a_val=0) -> int:
    register = {"a": a_val, "b": 0, "c": 0, "d": 0}
    i = 0
    toggles = set()

    while i < len(cmds):
        split_cmd = cmds[i].split(" ")
        instruction = split_cmd[0]
        args = split_cmd[1:]
        if register['d'] < 100:
            print()
        if i in toggles:
            if len(args) == 1:
                instruction = "dec" if instruction == "inc" else "inc"
            else:
                instruction = "cpy" if instruction == "jnz" else "jnz"
        try:
            match instruction:
                case "cpy":
                    register[args[1]] = get_arg(args[0], register)
                case "inc":
                    register[args[0]] += 1
                case "dec":
                    register[args[0]] -= 1
                case "jnz":
                    if get_arg(args[0], register) != 0:
                        i += get_arg(args[1], register) - 1
                case "tgl":
                    toggles.add(i + get_arg(args[0], register))
        except Exception:
            pass
        i += 1
    return register["a"]


def get_arg(x, register):
    try:
        return int(x)
    except ValueError:
        return register[x]
