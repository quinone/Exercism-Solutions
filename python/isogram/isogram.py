def is_isogram(string):
    letter_list = set()
    for letter in string:
        if letter.lower() in letter_list:
            return False
        if letter.isalpha():
            letter_list.add(letter.lower())
    return True

