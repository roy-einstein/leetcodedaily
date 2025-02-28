"""
A taxi can take multiple passengers to the railway station at the same time.On the way back to the starting point,the taxi driver may pick up additional passengers for his next trip to the airport.A map of passenger location has been created,represented as a square matrix.

The Matrix is filled with cells,and each cell will have an initial value as follows:

A value greater than or equal to zero represents a path.
A value equal to 1 represents a passenger.
A value equal to -1 represents an obstruction.
The rules of motion of taxi are as follows:

The Taxi driver starts at (0,0) and the railway station is at (n-1,n-1).Movement towards the railway station is right or down,through valid path cells.
After reaching (n-1,n-1) the taxi driver travels back to (0,0) by travelling left or up through valid path cells.
When passing through a path cell containing a passenger,the passenger is picked up.once the rider is picked up the cell becomes an empty path cell.
If there is no valid path between (0,0) and (n-1,n-1),then no passenger can be picked.
The goal is to collect as many passengers as possible so that the driver can maximize his earnings.
For example consider the following grid,

0      1
-1     0

Start at top left corner.Move right one collecting a passenger. Move down one to the destination.Cell (1,0) is blocked,So the return path is the reverse of the path to the airport.All Paths have been explored and one passenger is collected.

Returns:

Int:maximum number of passengers that can be collected.
Sample Input 0

4  -> size n = 4
4 -> size m = 4
0 0 0 1 -> mat
1 0 0 0
0 0 0 0
0 0 0 0
Output 0

2
Explanation 0

The driver can contain a maximum of 2 passengers by taking the following path
(0,0) → (0,1) → (0,2) → (0,3) → (1,3) → (2,3) → (3,3) → (3,2) → (3,1) → (3,0) → (2,0) → (1,0)  → (0,0)

Sample Input 1

STD IN                  Function

————              ————-

   3     →  size  n=3
   3    →  size m=3
   0 1 -1 → mat
   1 0 -1
   1 1 1
Sample Output 1

5
Explanation 1

The driver can contain a maximum of 5 passengers by taking the following path
(0,0) → (0,1) → (1,1) → (2,1) → (2,2) → (2,1) → (2,0) → (1,0) → (0,0)
"""
from collections import defaultdict
from os.path import curdir


def solve(matrix):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    m, n = len(matrix), len(matrix[0])
    visited = set()
    cur_sum =0
    def dfs(i, j, visted, cur_sum):
        visted.add((i, j))
        if i==m-1 and j ==n-1:
            return cur_sum
        if matrix[i][j] == -1:
            return
        for x, y in directions:
            dx, dy = i+x, j+y
            if 0<=dx<m and 0<=dy<n and (dx,dy) not in visted and matrix[dx][dy]>=0:
                dfs(dx,dy, visted,cur_sum+matrix[dx][dy])
                matrix[dx][dy] = 0


    for i in range(m):
        cur_sum = dfs(i,0, visited,cur_sum)

    for j in range(n):
        cur_sum =dfs(0,j,visited, cur_sum)

    return cur_sum

if __name__ == "__main__":
    """
    0 0 0 1 -> mat
1 0 0 0
0 0 0 0
0 0 0 0
    """
    matrix = [[0,0,0,1], [1,0,0,0],[0,0,0,0], [0,0,0,0] ]
    b=solve(matrix)
    print(b)