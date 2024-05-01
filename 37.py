def sort_even(l: list):
    evens = [x for i, x in enumerate(l) if i % 2 == 0]
    odds = [x for i, x in enumerate(l) if i % 2 == 1]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans
