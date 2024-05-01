def common(l1: list, l2: list):
    l1 = set(l1)
    l2 = set(l2)
    return sorted(list(l1.intersection(l2)))
