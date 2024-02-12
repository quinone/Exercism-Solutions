def abbreviate(words):
    words = words.replace('_', '')
    words = words.replace('-', ' ')
    word_list = words.split(' ')
    result = ''
    for word in word_list:
        if not word:
            continue
        upper_letter = word[0].upper()
        result+=upper_letter
    return result

