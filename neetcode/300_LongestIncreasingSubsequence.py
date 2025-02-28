"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence
.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
"""
# ref:
# https://www.youtube.com/watch?v=MrPa5EFcDCU
# https://www.youtube.com/watch?v=cjWnW0hdF1Y

"""
logic:
lets consider array =[0,1,0,3,2,3]
then answer space is  
{
Index | value
0-0   |[0]  -> 1
0-1   |[0,1]
0-2   |[0,1,0],
0-3   |[0,1,0,3]
0-4   |[0,1,0,3,2]
0-5   |[0,1,0,3,2,3]
}
so we got to know answer for single element is 1 (default value)
compare the first element with all other element and see if its greater than 1 then add 1 to existing default value

"""
from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    dp = [1]*n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1+ dp[j])
    return max(dp)

if __name__ == "__main__":
    nums =[10,9,2,5,3,7,101,18]
    b = lengthOfLIS(nums)
    print(b)