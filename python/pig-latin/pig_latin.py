def translate(text):
    vowel_sound = ("a", "e", "i", "o", "u")
    text = text.split()
    translation = []
    for word in text:
        if word[0] in vowel_sound or word[:2] in ("xr", "yt"):
            word = word
        elif word.startswith("qu"):
            word = word[2:] + "qu"
        else: 
            if word[1] in ("h", "c", "t"):
                if word[2] in ("h", "r"):
                    word = word[3:] + word[:3]
                else:
                    word = word[2:] + word[:2]
            elif word[1:3] == "qu":
                word = word[3:] + word[:3]
            else:
                word = word[1:] + word[0]
        translation.append(word + "ay")

    return " ".join(translation)
