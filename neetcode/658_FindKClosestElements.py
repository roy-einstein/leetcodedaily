"""
Given a sorted integer array arr, two integers k and x,
return the k closest integers to x in the array.
 The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]



Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""

from typing import List


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    n = len(arr)

    def binary_search(arr, x):
        left, right = 0, n - 1
        while left < right:
            if arr[left] <= x:
                return left
            if arr[right] >= x:
                return right

            mid = (right + left) // 2
            if arr[mid] <= x < arr[mid + 1]:
                return mid
            if arr[mid] > x:
                left = mid + 1
            if arr[mid] < x:
                right = mid - 1

    i = binary_search(arr, x)
    ans = []
    left, right = i, i + 1
    if arr[i] == x:
        left = i - 1
    while k and left >= 0 and right < n:
        x1 = x - arr[left]
        x2 = arr[right] - x
        if x1 < x2:
            ans.append(arr[left])
            left += 1
        else:
            ans.append(arr[right])
            right -= 1
        k -= 1

    while k > 0 and left >= 0:
        ans.append(arr[left])
        left -= 1
        k -= 1
    while k > 0 and right < n:
        ans.append(arr[right])
        right += 1
        k -= 1

    return ans


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    b=findClosestElements(arr, k, 3)
    print(b)