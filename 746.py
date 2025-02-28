from typing import List
def minCostClimbingStairs(cost: List[int]) -> int:
    def dp(n):
        if n<2:
            return cost[n]
        return cost[n]+min(dp(n-1), dp(n-2))
    l = len(cost)
    return min(dp(l-1), dp(l-2))

def minCostClimbingStairs(cost: List[int]) -> int:
    for i in range(len(cost)-3, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])
    return min(cost[0], cost[1])

if __name__ == "__main__":
    cost = [10, 15, 20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    b=minCostClimbingStairs(cost)
    print(b)