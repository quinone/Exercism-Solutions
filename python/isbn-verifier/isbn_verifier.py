def is_valid(isbn):
    isbn = list(isbn.replace("-", ""))
    if len(isbn) != 10:
        return False

    if isbn[-1] == "X":
        isbn[-1] = "10"

    if any(number.isalpha() for number in isbn):
        return False

    return sum(int(digit) * i for digit, i in zip(isbn, range(10, 0, -1))) % 11 == 0

    #return (
    #   sum(map(lambda digit, index: int(digit) * index, isbn, range(10, 0, -1))) % 11
    #   == 0
    #)
