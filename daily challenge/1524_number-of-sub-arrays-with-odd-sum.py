"""
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.



Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16


Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100
"""

"""
Logic:

High-Level Idea:
Use prefix sums to efficiently compute subarray sums.
A subarray sum is odd if the difference between two prefix sums (from start to some index) is odd.
Leverage the properties of even and odd numbers:
even - even = even
odd - odd = even
even - odd = odd
odd - even = odd
"""
from typing import List
def numOfSubarrays(arr: List[int]) -> int:
    prefix_sum=odd=0
    even =1
    for num in arr:
        prefix_sum+=num
        if prefix_sum%2: # odd prefix sum
            odd +=1
        else: #even prefix sum
            even +=1
    return all_sum

if __name__ == '__main__':
    arr = [1, 3, 5]
    b=numOfSubarrays(arr)
    print(b)