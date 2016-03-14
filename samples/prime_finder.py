import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number)) + 1, 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(beg, end):
    current = beg
    while current < end:
        if is_prime(current):
            yield current
        current += 1
            
    
