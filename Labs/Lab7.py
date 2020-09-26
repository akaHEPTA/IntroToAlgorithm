""" Recursion """

# Palindrome is a word, phrase, or sequence that reads the same
# backward as forward.

# Examples)
# is_palindrome(madam) -> True
# is_palindrome(racecar) -> True
# is_palindrome(pizza) -> False


def is_palindrome(word):
    """
    Check if a given string input (word) is a palindrome.
    You must write your solution recursively. (no loops)
    :param word: string input
    :return: True if word is palindrome, otherwise False
    """
    if len(word) < 2:  # One character is palindrome itself -> True
        return True
    if not word[0] == word[-1]:  # If the first and the last character is not matched -> False
        return False
    return is_palindrome(word[1:-1])  # All the case left(First == Last) -> recursion


# without loop, recursion
def my_palindrome(word):
    return word == word[::-1]


print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("pizza"))

print(my_palindrome("madam"))
print(my_palindrome("racecar"))
print(my_palindrome("pizza"))

