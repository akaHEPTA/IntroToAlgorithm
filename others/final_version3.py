""" Final Exam V3 """


# please submit your python file upon completion.

def is_anagram(s: str, t: str):
    """
    An anagram is a word or phrase formed by rearranging the
    letters of a different word or phrase, typically using all
    the letters exactly once.

    Given two strings s and t, write a program to
    determine if t is an anagram of s.
    You may assume that the string contains only lowercase alphabets.

    e.g.
    is_anagram("anagram", "nagaram") -> True
    is_anagram("rat", "car") -> False
    is_anagram("listen", "silent") -> True
    is_anagram("", "") -> True
    is_anagram("h", "e") -> False

    :param s: string
    :param t: string
    :return: True if s is an anagram of t, otherwise False
    """

    # 1. check the length of two string
    # 2. if the character of s is not in t, it is not anagram
    # 3. if the program didn't find any differences until the end of the string, it's anagram

    if len(s) == len(t):
        for char in s:
            if char not in t:
                return False
        return True
    return False


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("listen", "silent"))
print(is_anagram("", ""))
print(is_anagram("h", "e"))
print("End of question 1.")
print()


def remove_vowels(s: str):
    """
    Write an algorithm to remove all vowels from a string without replace() built-in method.
    You can write iteratively or recursively.

    e.g.
    remove_vowels("hello") -> "hll"
    remove_vowels("world") -> "wrld"
    remove_vowels("what") -> "wht"
    remove_vowels("") -> ""
    remove_vowels("a") -> ""

    :param s: string
    :return: string removed vowels
    """

    # Case sensitive
    vowels = "aeiouAEIOU"
    result = ""

    for char in s:
        if char not in vowels:
            result += char

    return result


print(remove_vowels("hello"))
print(remove_vowels("world"))
print(remove_vowels("what"))
print(remove_vowels(""))
print(remove_vowels("a"))
print("End of question 2.")
