def is_pangram(sentence):
    alphabet = set()
    for letter in sentence:
        if letter.isalpha():
            alphabet.add(letter.lower())    
    return len(alphabet) == 26
