MAX_IP = 4294967295


def solve_lowest(blocked_ranges) -> int:
    lowest = MAX_IP
    for c in blocked_ranges:
        for possible in c[0] - 1, c[1] + 1:
            if possible < 0:
                continue
            is_blocked = False
            for d in blocked_ranges:
                if possible in range(d[0], d[1] + 1):
                    is_blocked = True
            if not is_blocked:
                lowest = min(lowest, possible)
    return lowest


def solve_allowed(blocked_ranges) -> int:
    condensed = sorted(combine(blocked_ranges), key=lambda r: r.start)
    valid_ips = 0
    for c in zip(condensed, condensed[1:]):
        if c[1].stop > MAX_IP:
            break
        valid_ips += c[1].start - c[0].stop - 1
    return valid_ips


def combine(blocked_ranges):
    condensed = blocked_ranges.copy()
    for r in blocked_ranges:
        updated_condensed = []
        local_min = MAX_IP
        local_max = 0
        have_condensed = False
        for c in condensed:
            if r == c:
                continue
            if r.start in c or r.stop - 1 in c:
                local_min = min(local_min, r.start, c.start)
                local_max = max(local_max, r.stop, c.stop)
                have_condensed = True
            else:
                updated_condensed.append(c)
        if have_condensed:
            updated_condensed.append(range(local_min, local_max))
        else:
            updated_condensed.append(r)
        condensed = updated_condensed.copy()
    return condensed
