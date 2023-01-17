import re
from collections import defaultdict


def solve(instructions, vals_to_check=None) -> int:
    bots = defaultdict(list)
    output = {}
    for instruction in [instruction for instruction in instructions if instruction.startswith("value")]:
        nums = [int(x) for x in re.findall(r"\d+", instruction)]
        bots[nums[1]].append(nums[0])
    if bot_id := check_vals(bots, vals_to_check):
        return bot_id
    while True:
        new_instructions = []
        for instruction in [instruction for instruction in instructions if instruction.startswith("bot")]:
            nums = [int(x) for x in re.findall(r"\d+", instruction)]
            vals = bots[nums[0]]
            if len(vals) != 2:
                new_instructions.append(instruction)
                continue
            high, low = max(vals), min(vals)
            bots[nums[0]] = []
            if "low to output" in instruction:
                output[nums[1]] = low
            else:
                bots[nums[1]].append(low)
            if "high to output" in instruction:
                output[nums[2]] = high
            else:
                bots[nums[2]].append(high)
            if bot_id := check_vals(bots, vals_to_check):
                return bot_id
            if not vals_to_check and 0 in output and 1 in output and 2 in output:
                return output[0] * output[1] * output[2]
        instructions = new_instructions.copy()


def check_vals(bots, vals_to_check):
    if vals_to_check:
        for bot_id, bot_vals in bots.items():
            if vals_to_check[0] in bot_vals and vals_to_check[1] in bot_vals:
                return bot_id
    return None
