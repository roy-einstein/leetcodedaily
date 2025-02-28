
from typing import List

def minimizeArrayValue(nums: List[int]) -> int:
    n = len(nums)
    def check_min(k):
        temp = 0
        for i in range(n-1,0,-1):
            if temp+nums[i] >k:
                temp +=nums[i]-k
            else:
                temp = 0
        return False if temp + nums[0] > k else True
    l=1
    h=10 **5 +1
    while l<h:
        m= (h+l)//2
        if check_min(m):
            h=m
        else:
            l=m+1
    return l

if __name__ =="__main__":
    nums = [3, 7, 1, 6]
    b=minimizeArrayValue(nums)
    print(b)
