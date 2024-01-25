def translate(text):
    text = text.split()
    for word in text:
        if word[0] in ('a', 'e','i','o','u', 'x', 'y'):
            word+='ay'

    
    return ' '.join(text)
