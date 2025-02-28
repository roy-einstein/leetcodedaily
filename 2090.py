from typing import List

def getAverages(nums: List[int], k: int) -> List[int]:
    radius = 0
    n = len(nums)
    ans = [-1]*n
    for i in range(k, n):
        if len(nums[i:i+k]) == len(nums[i+k:i+k*2]):
            radius = sum(nums[i:k*2 +i])
            ans[i+k-1] = radius / k+1
    return ans

def getAverages(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    ans = [-1]*n
    start = 0
    end = 2*k
    if end +1 > n:
        return ans
    prefix_sum = [0]*(n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + nums[i]
    print(prefix_sum)
    f=sum(nums[start:end+1])
    while end < n:
        ans[start+k] = f //(2*k+1)
        f +=nums[end+1]-nums[start]
        start +=1
        end += start
    return ans

if __name__=="__main__":
    nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k = 3
    print(getAverages(nums,k))