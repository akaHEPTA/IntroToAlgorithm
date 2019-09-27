# String (str) : A sequence of characters in "" or ''

# + Concatenation: combining two strings
print("hello" + " world")

# * multiplication: repeat strings
print("hello" * 5)  # hellohellohellohellohello

# String indexing (position)
singer = "Justin Bieber"

print(singer[7])  # "B"
print(singer[-6])  # "B"
print(singer[-1])  # last char
# print(singer[-14])  # Error (out of index)

# String slicing
# index
# [start index : end index] - last index is INCLUSIVE
actor = "Brad Pitt"
print(actor[0:3])

# shortcuts
# starting at 0 index
print(actor[:4])
# starting at 5 to the end
print(actor[5:])
# from 0 to the end (copy)
print(actor[:])

# THERE IS NO CHAR TYPE IN PYTHON
print(ord("a"[0]))

# How to get the number of characters?
# actor's last index: length - 1
print(len(actor))  # 9
print(actor[-1])
print(actor[len(actor)-1])
print(actor[8])
