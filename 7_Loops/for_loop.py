# Loops - to repeat code

# for loops are used to iterate over a given sequence.
# On each iteration, the variable (loop variable) defined in the for loop will be assigned to the next value(sequence).

# Numbers: a range of numbers (end index number is not inclusive)

# range(end): 0 to end-1
for i in range(10):  # range(10): 0...9
    print(i)

# range(start,end): start to end-1
for i in range(1, 10):  # 1...9
    print(i)

# range(start, end, steps)
for i in range(0, 10, 2):  # from 0...9, go 2 steps at a time
    print(i)  # 0, 2, 4, 8

# Function Overloading
# Overloading a function with a different set of parameters

# Exercises
# 1. Write a loop to print all even numbers from 0 to 100
for i in range(0, 101, 2):
    print(i, end=", ")
print()

# list comprehension
# [print(i) for i in range(101) if i % 2 == 0] -> this also works!

# 2. Write a loop to print all odd numbers from 0 to 100
for i in range(1, 100, 2):
    print(i, end=", ")
print()

# Strings: a sequence of characters
for ch in "Hello":
    print(ch)

# lists: a sequence of items
for item in ["Hello", "Hola", "World"]:
    print(item)

# Exercise
# Print the names that have less than 5 characters.
# Exercise
# Print the names that have less than 5 characters.

names = ["Derrick", "Diego", "Rick", "Richard", "Anzu", "Wenda",
         "Yusuke", "Ryohei", "Bianca", "Tae", "Kam", "Elen",
         "Naoki", "Daniel", "Shohei", "Hotsuma", "Yuka", "Mika",
         "Yuki", "Douglas", "Gabriel"]

for name in names:
    if len(name) < 5:
        print(name, end=" ")
print()

# What is the value of this -> 2^0 + 2^1 + ... + 2^30
result = 0
for i in range(31):
    result += 2 ** i
print(result)

