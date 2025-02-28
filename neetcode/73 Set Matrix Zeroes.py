"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

"""
logic 
1. copy a matrix and do reverse search 
keep the index handy marke the row index and column index keep marking the row values or column value to be zero
"""
from typing import List
def setZeroes(matrix: List[List[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    row_index = [1] * m
    column_index = [1] * n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_index[i] =0
                column_index[j] =0
    for i in range(m):
        if row_index[i] == 0:
            matrix[i] =[0]*n
    for j in range(n):
        if column_index[j] == 0:
            for i in range(m):
                matrix[i][j] =0

if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(matrix)
    print(matrix)
