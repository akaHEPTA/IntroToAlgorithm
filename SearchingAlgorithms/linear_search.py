# Linear Search

alist = ["Apple", "Banana", "Kiwi", "Peach", "Watermelon", "Mango", "Pears", "Grapes", "Mangosteen", "Strawberry"]


def linear_search(collection, target):
    """
    Returns the index of the target object from the coleection.
    Return -1 if the target is does not exist in the coleection.
    """
    for i in range(len(collection)):
        if collection[i] == target:
            return i
    return -1


print(linear_search(alist, "Kiwi"))