#!/usr/bin/python3
"""
0x08. Making Change
"""


def makeChange(coins, total):
    """Returns the fewest number of coins needed to meet the given total."""
    if total <= 0:
        return 0

    dp = [0] + [float('inf')] * total

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
