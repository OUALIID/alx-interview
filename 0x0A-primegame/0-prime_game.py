#!/usr/bin/python3
"""
0x0A. Prime Game
"""


def isWinner(x, nums):
    """Prime game winner determination"""
    if x < 1 or not nums:
        return None

    maria = 0
    ben = 0

    for n in nums:
        prime_count = 0
        for i in range(2, n + 1):
            if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
                prime_count += 1
        if prime_count % 2 != 0:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
