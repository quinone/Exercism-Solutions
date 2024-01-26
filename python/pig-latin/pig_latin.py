def translate(text):
    vowel_sound = ('a', 'e','i','o','u')
    text = text.split()
    translation=[]
    for word in text:
        if word[0] in vowel_sound or word[:2] in ('xr', 'yt'):
            word+='ay'
        elif word.startswith('qu'):
            word= word[2:] + 'quay'
        elif word[0] in ('w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k',
                              'l', 'z', 'c', 'v', 'b', 'n', 'm', 'x', 'y'):
            if word[1] in ('h', 'c','t'):
                if word[2] in ('h', 'r'):
                    word = word[3:]+word[:3]+'ay'
                else:
                    word = word[2:]+word[:2]+ 'ay'
            elif word[1:3] == 'qu':
                word = word[3:]+word[:3]+'ay'
            
            else:
                word = word[1:] + word[0] + 'ay'    
        else:
            word= word[1:] + word[0] + 'ay'
        translation.append(word)
    
    return ' '.join(translation)