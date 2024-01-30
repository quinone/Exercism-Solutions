vowel_sound = {"a", "e", "i", "o", "u"}


def translate(text):
    return " ".join([trans_pig(word) for word in text.split()])


def trans_pig(word):
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
    return word + "ay"
