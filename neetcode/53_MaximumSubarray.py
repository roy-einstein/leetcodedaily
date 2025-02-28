# https://leetcode.com/problems/maximum-subarray/description/
"""
Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List

#  logic, smallest number in negative array is smallest negative number, so always work on possitive number
def maxSubArray(nums: List[int]) -> int:
    n = len(nums)
    cur_sum =0
    max_sum = float('-inf')
    for i in range(n):
        cur_sum += nums[i]
        max_sum = max(max_sum, cur_sum)
        if cur_sum <0:
            cur_sum = 0
    return max_sum

def minSubArray(nums: List[int]) -> int:
    n = len(nums)
    cur_sum =0
    min_sum = float('inf')
    for i in range(n):
        cur_sum += nums[i]
        min_sum = min(min_sum, cur_sum)
        if cur_sum >0:
            cur_sum = 0
    return min_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-5,-3,-4,-7,-8]
    # nums = [5, 4, -1, 7, 8]
    nums = [2,-5,1,-4,3,-2]
    nums = [-3, -5, -3, -2, -6, 3, 10, -10, -8, -3, 0, 10, 3, -5, 8, 7, -9, -9, 5, -8]
    b = maxSubArray(nums)
    c = minSubArray(nums)
    print(b)
    print(c)
