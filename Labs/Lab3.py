"""
 String, List - Level 2.0
"""


def count_hi(string: str):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    # WASTES
    # after_h = False
    # cnt = 0
    # # Need to scan the string only once
    # for char in string:
    #     if char == 'h':
    #         after_h = True
    #     elif char == 'i' and after_h is True:
    #         cnt += 1
    #         after_h = False
    #     else:
    #         after_h = False
    # return cnt
    return string.count("hi")


def cat_dog(string: str):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    # WASTES
    # if len(string) < 3:
    #     return True
    # else:
    #     cat_cnt = dog_cnt = 0
    #     for i in range(len(string) - 2):
    #         if string[i:i+3] == "cat":
    #             cat_cnt += 1
    #         elif string[i:i+3] == "dog":
    #             dog_cnt += 1
    #
    #     if cat_cnt == dog_cnt:
    #         return True
    # return False
    return string.count("cat") == string.count("dog")


def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    # No need to check the length - range() automatically check the range
    code_cnt = 0
    for i in range(0, len(string) - 3):
        if string[i:i + 2] == "co" and string[i + 3] == "e":
            code_cnt += 1
    return code_cnt


def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """
    # 1. make both strings lowercase
    a = a.lower()
    b = b.lower()
    # 2. get the length of two strings and compare, swap if the "a" is smaller than "b"
    if len(a) < len(b):
        a, b = b, a
    # 3. check if the shorter string appears at the end of longer string
    return a[-len(b):] == b


def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    cnt = 0
    for i in nums:
        if i % 2 == 0:
            cnt += 1
    return cnt
    # return len([i for i in nums if i % 2 == 0])


def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    # min_ = max_ = nums[0]
    # for i in nums:
    #     if i < min_:
    #         min_ = i
    #     if i > max_:
    #         max_ = i
    # return max_ - min_
    return max(nums) - min(nums)


def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    # after_13 = False
    # res = 0
    # for i in nums:
    #     if i == 13:
    #         after_13 = True
    #     elif not i == 13 and after_13 is True:
    #         after_13 = False
    #     else:
    #         res += i
    # return res

    i = 0
    total = 0
    while i < len(nums):
        if nums[i] != 13:
            total += nums[i]
            i += 1
        else:
            i += 2
    return total


def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    # after_6 = False
    # res = 0
    # for i in nums:
    #     if i == 6:
    #         after_6 = True
    #     elif i == 7 and after_6 is True:
    #         after_6 = False
    #     elif after_6 is False:
    #         res += i
    # return res
    total = 0
    add = True
    for num in nums:
        if num == 6 and add:
            add = False
            continue
        if num == 7 and not add:
            add = True
            continue
        if add:
            total += num
    return total


def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    # after_2 = False
    # for i in nums:
    #     if i == 2 and after_2 is True:
    #         return True
    #     elif i == 2 and after_2 is False:
    #         after_2 = True
    #     else:
    #         after_2 = False
    # return False
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False

