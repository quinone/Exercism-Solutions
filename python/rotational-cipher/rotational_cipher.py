def rotate(text, key):
    cipher_text = ''
    for letter in text:
        if letter.isalpha():
            letter_number = ord(letter)
            if 65 <= letter_number <= 90:
                letter_key = (letter_number - 65 + key) % 26
                cipher_letter = chr(letter_key + 65)
            if 97 <= letter_number <= 122:
                letter_key = (letter_number - 97 + key) % 26
                cipher_letter = chr(letter_key + 97)
            cipher_text = cipher_text + cipher_letter
        else:
            cipher_text = cipher_text + letter
    return cipher_text