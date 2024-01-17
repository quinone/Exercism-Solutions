def is_pangram(sentence):
    letter_list = [letter.lower() for letter in sentence if letter.isalpha()]
    return len(set(letter_list)) == 26