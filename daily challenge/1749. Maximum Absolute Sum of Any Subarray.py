"""
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.


Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""

"""
logic to be noted: Kdane algo or prefix sum read prefix.md in Onclick"""

from typing import List
def maxAbsoluteSum(nums: List[int]) -> int:
    max_sum=float('-inf')
    min_sum=float('inf')
    cur_sum = 0
    # find max sum in subarray
    for n in nums:
        cur_sum +=n
        max_sum=max(max_sum,cur_sum)
        if cur_sum<0:
            cur_sum=0
    cur_sum = 0
    for n in nums:
        cur_sum +=n
        min_sum = min(min_sum, cur_sum)
        if cur_sum>0:
            cur_sum=0
    return max(abs(max_sum),abs(min_sum))

def maxAbsoluteSum_2(nums: List[int]) -> int:
    # finding the prefix sum
    prefix =[nums[0]]
    for i in range(1,len(nums)):
        prefix.append(prefix[i-1] +nums[i])

    return max(prefix) - min(prefix)

if __name__ == '__main__':
    nums = [1, -3, 2, 3, -4]
    b=maxAbsoluteSum(nums)
    c=maxAbsoluteSum_2(nums)
    print(b)
    print(c)