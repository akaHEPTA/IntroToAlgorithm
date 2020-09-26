# Anagram exercise


def is_anagram(A, B):
    if len(A) == len(B):
        for char in A:
            if char not in B:
                return False
        return True


print(is_anagram("listen", "silent"))

