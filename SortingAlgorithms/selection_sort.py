# Selection Sort
# pseudo-code
# for each scan from 0 th len(alist)
#   find the min element
#   swap the min element with alis[scan]

import random

# Time Complexity
# O(n^2) Algorithm


def selection_sort(alist):
    print("Before: " + str(nums))
    steps = 0
    for i in range(len(alist) - 1):
        least = i
        for j in range(i + 1, len(alist)):
            steps += 1
            if alist[j] < alist[least]:
                least = j
        if not least == i:
            alist[i], alist[least] = alist[least], alist[i]
    print("After: " + str(nums))
    print("Steps: " + str(steps))


# Create random integer list
nums = []
for i in range(5):
    nums.append(random.randrange(0, 100))
selection_sort(nums)
