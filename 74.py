from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    l=0
    r= m*n -1
    while l<=r:
        mid = (l+r)//2
        i, j = mid //n , mid%n
        if target == matrix[i][j]:
            return True
        elif target > matrix[i][j]:
            l = mid+1
        else:
            r = mid -1
    return False


if __name__ == "__main__":
    matrix =[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(searchMatrix(matrix,3))