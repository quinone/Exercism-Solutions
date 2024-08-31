def roman(number):
    result = []
    values = {
        1000 : 'M',
        900: 'CM',
        500 : 'D',
        100 : 'C',
        90 : 'XC',
        50 : 'L',
        40: 'XL',
        10 : 'X',
        9: 'IX',
        5 : 'V',
        4: 'IV',
        1 : 'I',
    }

    for numerical, symbol in values.items():
        
        while numerical <= number:
            number = number - numerical
            result.append(symbol)

    result = ''.join(result)
    result = result.replace('IIII','IV') 
    result = result.replace('VIIII','IX')
    result = result.replace('XXXX','XL')
    result = result.replace('LLLL','XC')
    result = result.replace('CCCC','CD')
    result = result.replace('DDDD','CM')
                
    return result
