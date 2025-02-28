"""
There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and a.length < b.length.
Example 1:

Input: ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:

Input: ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possibile solution is "hernf"
Constraints:

The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100
"""
from collections import defaultdict
from typing import List

def foreignDictionary(words: List[str]) -> str:
    d= defaultdict(set)
    d = {c: set() for word in words for c in word}
    for i in range(len(words)-1):
        w1, w2, = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                d[w1[j]].add(w2[j])
                break
    # unvisited =0
    # visiting =1
    # visited =2
    # states = [unvisited] * len(words)

    # above method fails because indices can't slice, using same apprach using dict

    visited = {}  # False if not visited, #True in the Path
    res = []
    def dfs(c):
        if c in visited:
            return visited[c]
        # if states[c] == visited: return True
        # if states[c] == visiting: return False

        visited[c] = True
        # states[c] = visiting
        for nei in d[c]:
            if dfs(nei):
                return True
        res.append(c)
        visited[c] = False
        # states[c] = visited

    for c in d:
        if dfs(c):
            return ""
    res.reverse()
    return "".join(res)
if __name__== "__main__":
    words = ["hrn","hrf","er","enn","rfnn"]
    b=foreignDictionary(words)
    print(b)