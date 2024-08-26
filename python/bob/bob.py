def response(hey_bob):
    bob = hey_bob.strip().replace(",", "")
    if not bob:
        return "Fine. Be that way!"
    if bob.endswith('?'):
        if bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if bob.isupper():
        return "Whoa, chill out!"

    return "Whatever."
