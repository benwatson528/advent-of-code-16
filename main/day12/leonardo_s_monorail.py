def solve(cmds, change_c = False) -> int:
    register = {"a": 0, "b": 0, "c": 0, "d": 0}
    if change_c:
        register["c"] = 1
    i = 0
    while i < len(cmds):
        split_cmd = cmds[i].split(" ")
        match split_cmd[0]:
            case "cpy":
                register[split_cmd[2]] = int(split_cmd[1]) if split_cmd[1].isnumeric() else register[split_cmd[1]]
            case "inc":
                register[split_cmd[1]] += 1
            case "dec":
                register[split_cmd[1]] -= 1
            case "jnz":
                if split_cmd[1].isnumeric():
                    if split_cmd[1] != '0':
                        i += int(split_cmd[2]) - 1
                elif register[split_cmd[1]] != 0:
                    i += int(split_cmd[2]) - 1
        i += 1
    return register["a"]
