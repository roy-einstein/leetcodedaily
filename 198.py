from typing import List

def rob(nums: List[int]) -> int:
    n = len(nums)
    l_sum, r_sum = 0,0
    max_value =0
    for i in range(0,n,2):
        print("i",i)
        j = n-i-2
        print("start",j)
        l_sum += nums[i]
        max_value = max(max_value, l_sum)
        if j%2 !=0:
            print("end",j)
            r_sum +=nums[j]
            max_value = max(max_value, r_sum)
    return max_value

if __name__ == "__main__":
    nums = [1,2,3,1]
    nums = [1,3,1]
    b=rob(nums)
    print(b)