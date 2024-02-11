BRACKET = {"(": ")", "[": "]", "{": "}"}


def is_paired(input_string):
    list_unclosed_bracket = []
    for character in input_string:
        if character in BRACKET.keys():
            list_unclosed_bracket.append(character)
        if character in BRACKET.values():
            if not list_unclosed_bracket or BRACKET[list_unclosed_bracket[-1]] != character:
                return False
            list_unclosed_bracket.pop()

    return not list_unclosed_bracket
