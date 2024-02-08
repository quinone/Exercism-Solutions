def flatten(iterable):
    flat_list = []
    for item in iterable:
        if type(item) == list:
            flat_list += flatten(item)
        elif item is not None:
            flat_list.append(item)
    return flat_list
