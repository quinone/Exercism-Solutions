def rotate(text, key):
    cipher_text = ""
    for letter in text:
        letter_number = ord(letter)
        if 65 <= letter_number <= 90:
            letter_number = ((letter_number - 65 + key) % 26) + 65
        if 97 <= letter_number <= 122:
            letter_number = ((letter_number - 97 + key) % 26) + 97
        cipher_text += chr(letter_number)
    return cipher_text
