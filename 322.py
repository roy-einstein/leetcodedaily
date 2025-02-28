from itertools import count
from typing import List
def coinChange(coins: List[int], amount: int) -> int:
    coins.sort()
    mem_cache = {0:0}
    def min_coins(amt):
        if amt in mem_cache:
            return  mem_cache[amt]
        minn = float('inf')
        for coin in coins:
            diff = amt-coin
            if diff <0:
                break
             minn = min(minn, 1+ min_coins(diff))
        mem_cache[amt] = minn
        return minn
    results = min_coins(amount)
    if results < float('inf'):
        return results
    else:
        return -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    b=coinChange(coins, amount)
    print(b)