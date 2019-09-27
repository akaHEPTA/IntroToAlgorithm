import math


def is_prime(n):
    """ Check if n is prime """
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False

    return True

print(is_prime(31))
