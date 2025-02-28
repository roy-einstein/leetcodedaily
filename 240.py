from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        l, r =0, n -1
        while l<=r:
            mid = (l+r) //2
            if target == matrix[i][mid]:
                return True
            elif target > matrix[i][mid]:
                l = mid+1
            else:
                r = mid-1
    return False

