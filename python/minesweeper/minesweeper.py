def annotate(minefield):
    # Function body starts here
    if minefield == []:
        return []
    if len(set(map(len, minefield))) != 1:
        raise ValueError("The board is invalid with current input.")

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    row = len(minefield)
    col = len(minefield[0])
    result = [list(row) for row in minefield]

    for y in range(row):
        for x in range(col):
            if minefield[y][x] == "*":
                continue
            if minefield[y][x] != " ":
                raise ValueError("The board is invalid with current input.")
            mine_count = sum(
                1
                for dy, dx in directions
                if 0 <= y + dy < row
                and 0 <= x + dx < col
                and minefield[y + dy][x + dx] == "*"
            )
            if mine_count > 0:
                result[y][x] = str(mine_count)

    return ["".join(row) for row in result]
