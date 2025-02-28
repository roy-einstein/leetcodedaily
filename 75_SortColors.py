"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

"""
from typing import List

def sortColors(nums: List[int]) -> None:
    n = len(nums)
    count=[0,0,0]
    for color in nums:
        count[color] +=1
    R,W,B = count

    nums[:R] = [0]* R
    nums[R:W+R] =[1]*W
    nums[W+R:] =[2] *B
    return

if __name__ == "__main__":
    nums =[0]
    sortColors(nums)
    print(nums)