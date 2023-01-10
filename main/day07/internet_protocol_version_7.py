def solve(ips, tls) -> int:
    count = 0
    for ip in ips:
        inners = []
        outers = []
        s = []
        for c in ip:
            if c == "[":
                outers.append("".join(s))
                s.clear()
            elif c == "]":
                inners.append("".join(s))
                s.clear()
            else:
                s.append(c)
        if len(s) > 0:
            outers.append("".join(s))
        if tls:
            if any(has_reverse_pair(outer) for outer in outers) and not any(
                    has_reverse_pair(inner) for inner in inners):
                count += 1
        else:
            abas = flatten([get_triples(outer) for outer in outers])
            babs = flatten([get_triples(inner) for inner in inners])
            babs_transformed = [f"{bab[1]}{bab[0]}{bab[1]}" for bab in babs]
            if len(set(abas).intersection(set(babs_transformed))) > 0:
                count += 1
    return count


def has_reverse_pair(s):
    return any(c for c in zip(s, s[1:], s[2:], s[3:]) if c[0] == c[3] and c[1] == c[2] and c[0] != c[1])


def get_triples(s):
    return ["".join(c) for c in zip(s, s[1:], s[2:]) if c[0] == c[2] and c[0] != c[1]]


def flatten(ls):
    return [item for sublist in ls for item in sublist]
