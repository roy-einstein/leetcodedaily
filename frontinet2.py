from collections import defaultdict


def getAlphabeticallyMinimalString(s, arr, brr):
    # Write your code here
    s = list(s)
    n = len(s)

    graph = defaultdict(list)
    for i in range(len(arr)):
        graph[arr[i]].append(brr[i])
        graph[brr[i]].append(arr[i])

    visited = set()

    def dfs(node, i, ch):
        visited.add(node)
        i.append(node)
        ch.append(s[node])
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei, i, ch)

    for i in range(n):
        if i not in visited:
            idx = []
            ch = []
            dfs(i, idx, ch)

            idx.sort()
            ch.sort()
            for dx, dch in zip(idx, ch):
                s[dx] = dch
    return "".join(s)

def getAlphabeticallyMinimalString(s, arr, brr):
    # Write your code here
    s = list(s)
    n = len(s)

    graph = defaultdict(list)
    for i in range(len(arr)):
        graph[arr[i]].append(brr[i])
        graph[brr[i]].append(arr[i])

    visited = [False]*n
    s=list(s)

    def dfs(start):
        stk=[start]
        idx=[]
        ch=[]
        while stk:
            node = stk.pop()
            if visited[node]:
                continue
            visited[node] = True
            idx.append(node)
            ch.append(s[node])
            for nei in graph[node]:
                if not visited[nei]:
                    stk.append(nei)
        return idx, ch

    for i in range(n):
        if not visited[i]:
            idx, chr = dfs(i)

            idx.sort()
            chr.sort()

            for dx, dch in zip(idx, chr):
                s[dx] = dch
    return "".join(s)

if __name__ == '__main__':
    s="acb"
    arr = [0,0]
    brr = [1,2]
    s = "acbde"
    arr = [0, 1, 3]
    brr = [1, 2, 4]

    b= getAlphabeticallyMinimalString(s,arr,brr)
    print(b)