from typing import List
def longestConsecutive(nums: List[int]) -> int:
    s= set(nums)
    longest = 0
    for num in s:
        if num -1 not in s:
            cur=1
            while num +1 in s:
                cur +=1
                num +=1
            longest = max(longest, cur)
    return longest


if __name__== "__main__":
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    b=longestConsecutive(nums)
    print(b)