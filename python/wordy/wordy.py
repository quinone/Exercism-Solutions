OPERATION = {"minus", "plus", "multiplied", "divided"}


def answer(question):
    parse = instruction_parse(question)
    first_operand = int(parse[0])
    if len(parse) == 1:
        return first_operand

    second_operand = int(parse[2])
    result = calculate(first_operand, second_operand, parse[1])

    if len(parse) == 3:
        return result

    third_operand = int(parse[4])
    return calculate(result, third_operand, parse[3])


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


def instruction_parse(sentence):
    instruction_list = sentence.replace("by", " ").replace("?", "").split()
    instruction_list = instruction_list[2:]

    for index, instruction in enumerate(instruction_list):
        if instruction.isalpha() and instruction not in OPERATION:
            raise ValueError("unknown operation")
        if (index % 2 == 0 and instruction.isalpha()) or (
            index % 2 != 0 and instruction.isnumeric()
        ):
            raise ValueError("syntax error")

    if not instruction_list or instruction_list[-1].isalpha():
        raise ValueError("syntax error")
    return instruction_list
