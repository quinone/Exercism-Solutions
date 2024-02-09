def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")
    primes = []
    position = 1
    for _ in range(number):
        while True:
            position += 1
            if isPrime(position, primes):
                primes.append(position)
                break

    return primes[-1]


def isPrime(number, primes):
    if number == 1:
        return False
    if primes:
        for n in primes:
            if number % n == 0:
                return False
        for n in range(primes[-1], number):
            if number % n == 0:
                return False
    return True
