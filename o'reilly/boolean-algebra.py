OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == "conjunction":
        if x == y == 1:
            return 1
        else:
            return 0
    elif operation == "disjunction":
        if x == y == 0:
            return 0
        else:
            return 1
    elif operation == "implication":
        if (x == y == 1) or (x == 0 and y == 1) or (x == y == 0):
            return 1
        else:
            return 0
    elif operation == "exclusive":
        if x != y:
            return 1
        else:
            return 0
    elif operation == "equivalence":
        if (x == y == 1) or (x == y == 0):
            return 1
        else:
            return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
