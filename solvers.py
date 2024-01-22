def NewtonsMethod(f, fdash, x0, tolerance):
    x = x0

    while abs(f(x)) > tolerance:
        x = x - (f(x))/(fdash(x))

    return x 