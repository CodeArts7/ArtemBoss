def feast(beast, dish):
    b = list(beast)
    c = list(dish)

    if b[0] == c[0] and b[-1] == c[-1]:
        return True
    else:
        return False


feast("brown bear", "bear claw")
