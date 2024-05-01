def correct_bracketing(brackets: str):
    # if brackets.count("<") != brackets.count(">"):
    #     return False
    # if brackets.find(">") < brackets.find("<"):
    #     return False
    # if brackets[0] == ">":
    #     return False
    # if brackets[-1] == "<":
    #     return False
    # return True
    depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0
