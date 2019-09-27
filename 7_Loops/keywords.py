# break: stop
# break out of the loop if there's 4
# print numbers before 4
items = [12, 1, 5, 4, 16, 21, 6, 3, 8, 7]

print("Q1")
for item in items:
    if item == 4:
        break
    print(item, end=" ")
print("\n")

# continue: skip
# print all numbers except for 4

print("Q2")
for item in items:
    if item == 4:
        continue
    print(item, end=" ")
print("\n")
