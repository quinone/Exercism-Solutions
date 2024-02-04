VOWEL_SOUND = ("a", "e", "i", "o", "u")
VOWEL_SOUND_Y = VOWEL_SOUND + tuple("y")
IRREGULAR_VOWEL_SOUND = ("xr", "yt")


def translate(text):
    return " ".join(trans_pig(word) for word in text.split())


def trans_pig(word):
    if word.startswith(VOWEL_SOUND) or word.startswith(IRREGULAR_VOWEL_SOUND):
        return word + "ay"

    for index, letter in enumerate(word[1:], start=1):
        if letter in VOWEL_SOUND_Y and not (letter == "u" and word[index - 1] == "q"):
            return word[index:] + word[:index] + "ay"
    return word + "ay"
