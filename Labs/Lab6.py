""" Primes, GCD, LCM """
import math


def is_prime(n):
    """ Check if n is prime """
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def gcd(a, b):
    """ GCD of a and b """
    while not b == 0:  # Based on Euclidean Algorithm
        remainder = a % b
        a = b
        b = remainder
    return a


def lcm(a, b):
    """ LCM of a and b """  # Basic idea of getting lcm is same
    return int(a * b / gcd(a, b))


def generate_primes(n):
    """
    Generating a list of primes
    :return: a list of primes from 2 to n
    """
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


# test codes
print(gcd(13054, 32635))
print(lcm(13054, 32635))
print(generate_primes(50000))
