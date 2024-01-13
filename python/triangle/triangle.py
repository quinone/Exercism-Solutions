def equilateral(sides):
    return isTriangle(sides) and len(set(sides)) == 1
        
def isosceles(sides):    
    return isTriangle(sides) and len(set(sides)) <= 2 

def scalene(sides):
    return isTriangle(sides) and len(set(sides)) == 3

def isTriangle(sides):
    return all(sides) and sum(sides) > 2 * max(sides)