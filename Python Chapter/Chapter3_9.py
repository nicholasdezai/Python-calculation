def f(x):
    if x < 0:
        return 0
    elif 0 <= x < 5:
        return x
    elif 5 <= x < 10:
        return 3 * x - 5
    elif 10 <= x < 20:
        return 0.5 * x - 2
    else:
        return 0

print(f(1))