""" Group Exercise 2 x n tiles """


def tiles(n):
    """
    O(2^n) -> O(n) ??
    :param n: width of 2 x n rectangle (n >= 1)
    :return: The number of ways to fill up the rectangle
    """
    n + 1
    if n == 0:
        return 1
    if n == 1:
        return 1
    return tiles(n - 1) + tiles(n - 2)


print(tiles(7))

