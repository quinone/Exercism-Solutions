def square_root(number):
    result = 1
    while number != result*result:
        result+=1
    return result
