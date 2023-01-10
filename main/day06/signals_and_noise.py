from collections import Counter, defaultdict


def solve(messages, most_common=True) -> str:
    counters = defaultdict(list)
    for message in messages:
        for i, c in enumerate(message):
            counters[i].append(c)
    selector = 0 if most_common else -1
    return "".join("".join(Counter(position).most_common()[selector][0]) for position in counters.values())
