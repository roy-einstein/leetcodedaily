from collections import defaultdict
from typing import List


def partitionLabels(s: str) -> List[int]:
    d= defaultdict(list)
    for i in range(len(s)):
        if s[i] in d and len(d[s[i]]) <2:
            d[s[i]][-1].append(i)
        else:
            d[s[i]].append([i])
    print(d)

if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    partitionLabels(s)