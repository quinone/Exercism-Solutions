def response(hey_bob):    
    bob = hey_bob.strip().replace(',', '')
    if bob=='':
        return "Fine. Be that way!"
    if bob[-1]=='?':
        if bob[:-1].isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if bob[:-1].isupper():
        return "Whoa, chill out!"

    return "Whatever."

