# Indexing a list
countries = ["Canada", "China", "Mexico", "Japan", "Brazil", "Iran", "Korea", "Philippines", "USA"]

print(countries[0])  # Canada
print(countries[-1])  # USA
print(countries[len(countries)-1])  # USA

# Modify elements - lists are mutable
countries[0] = "England"
print(countries)

# Slicing lists (end index is not inclusive)
print(countries[0:3])
countries[4:6] = []  # removes 2 items at index 4 and 5
countries[0:3] = ["USA"]  # replaces 3 items at index 0, 1, 2 to "USA"
print(countries)

# str vs list
# Strings are immutable. Strings contain characters.
# lists are mutable. Lists can have any type of elements.

province = "AB"
# mutate str province
province[0] = "C"  # Error -> strings are immutable.
# re-assign a new value to province
province = "BC"
