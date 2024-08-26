def find(search_list, value):
    if not search_list:
        raise ValueError("value not in array")
    start, end = 0, len(search_list) - 1
    middle_position = (end) // 2
    if value < search_list[start] or value > search_list[end]:
        raise ValueError("value not in array")
    if search_list[middle_position] == value:
        return middle_position

    if search_list[middle_position] < value:
        return middle_position + 1 + find(search_list[middle_position + 1 :], value)

    if search_list[middle_position] > value:
        return find(search_list[:middle_position], value)

    raise ValueError("Value not in array")
