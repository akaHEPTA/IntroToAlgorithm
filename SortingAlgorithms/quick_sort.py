# Quick sort

import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


alist = []

for _ in range(100):
    alist.append(random.randint(0, 1000))

print("Random array created")
print(alist)

print("Quick sorting...")
print(quick_sort(alist))

