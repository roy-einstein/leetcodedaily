from typing import List
def maxConsecutive(bottom: int, top: int, special: List[int]) -> int:
    longest = 0
    s= {i for i in range(bottom, top+1) if i not in special}
    for num in s:
        if num-1 not in s:
            cur = 1
            while num + 1 in s and num not in special:
                cur += 1
                num += 1
            longest = max(longest, cur)
    return longest

if __name__ == "__main__":
    bottom = 2
    top = 9
    special = [4, 6]
    # bottom = 6
    # top = 8
    # special = [7, 6, 8]
    b = maxConsecutive(bottom, top, special)
    print(b)