VOWEL_SOUND = {"a", "e", "i", "o", "u"}
IRREGULAR_VOWEL_SOUND = {"xr", "yt"}


def translate(text):
    return " ".join([trans_pig(word) for word in text.split()])


def trans_pig(word):
    for tup in enumerate(word):
        index = tup[0]
        if (word[index] == "u" and word[index - 1] == "q") or (word[index + 1] == "y"):
            return word[index + 1 :] + word[: index + 1] + "ay"
        if word[index] in VOWEL_SOUND or word[: index + 2] in IRREGULAR_VOWEL_SOUND:
            return word[index:] + word[:index] + "ay"
