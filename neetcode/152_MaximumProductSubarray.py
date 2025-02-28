"""
Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List

def maxProduct(nums: List[int]) -> int:
    l_mult = 1
    r_mult = 1
    n = len(nums)
    mult = float('-inf')

    for i in range(n):
        l_mult *= nums[i]
        mult = max(mult, l_mult)
        if l_mult == 0:
            l_mult = 1

        j = n - i - 1
        r_mult *= nums[j]
        mult = max(mult, r_mult)
        if r_mult == 0:
            r_mult = 1
    return mult

if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    nums = [-2,0,-1]
    b=maxProduct(nums)
    print(b)