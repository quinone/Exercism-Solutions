def label(colors):
    bands = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9,
    }
    result = []
    for color in colors:
        if color in bands:
            result.append(bands.get(color))
        
    result[2] = result[2]*'0'
    print(result)        
    result = [str(band) for band in result]
    print(result)
    if result[2] == '000':
        result[2] = ' kilo'
    elif result[2] == '000000':
        result[2] = ' mega'
    else:
        result[2]+=' '
    if result[0] == '0':
        result.remove('0')
    result = ''.join(result) + 'ohms'

    return result
