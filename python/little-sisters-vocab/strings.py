"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un' + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied separated with ::.
    """

    prefix = vocab_words[0]
    new_words = []
    new_words.append(prefix)
    for word in vocab_words[1:]:
        new_words.append('::')
        new_words.append(prefix + word)
    return ' '.join(new_words)
    



def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.
    """

    if word[-4:] == 'ness':
        if word[-5] == 'i':
            return word[:-5] + 'y'
        return word[:-4]
    return word

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.
    """

    sentence_list = sentence.split()
    if sentence_list[index][-1] in [',', '.', '!', '?']:
        return sentence_list[index][:-1] + 'en'
    return sentence_list[index] + 'en'
