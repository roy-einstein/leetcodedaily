"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    m,n = len(matrix), len(matrix[0])
    up,down,right, left =0,1,2,3

    up_wall, down_wall, right_wall, left_wall = 0,m,n,-1
    ans = []
    i, j =0,0
    direction = right
    while len(ans) != (m*n):
        if direction == right:
            while j<right_wall:
                ans.append(matrix[i][j])
                j +=1
            right_wall -=1
            i +=1
            j -=1
            direction = down
        if direction == down:
            while i<down_wall:
                ans.append(matrix[i][j])
                i +=1
            i -=1
            j -=1
            down_wall -=1
            direction =left
        if direction == left:
            while j > left_wall:
                ans.append(matrix[i][j])
                j -=1
            j +=1
            i -=1
            left_wall +=1
            direction = up
        if direction == up:
            while i > up_wall:
                ans.append(matrix[i][j])
                i -=1
            i +=1
            j +=1
            up_wall +=1
            direction =right
    return ans


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = spiralOrder(matrix)
    print(b)