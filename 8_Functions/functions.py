# Functions are a convenient way to devide your code into useful blocks, make it more readable and help to 'reuse' it.
# In Python, functions are defined by using the keyword 'def', followed by function's name.

# TL;DR -> "A reusable block of code"


# define a function
def print_menu():
    print("MENU")
    print("1. Tacos")
    print("2. Brazilian BBQ")
    print("3. Kebab")
    print("4. Hotpot")
    print("5. Sashimi")
    print("6. Sinigang")
    print("7. Kimchi")


# call, execute the function
for _ in range(5):
    print_menu()


# Parameters vs Arguments
def add_two(a, b):  # a, b: parameters
    return a + b


result = add_two(10, 20)  # 10, 20: arguments
print(result)


# Define a function similar to 'range' function.
# Default parameters - when the functions did not get the parameter, default value will be used
def my_range(start, end, steps=1):
    """
    Returns a list of numbers from start to end by steps
    :param start: start number
    :param end: end number
    :param steps: interval
    :return: a list
    """
    templist = []
    # for num in range(start, end, steps):
    #     templist.append(num)
    while start < end:
        templist.append(start)
        start += steps

    return templist


print(my_range(1, 20))


def your_range(*args):  # *args(arguments):
    if len(args) == 1:
        templist = []
        i = 0
        while i < args[0]:
            templist.append(i)
            i += 1
        return templist
    elif len(args) == 2:
        return my_range(args[0], args[1])
    elif len(args) == 3:
        return my_range(args[0], args[1], args[2])
    else:
        print("Invalid number of arguments.")
        return []


print(your_range(10))
print(your_range(1, 10))
print(your_range(1, 10, 2))

