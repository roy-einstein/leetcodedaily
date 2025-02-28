"""
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.



Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5


Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
"""

from typing import List

def smallestDistancePair(nums: List[int], k: int) -> int:
    n = len(nums)
    nums.sort()
    minDistance, maxDistance = 0, nums[-1] - nums[0]

    def count_pairs(targetDistance):
        count = 0
        left = 0
        # two-pointers technique
        for right in range(1, n):
            while left < n and nums[right] - nums[left] > targetDistance:
                left += 1
            count += right - left
        return count

    while minDistance < maxDistance:
        midDistance = (maxDistance + minDistance) // 2
        if count_pairs(midDistance) < k:
            minDistance = midDistance + 1
        else:
            maxDistance = midDistance - 1
    return minDistance

if __name__== "__main__":
    nums = [1, 3, 1]
    k = 1
    smallestDistancePair(nums,k)

"""
Algorithm Overview:
The code uses a combination of:

Sorting
Binary Search (on possible distances)
Two-Pointer Technique (to count valid pairs)

Sorting helps efficiently count pairs with the two-pointer technique.
Sorted array ensures that the difference between elements increases as you move right.

minDistance: The smallest possible pair distance (0 if duplicates exist).
maxDistance: The largest possible pair distance (max - min in the array).
We will binary search over this range to find the k-th smallest distance.

Two pointers (left, right) move through the sorted array.
For every right, increment left to ensure nums[right] - nums[left] <= targetDistance.
The number of valid pairs with right as the upper bound is (right - left)

some points 
absoulete distance shows then diffrence between anything always start from {0....}
we can count the pairs by navigating the partial arrays and pair_count is always (right-left)
"""
