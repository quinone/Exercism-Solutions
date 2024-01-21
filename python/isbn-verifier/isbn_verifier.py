def is_valid(isbn):
    
    isbn = isbn.replace('-', '')
    new_isbn = isbn.lower()
    if len(new_isbn)!=10:
        return False
    if new_isbn.isalpha() and not (new_isbn[-1]=='x'):
        return False
    total = 0
    d = 10
    for index in range(9):
        value = new_isbn[index]
        if value.isalpha():
            return False
        number = int(value)
        total += d * number
        d-=1
    if new_isbn[-1] == 'x':
        total += 10
    elif new_isbn[-1].isalpha():
        return False
    else:
        total += int(new_isbn[-1])
    return total % 11 == 0
        