def is_armstrong_number(number):
    number_list = list(str(number))
    return number == sum([pow(int(digit), len(number_list)) for digit in number_list])
