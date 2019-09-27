# Bubble Sort - "Bubbling" the largest element to the right side
# (pseudo-code)
# list = [...]
# for each i from 1 th len(list)
#   compare two adjacent elements
#   if the first element is greater than the second element
#   swap two elements

import random


# Time Complexity - O(n^2)
def bubble_sort(alist):
    print("Before: " + str(nums))
    cnt = 0
    for i in range(len(alist)):
        swapped = False
        for j in range(len(alist) - 1 - i):
            cnt += 1
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                swapped = True
        if not swapped:
            break

    print("After: " + str(nums))
    print("Steps: " + str(cnt))


# Create random integer list
nums2 = [3, 4, 1, 5, 2]
nums = []

for i in range(100):
    nums.append(random.randrange(0, 1000))

bubble_sort(nums)








#
# def swap(a, b):
#     nums[a], nums[b] = nums[b], nums[a]
#
