def is_valid(isbn):
    isbn = isbn.replace('-', '')
    new_isbn = isbn.lower()
    if len(new_isbn)!=10:
        return False

    total = 0
    d = 10
    for index in range(10):
        value = new_isbn[index]
        if value.isalpha():
            if value == 'x' and index == 9:
                value = 10
            else:
                return False    
        number = int(value)
        total += d * number
        d-=1
    return total % 11 == 0
