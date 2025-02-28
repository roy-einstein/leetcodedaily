"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List
# note
# <-|1|2|3| --- |100|---|102|-->
# <--------------------------- > scale
#  start with look back if number exist then keep looking till its first number in sequence, in above case
# |1|, |100|, |102| are number with starting point

def longestConsecutive(nums: List[int]) -> int:
    s = set(nums)
    longest = 0
    for num in s:
        if num - 1 not in s:
            cur = 1
            while num + 1 in s:
                cur += 1
                num += 1
            longest = max(longest, cur)
    return longest

if __name__ == "__main__":
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    b = longestConsecutive(nums)
    print(b)