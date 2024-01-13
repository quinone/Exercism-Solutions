def equilateral(sides):
    a, b, c = sides
    return isTriangle(sides) and (a == b) and (b == c)
           
def isosceles(sides):    
    a, b, c = sides
    return isTriangle(sides) and ((a == b) or (b == c) or (a == c))

def scalene(sides):
    return isTriangle(sides) and not (equilateral(sides)) and not (isosceles(sides))

def isTriangle(sides):
    return all(sides) and sum(sides) > 2 * max(sides)