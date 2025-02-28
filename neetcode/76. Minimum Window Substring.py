"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""
from collections import Counter, defaultdict


def minWindow(s: str, t: str) -> str:
    lt = len(t)
    ls = len(s)
    counter_t  = Counter(t)
    left, right = 0, 0
    counter_search = defaultdict(int)
    count =0
    longest =float('inf')
    min_window =''
    for right in range(ls):
        counter_search[s[right]] +=1
        if s[right] in counter_t:
            if counter_search[s[right]] <= counter_t[s[right]]:
                count +=1
        while left <= right and count == lt:
            if right-left +1 < longest:
                longest = right-left+1
                min_window = s[left:right+1]
            counter_search[s[left]] -=1

            if s[left] in counter_t and counter_search[s[left]] < counter_t[s[left]]:
                count -=1
            left +=1

    return min_window


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    s='ab'
    t='a'
    print(minWindow(s, t))