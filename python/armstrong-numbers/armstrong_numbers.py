def is_armstrong_number(number):
    number_string = str(number)
    number_list = list(number_string)
    total = 0
    for digit in number_list:
        total+= pow(int(digit), len(number_list))
    return total == number
