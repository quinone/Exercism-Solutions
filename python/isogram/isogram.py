def is_isogram(string):
    letter_list = [letter.lower() for letter in string if letter.isalpha()]
        #if letter.lower() in letter_list:
        #    return False
        #if letter.isalpha():
        #    letter_list.add(letter.lower())
    return len(letter_list) == len(set(letter_list))

