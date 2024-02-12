def answer(question):
    parse = question.split()
    first_operand = int(parse[2])
    second_operand = int(parse[-1])
    if parse[3] == 'minus':
        return first_operand - second_operand
    if parse[3] == 'plus':
        return first_operand + second_operand
    if parse[3] == 'multiplied':
        return first_operand * second_operand
    if parse[3] == 'divided':
        return first_operand / second_operand