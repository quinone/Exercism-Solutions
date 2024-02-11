open = {"(", "{", "["}
close = {")","}", "]"}
BRACKET = {
    "(":")",
    "[":"]",
    "{":"}"
}

def is_paired(input_string):
    opened_brackets = []
    for char in input_string:
        if char in BRACKET.keys():
            opened_brackets.append(char)
        if char in BRACKET.values():
            if BRACKET[opened_brackets[-1]] != char:
                return False
            opened_brackets.pop()
    return True
