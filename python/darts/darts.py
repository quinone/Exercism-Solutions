def score(x, y):
    squared = x**2 + y**2
    if squared <= 1:
        return 10
    if squared <= 5**2:
        return 5
    if squared <= 10**2:
        return 1
    return 0
