def solve(a, length) -> str:
    while len(a) <= length:
        b = ''.join(reversed(a))
        b = ''.join('1' if c == '0' else '0' for c in b)
        a = a + '0' + ''.join(b)

    a = a[:length]

    while len(a) % 2 == 0:
        a = ''.join('1' if pair[0] == pair[1] else '0' for pair in pairs(a))
    return a


def pairs(a):
    for i in range(0, len(a), 2):
        yield a[i:i + 2]
