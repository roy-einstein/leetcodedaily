"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from typing import List

def numIslands(grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if 0 <= i < m and 0 <= j < n and grid[i][j] != '0':
            grid[i][j] = '0'
            dfs(i + 1, j)  # move to down
            dfs(i, j + 1)  # move to right
            dfs(i - 1, j)  # move up
            dfs(i, j - 1)  # move left
        else:
            return

    no_islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                no_islands += 1
                dfs(i, j)

    return no_islands

if __name__ == "__main__":
    grid =[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    b = numIslands(grid)
    print(b)