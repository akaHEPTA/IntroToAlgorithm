# Python operators
# +, -, *, /, //
# % (modulo): remainder "mod"
# ** (power)

print(10 % 3)  # 1
print(10 ** 2)  # 100

# = assignment operator
number = 7

# += : increments number by 3
number = number + 3
print("number = " + str(number))

# -= : decrement operator
number = number - 3
print("number = " + str(number))
number -= 3
print("number = " + str(number))

# += : multiple by operator
number *= 2  # number = number * 2
print("number = " + str(number))

# /= : divide by operator
number /= 2  # number = number / 2
print("number = " + str(number))

# Boolean Operators
# Boolean(bool) is a type of value that can only be True or False.

# Comparison
# == : equality (equal)
print(3 == 4)  # False

# > : greater than
# >= : greater than and equal to
# < : less than
# <= : less than and equal to

print(3 < 4)  # True
print(3 <= 4)  # True

# This chained comparison means that the (3 < 4) and (4 < 5)
# Comparisons are performed at the same time.
print(3 < 4 < 5)  # True
print((3 < 4) and (4 < 5))  # True - same result
print((3 != 3) or (4 == 4))  # either one of them is True ==> True

# Exercise
num = 10
print((num > 1) and (num / 0 == 0))  # Error
print((num > 10) and (num / 0 == 0))  # False
print((num > 1) or (num / 0 == 0))  # True
print((num > 10) or (num / 0 == 0))  # Error
# ! : not available in Python
print(not True)  # False
print(not False)  # True

