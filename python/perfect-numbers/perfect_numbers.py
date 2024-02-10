def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    result = sum_factors(number)
    if result == number:
        return "perfect"
    if result > number:
        return "abundant"
    return "deficient"
    


def sum_factors(number):
    return sum(n for n in range(1, number) if number % n == 0)