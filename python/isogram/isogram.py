def is_isogram(string):
    letter_list = [letter.lower() for letter in string if letter.isalpha()]
    return len(letter_list) == len(set(letter_list))

