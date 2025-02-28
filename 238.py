from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    l_arr = [0] * n
    r_arr = [0] * n
    l_mult = 1
    r_mult = 1
    for i in range(n):
        j = n - i - 1
        l_arr[i] = l_mult
        r_arr[j] = r_mult
        l_mult = l_mult * nums[i]
        r_mult = r_mult * nums[j]
    return [x * y for x, y in zip(l_arr, r_arr)]


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    nums = [-1, 1, 0, -3, 3]
    b = productExceptSelf(nums)
    print(b)
