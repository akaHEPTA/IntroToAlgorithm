# Lists, strings, tuples - index-based
# Dictionary: A collection of key-value pairs
# A dictionary is similar to a list, except that you access its values by looking up a key instead of an index.
# A key can be any string or a number.
contacts = {
    "John": "778-123-1234",
    "Dan": "604-842-1234",
    "Max": "778-123-9872",
    "Sean": "213-123-1531"
}
# Key has to be "unique" - DON'T DO THIS
print(contacts["John"])

contacts["Silva"] = "780-123-4783"  # add a new item to the dictionary
contacts["Silva"] = "438-341-1242"  # update the value if the key exist already
del contacts["Silva"]  # remove key-value pair from the dictionary
print(contacts)

# Get the keys as a list
print(list(contacts.keys()))

# Get the values as a list
values = list(contacts.values())
print(values)

# 'in' keyword
# The in keyword is used to check if a list or dictionary contains a specific item.
print("John" in contacts)

