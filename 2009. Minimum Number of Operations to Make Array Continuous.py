"""
You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

nums is considered continuous if both of the following conditions are fulfilled:

All elements in nums are unique.
The difference between the maximum element and the minimum element in nums equals nums.length - 1.
For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous.



Example 1:

Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.
Example 2:

Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.
Example 3:

Input: nums = [1,10,100,1000]
Output: 3
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
"""
from typing import List

"""
Logic:
Sort the input array nums in ascending order.
Traverse the sorted array to remove duplicates and count unique elements in uniqueLen.
Initialize ans to the length of the input array, representing the maximum operations initially.
Iterate over unique elements using an outer loop.
Use an inner while loop with two pointers to find subarrays where the difference between the maximum and minimum element is within the array's length.
Calculate the number of operations needed to make all elements distinct within each subarray.
Update ans with the minimum operations found among all subarrays.
Return the minimum operations as the final result.
Complexity
"""

def minOperations(nums: List[int]) -> int:
    n = len(nums)
    nums = sorted(set(nums))
    ans = float("inf")
    for i, num in enumerate(nums):

        search = num +n-1
        low, high= 0, len(nums)-1

        while low <= high:
            mid = (high+low)//2
            if nums[mid] <= search:
                idx=mid
                low = mid +1
            else:
                high = mid-1
        changes = idx-i+1
        ans = min(ans, n-changes)
    return ans

if __name__ == "__main__":
    nums = [1, 2, 3, 5, 6]
    nums = [2, 3, 3, 4]
    b = minOperations(nums)
    print(b)