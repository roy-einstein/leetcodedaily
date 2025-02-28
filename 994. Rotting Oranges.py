"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from collections import deque
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    m=len(grid)
    n= len(grid[0])
    min_time=0
    q = deque()
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    fresh =0
    for i in range(m):
        for j in range(n):
            if grid[i][j] ==2:
                q.append((i,j,0))
            if grid[i][j] ==1:
                fresh +=1
    if fresh ==0:
        return 0
    while q:
        i, j, t = q.popleft()
        min_time =max(min_time,t)
        for idx, idy in directions:
            dx, dy = idx + i, idy + j
            if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:
                q.append((dx, dy, 1 + t))
                grid[dx][dy] = 2
                fresh -=1

    return min_time if fresh==0 else -1

if __name__ == '__main__':
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    b=orangesRotting(grid)
    print(b)