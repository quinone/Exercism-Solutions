def equilateral(sides):
    return all(sides) and sum(sides) > 2 * max(sides) and len(set(sides)) == 1
        
def isosceles(sides):    
    return all(sides) and sum(sides) > 2 * max(sides) and len(set(sides)) <= 2 

def scalene(sides):
    return all(sides) and sum(sides) > 2 * max(sides) and len(set(sides)) == 3
