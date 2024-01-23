def is_valid(isbn):
    isbn = isbn.replace('-', '')
    isbn = [*isbn]
    if len(isbn)!=10:
        return False
    
    if isbn[-1] == 'X':
        isbn[-1] = '10'

    if any(number.isalpha() for number in isbn):
        return False
    
    isbn = [int(digit) for digit in isbn]
    total = sum(map(lambda digit, index: digit * index, isbn, range(10, 0, -1)))

    return total % 11 == 0
