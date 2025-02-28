"""
given string = ABCD ->
zig zag number is 2
visual
A  C
B  D

output = ACBD
"""

def printZigZag(str,n):
    if n==1:
        return str
    l=len(str)
    arr = ["" for _ in range(n)]
    row = 0
    for i in range(l):
        arr[row] +=str[i]
        if row == n-1:
            down=False
        elif row == 0:
            down =True
        if down:
            row +=1
        else:
            row -=1
    print(arr)
    return "".join(arr)

if __name__ == "__main__":
    str = "ABCD"
    n=2
    b=printZigZag(str,n)
    print(b)