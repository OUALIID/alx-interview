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
        # Generate a list of prime numbers
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        # Check if there's at least one prime number left
        if any(primes[i] for i in range(2, n + 1)):
            if n % 2 == 0:  # Even round number, Ben's turn
                ben += 1
            else:  # Odd round number, Maria's turn
                maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
