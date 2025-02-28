"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
"""
logic:

nums = [1,2,3,1]

consider dp array= [0, 0, 0, 0]
1. take 1 [1,0,0,0]
2. either take 2 or take 1 max(1,2) -> [1,2,0,0]
3. either take 3 + 1 behind of previous aka 1 or take 3 (previous) greater = [1,2,4,0]
4. either take 1 + 1 behind of previous aka 2 or take 4 previous : greater  = [1,2,4,4]

now do this steps twice 1 from nums[0:n-1] and nums[1:n]

"""
from typing import List

from functools import cache

def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    if n < 3:
        return max(nums)

    def dp(nums):
        rob2, rob1 = 0, 0
        for i in nums:
            rob2, rob1 = max(rob2, rob1 + i), rob2
        return rob2

    return max(dp(nums[0:n - 1]), dp(nums[1:n]))


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    b=rob(nums)
    print(b)