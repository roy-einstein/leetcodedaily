from typing import List
def maxProduct(nums: List[int]) -> int:
    n = len(nums)
    l_mult, r_mult =1,1
    max_value = nums[0]
    for i in range(n):
        j =n-i-1
        l_mult = l_mult*nums[i]
        max_value = max(max_value, l_mult)
        if l_mult == 0:
            l_mult=1

        r_mult = r_mult * nums[j]
        max_value = max(max_value, r_mult)
        if r_mult ==0:
            r_mult =1
    return max_value

if __name__ == "__main__":
    nums = [2,3,-2,4]
    nums = [-1,4,-4,5,-2,-1,-1,-2,-3]
    b=maxProduct(nums)
    print(b)


