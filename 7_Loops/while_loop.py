# A while loop is similar to an if statement.
# it executes some code if some condition is true.
# It will continue to execute the code for as long as the condition is true.

num = 1

while num <= 10:
    print(num)
    num += 1

# Exercise
# Print all squares from 1 to 99 (1, 4, 9, 16, ... )

i = 1
while i ** 2 < 100:
    print(i ** 2, end=" ")
    i += 1
print()

