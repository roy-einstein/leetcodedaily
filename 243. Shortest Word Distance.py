"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.



Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1


Constraints:

2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
"""

from typing import List

def shortestDistance(wordsDict: List[str], word1: str, word2: str) -> int:
    i, j =-1,-1
    ans = float("inf")

    for w in range(len(wordsDict)):
        if wordsDict[w] == word1:
            i =w
        if wordsDict[w] == word2:
            j =w
        if i != -1 and j != -1:
            ans = min(ans, abs(i-j))
    return ans

