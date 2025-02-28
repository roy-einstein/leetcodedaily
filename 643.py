from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    sum_k = sum(nums[:k])
    avg = sum_k / k
    n = len(nums)
    for i in range(k,n):
        sum_k += nums[i]
        sum_k -= nums[k-i]
        avg = max(avg, sum_k/k)
    return avg

if __name__ =="__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    b=findMaxAverage(nums,k)
    print(b)