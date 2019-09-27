city = "vancouver"

# func() -> call, execute, run

print(city.upper())  # VANCOUVER
print(city.capitalize())  # Vancouver

# index: returns the index of substring
# find: returns the index of first
# no match will return -1
print(city.index("v"))
print(city.index("cou"))
print(city.find("v"))
print(city.find("cou"))

#count: returns the occurrences of substring in string.
# Case-sensitive (0) vs Case-insensitive (x)
greetings = "hello hello hello"
print(greetings.count("hello"))

my_int = "123"

# isalnum(): checks alphanumeric characters
# isalpha(): checks if all characters are alphabets
# isdigit(): checks digit characters
# isupper(): checks if characters are uppercase
# islower(): checks if characters are lowercase
# isspace(): check whitespace characters

print(my_int.isdigit())

