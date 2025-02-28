from math import ceil
from typing import List

def minSpeedOnTime(dist: List[int], hour: float) -> int:
    def check(k):
        cnt=0
        for d in dist[:-1]:
            cnt +=ceil(d/k)
        cnt +=dist[-1]/k
        return cnt <= hour
    low=1
    high = 10 ** 5 +1
    while low< high:
        mid = (high+low)//2
        if check(mid):
            high = mid
        else:
            low =mid+1
    return low

if __name__ == "__main__":
    dist = [1, 3, 2]
    hour = 6
    b= minSpeedOnTime(dist, hour)
    print(b)