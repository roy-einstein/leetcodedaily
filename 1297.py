from collections import defaultdict


def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    l,r=0,minSize
    n= len(s)
    d= defaultdict(int)
    while l<n-minSize+1:
        while minSize<=r-l<=maxSize and len(set(s[l:r])) <= maxLetters and r<=n:
            d[s[l:r]] +=1
            r +=1
        l +=1
        r =minSize+l
    return max(d.values())

if __name__ == "__main__":
    s = "aababcaab"
    maxLetters = 2
    minSize = 3
    maxSize = 4
    b=maxFreq(s,maxLetters,minSize,maxSize)
    print(b)
