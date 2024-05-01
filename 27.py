def flip_case(string: str) -> str:
    new_string = ''
    for c in string:
        if c.isupper():
            new_string += c.lower()
        else:
            new_string += c.upper()
    return new_string
