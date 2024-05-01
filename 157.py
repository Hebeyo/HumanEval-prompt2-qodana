def right_angle_triangle(a, b, c):
    if a*a == b*b + c*c:
        return True
    elif b*b == a*a + c*c:
        return True
    elif c*c == a*a + b*b:
        return True
    else:
        return False
