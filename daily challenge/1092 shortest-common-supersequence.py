"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.



Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation:
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""


# start with lcs

def shortestCommonSupersequence(str1: str, str2: str) -> str:
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m+1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:# Match case
                    dp[i][j] = 1 + dp[i-1][j - 1]
                else:  # No match case
                    dp[i][j] = max(dp[i-1][j], dp[i][j - 1])
        return dp

    dp=longestCommonSubsequence(str1, str2)
    i= len(str1)
    j= len(str2)
    lcs=[]
    while i>0 and j>0:
        if str1[i-1] ==str2[j-1]:
            lcs.append(str1[i-1])
            i-=1
            j-=1
        elif dp[i-1][j] > dp[i][j-1]:
            lcs.append(str1[i-1])
            i -=1
        else:
            lcs.append(str2[j-1])
            j -=1
    while i>0:
        lcs.append(str1[i-1])
        i -=1
    while j > 0:
        lcs.append(str2[j - 1])
        j -=1
    return "".join(lcs[::-1])


if __name__ == '__main__':
    str1 = "abac"
    str2 = "cab"
    str1 = "abcde"
    str2 = "ace"
    c=shortestCommonSupersequence(str1,str2)
    print(c)

"""
bbbaaababbb
bbbaaababbb
"""