# Prints the given number of starts in the console
# assume n >= 1


def print_stars(n):
    if n == 1:  # base case
        print("*")
    else:  # recursive case
        print("*", end="")
        print_stars(n - 1)


print_stars(5)
print_stars(2)


# Factorial (recursively) - without using a loop
def factorial_recur(n):
    # base case
    if n == 1:
        return 1
    else:
        return n * factorial_recur(n - 1)


def fibonacci(n):
    """ Iteratively (loop) """
    a = b = 1
    for _ in range(n - 1):  # a, b (we already have 2 numbers)
        a, b = b, a + b
    return a


def fibonacci_recur(n):
    """ Recursively (no loop) """
    # base
    if n == 0 or n == 1:
        return 1
    # recursive
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)
# fib(n) = fib(n-1)+fib(n-2)
# factorial(n) = n * factorial(n-1)


# returns base^exp
# precondition: exp >= 0
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

