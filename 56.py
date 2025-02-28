from typing import List
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x :x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = [merged[-1][0], max(merged[-1][1],interval[1])]
    return merged

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1, 4], [4, 5]]
    m= merge(intervals)
    print(m)