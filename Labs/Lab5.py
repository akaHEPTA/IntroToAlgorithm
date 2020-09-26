""" Sorting Practice Problems """

# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.
alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6]


def sort_half(alist):
    first_half = alist[:len(alist) // 2]
    last_half = alist[len(alist) // 2:]

    # Ascending
    for i in range(len(first_half) - 1):
        least = i
        for j in range(i + 1, len(first_half)):
            if first_half[j] < first_half[least]:
                least = j
        if not least == i:
            first_half[i], first_half[least] = first_half[least], first_half[i]

    # Descending
    for i in range(len(last_half) - 1, 0, -1):
        least = i
        for j in range(i - 1, -1, -1):
            if last_half[j] < last_half[least]:
                least = j
        if not least == i:
            last_half[i], last_half[least] = last_half[least], last_half[i]

    return first_half + last_half


# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.
A = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
B = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def merge_two(A, B):
    # A += B
    # for i in range(len(A) - 1):
    #     least = i
    #     for j in range(i + 1, len(A)):
    #         if A[j] < A[least]:
    #             least = j
    #     if not least == i:
    #         A[i], A[least] = A[least], A[i]
    i = j = 0
    result = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1

    # Add the lefts if one of the list is already finished
    if i == len(A):
        result += B[j:]

    if j == len(B):
        result += A[i:]

    return result


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.
mylist = [2, 5, -1, 3, 7, -2, 8]


def replace_negative(mylist):
    res = []
    for num in mylist:
        if num < 0:
            res.append(0)
        else:
            res.append(num)
    return res


