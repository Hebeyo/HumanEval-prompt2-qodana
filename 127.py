def intersection(interval1, interval2):
    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    if length > 0:
        if length == 1:
            return "NO"
        for i in range(2, length):
            if length % i == 0:
                return "NO"
        return "YES"
    return "NO"
