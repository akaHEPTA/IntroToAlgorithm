# Binary search

alist = ["Australia", "Brazil", "Canada", "Denmark", "Ecuador", "France", "Germany", "Honduras", "Iran", "Japan",
         "Korea", "Latvia", "Mexico", "Netherlands", "Oman", "Philippines", "Qatar", "Russia", "Spain", "Turkey",
         "Uruguay", "Vietnam", "Wales", "Xochimilco", "Yemen", "Zambia"]


def binary_search(collection, target):
    """
    Binary Searchs
    - How you look up a workd in dictionary or a contact in phone book.
    * Items have to be sorted!
    """

    low = cnt = 0
    high = len(alist) - 1

    while low <= high:
        cnt += 1
        guess = (low + high) // 2

        if collection[guess] == target:
            # print("Guess[" + str(cnt) + "]: " + str(guess))
            return guess
        elif collection[guess] < target:
            # print("Guess[" + str(cnt) + "]: " + str(guess))
            low = guess + 1
        elif collection[guess] > target:
            # print("Guess[" + str(cnt) + "]: " + str(guess))
            high = guess - 1

    return -1


# Case sensitive!!!
print(binary_search(alist, "Canada"))
print(binary_search(alist, "Mexico"))
print(binary_search(alist, "Japan"))
print(binary_search(alist, "Italy"))
print(binary_search(alist, "China"))
