"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""
from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    hash_amt = {0: 0}
    coins.sort()

    def min_coins(amt):
        min_coin = float('inf')
        if amt in hash_amt:
            return hash_amt[amt]
        for coin in coins:
            diff = amt - coin
            if diff < 0:
                break
            min_coin = min(min_coin, 1 + min_coins(diff))
        hash_amt[amt] = min_coin
        return min_coin

    results = min_coins(amount)
    if results < float('inf'):
        return results
    return -1

