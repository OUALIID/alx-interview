#!/usr/bin/python3
"""
0x08. Making Change
"""


def makeChange(coins, total):
    """Returns the fewest number of coins needed to meet the given total."""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    return count if total == 0 else -1
