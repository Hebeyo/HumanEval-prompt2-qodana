def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for k in range(2, n - 1):
            if n % k == 0:
                return False
        return True
    for i in range(2, 101):
        if not is_prime(i): continue
        for j in range(2, 101):
            if not is_prime(j): continue
            for k in range(2, 101):
                if not is_prime(k): continue
                if i * j * k == a:
                    return True
    return False
