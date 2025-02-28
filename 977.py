from typing import List
"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
def sortedSquares(nums: List[int]) -> List[int]:
    l, r = 0, len(nums)-1
    result=[0]*len(nums)
    n=len(nums)-1
    while l<=r:
        if abs(nums[l]) < abs(nums[r]):
            s = nums[r] **2
            r -=1
        else:
            s = nums[l] ** 2
            l +=1
        result[n] = s
        n -=1
    return result

if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    nums = [-7, -3, 2, 3, 11]
    b=sortedSquares(nums)
    print(b)

