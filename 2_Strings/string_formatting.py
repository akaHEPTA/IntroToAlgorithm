# 'in' operator
# If you want to check whether a string contains a specific letter or a substring, you can use 'in' keyword.

favorite = "ice cream" "helado"

print(favorite)
print("ice" in favorite)

# Escaping Characters (\", \', \n)
dont_worry = "Don't worry \"about the weather.!\""
print(dont_worry)

message = "Hi, \n How are you?\nI'm doing good!"
print(message)

# Multi-line strings
prase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings.
"""

# string formatting
# %s: string
# %d: decimal (integer)
name = "Derrick"
message = "hello, pycharm! My name is %s" % name
print(message)

current_year = 2019
year = "It's %d" % current_year
print(year)

info = "name = %s, year = %d ( name, cure"

# string interpolation (from python 3.6)

# String interpolation
# print(F$1= 3, 4- 4 multiply {b] is {a * b}=)
