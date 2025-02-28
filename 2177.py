from typing import List
def sumOfThree(num: int) -> List[int]:
    last_digit = num // 3 +1
    ans = []
    if last_digit < 2:
        return []
    n = last_digit + last_digit - 1 + last_digit - 2
    if n == num:
        ans = [last_digit, last_digit - 1, last_digit - 2]
    return ans

if __name__ == "__main__":
    num =33
    b=sumOfThree(num)
    print(b)