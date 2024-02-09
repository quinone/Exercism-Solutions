def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")
    primes = []
    position = 1
    for n in range(number):
        
        while True:
            position+=1
            if isPrime(position):
                primes.append(position)
                break
            
    return primes[-1]
        

def isPrime(number):
    if number == 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return True