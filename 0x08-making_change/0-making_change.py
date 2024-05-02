#!/usr/bin/python3
"""Change comes from within
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    Parameters:
        coins (list of int): A list containing the values of available coins.
        total (int): The target total amount to be achieved using the coins.
    Returns:
        int: The fewest number of coins needed to meet the given total.
        Returns -1 if the total cannot be achieved with the available coins.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
