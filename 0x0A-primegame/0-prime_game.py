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

    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for x in range(2, int(n**0.5) + 1):
        if primes[x]:
            for y in range(x**2, n + 1, x):
                primes[y] = False

    for n in nums:
        count = sum(primes[2:n+1])
        ben += count % 2 == 0
        maria += count % 2 == 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
