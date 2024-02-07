def factors(value):
    prime = []
    if value == 1:
        return prime
    factor = 2
    while value / factor != 1:
        if value % factor == 0:
            prime.append(factor)
            value = value / factor
        if value % factor != 0:
            factor += 1

    prime.append(factor)
    return prime
