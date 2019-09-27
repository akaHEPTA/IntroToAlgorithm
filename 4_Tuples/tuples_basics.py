# Tuples are almost identical to lists.
# The only big difference between lists and tuples is that tuples cannot be modified. (immutable)
# You can't add(append), change(modify), or delete(remove) elements from the tuple.

# Tuples = 'immutable lists'
vowel_alphabets = ("a", "e", "i", "o", "u")
# vowel_alphabets[0] = "k"  # Error

# Use cases
# 1. return multiple values from a function
a = (1_000_000 * 1_000, "Derrick")  # Syntactic sugar...
# 2. check if an item is in a collection
print("a" in vowel_alphabets)
# 3. multiple assignments
year, country = (2019, "Canada")  # 2019 -> year, "Canada" -> country
print(str(year) + country)
