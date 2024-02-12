OPERATION = {"minus", "plus", "multiplied", "divided"}


def answer(question):
    parse = question.replace("by", " ").replace("?", "").split()
    if len(parse) < 3:
        raise ValueError("syntax error")
    if parse[2].isalpha():
        if parse[2] in OPERATION:
            raise ValueError("syntax error")
        raise ValueError("unknown operation")
    first_operand = int(parse[2])
    if len(parse) == 3:
        return first_operand

    if parse[3].isalpha() and parse[3] not in OPERATION:
        raise ValueError("unknown operation")
    if len(parse) not in (3, 5, 7):
        raise ValueError("syntax error")
    if parse[4].isalpha():
        raise ValueError("syntax error")
    second_operand = int(parse[4])
    result = calculate(first_operand, second_operand, parse[3])

    if len(parse) == 5:
        return result
    if parse[6].isalpha():
        raise ValueError("syntax error")
    third_operand = int(parse[6])
    return calculate(result, third_operand, parse[5])


def calculate(first_operand, second_operand, operation):
    if operation == "minus":
        return first_operand - second_operand
    if operation == "plus":
        return first_operand + second_operand
    if operation == "multiplied":
        return first_operand * second_operand
    if operation == "divided":
        return first_operand / second_operand
    raise ValueError("unknown operation")
