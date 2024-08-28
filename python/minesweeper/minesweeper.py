def annotate(minefield):
    # Function body starts here
    print(minefield)
    for index, row in enumerate(
        minefield,
    ):
        if len(minefield[0]) - len(minefield[index]) != 0:
            raise ValueError("The board is invalid with current input.")

    result = []
    row_total = len(minefield)
    row_list = convertSpaceToZero(minefield)

    for y_coordinate, number_list in enumerate(row_list):
        for x_coordinate, character in enumerate(number_list):
            if character == "*":
                if x_coordinate > 0:
                    number_list[x_coordinate - 1] = checkIfStar(
                        number_list[x_coordinate - 1]
                    )
                if x_coordinate < len(number_list) - 1:
                    number_list[x_coordinate + 1] = checkIfStar(
                        number_list[x_coordinate + 1]
                    )
                if y_coordinate > 0:
                    temp_row = row_list[y_coordinate - 1]
                    if x_coordinate > 0:
                        temp_row[x_coordinate - 1] = checkIfStar(
                            temp_row[x_coordinate - 1]
                        )
                    temp_row[x_coordinate] = checkIfStar(temp_row[x_coordinate])
                    if x_coordinate < len(number_list) - 1:
                        temp_row[x_coordinate + 1] = checkIfStar(
                            temp_row[x_coordinate + 1]
                        )
                    row_list[y_coordinate - 1] = temp_row
                if y_coordinate < row_total - 1:
                    # print(row_list[y_coordinate + 1])
                    temp_row = row_list[y_coordinate + 1]
                    if x_coordinate > 0:
                        temp_row[x_coordinate - 1] = checkIfStar(
                            temp_row[x_coordinate - 1]
                        )
                    temp_row[x_coordinate] = checkIfStar(temp_row[x_coordinate])
                    if x_coordinate < len(number_list) - 1:
                        temp_row[x_coordinate + 1] = checkIfStar(
                            temp_row[x_coordinate + 1]
                        )
                    row_list[y_coordinate + 1] = temp_row

    result = []
    for item in row_list:
        temp = "".join(str(e).replace("0", " ") for e in item)
        result.append(temp)
    return result


def checkIfStar(position):
    if isinstance(position, int):
        return position + 1
    return "*"


def convertSpaceToZero(minefield):
    row_list = []
    number_list = []
    for row in minefield:
        for character in row:
            if character == "*":
                number_list.append("*")
            elif character == " ":
                number_list.append(0)
            else:
                raise ValueError("The board is invalid with current input.")
        row_list.append(number_list)
        number_list = []
    return row_list