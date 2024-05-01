def cycpattern_check(a , b):
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        return a == b
    for i in range(len(b)):
        if b in a:
            return True
        b = b[-1] + b[:-1]
    return False
