# Data structure
# list: A sequence of items (elements)

# 1. create a list
squares = [1, 4, 9, 16, 25, 36, 49]

print(squares)

# 2. list operations
# + add a list
animals = ["Eagle", "Snake", "Panda", "Lion", "Tiger", "Bear", ]
animals += ["Koala", "Dog"]  # add two items to the list
print(animals)

animals.append("Cat")  # add "Cat" item at the end of the list
print(animals)
animals.insert(0, "Monkey")  # insert "Monkey" at 0 index
print(animals)
animals.remove("Snake")  # return NOTHING
print(animals)
print(animals.pop(0))  # pop the element at index 0

animals.count("Cat")  # How many same values are in the list? --> 1

# index: returns the index of the first element in the list
print(animals.index("Panda"))
