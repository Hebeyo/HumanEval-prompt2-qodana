def triples_sum_to_zero(l: list):
    l = sorted(l)
    n = len(l)
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            s = l[i] + l[left] + l[right]
            if s == 0:
                return True
            elif s < 0:
                left += 1
            else:
                right -= 1
    return False
