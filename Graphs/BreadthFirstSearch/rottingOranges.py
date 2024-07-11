'''
You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.

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
'''

from typing import List

class BFS:
    def __init__ (self, grid: List[List[int]]):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.goodOranges = []
        self.maxTimeToRot = 0

    # We will be BFS traversing from all good oranges to the nearest rotten orange
    # We don't need to BFS traverse for empty squares or rotten squares
    def findAllGoodOranges(self) -> None:
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    self.goodOranges.append([i,j])

    # Add valid steps away from a given coordinate to a list result
    def getAllValidSteps(self, coordinate: List[int], visited: List[List[int]]) -> List[List[int]]:
        steps = []
        if (coordinate[0] > 0 and                               # can step left
            visited[coordinate[0]-1][coordinate[1]] == 0 and    # left has not been visited
            self.grid[coordinate[0]-1][coordinate[1]] != 0):    # left has an orange 
            steps.append([coordinate[0]-1, coordinate[1]])
        if (coordinate[1] > 0 and                               # can step up
            visited[coordinate[0]][coordinate[1]-1] == 0 and    # up has not been visited
            self.grid[coordinate[0]][coordinate[1]-1] != 0):    # up has an orange 
            steps.append([coordinate[0], coordinate[1]-1])
        if (coordinate[0] < self.m - 1 and                      # can step right
            visited[coordinate[0]+1][coordinate[1]] == 0 and    # right has not been visited
            self.grid[coordinate[0]+1][coordinate[1]] != 0):    # right has an orange 
            steps.append([coordinate[0]+1, coordinate[1]])
        if (coordinate[1] < self.n - 1 and                      # can step down
            visited[coordinate[0]][coordinate[1]+1] == 0 and    # down has not been visited
            self.grid[coordinate[0]][coordinate[1]+1] != 0):    # down has an orange 
            steps.append([coordinate[0],coordinate[1]+1])
        return steps

    # BFS traverse from a good orange to the nearest rotten orange
    # Return false if no rotten connected
    def traverseToRottenOrange (self, coordinate: List[int]) -> bool:

        # Don't reevaluate squares we've already visited
        visited = [[0 for _ in range(self.n)] for _ in range(self.m)]

        # Traverse grid until we find a rotten orange or have evaluated all connected squares
        q = self.getAllValidSteps(coordinate, visited)
        step = 0
        while len(q) > 0:
            # Helps track the level of traversal, or steps we take towards a rotten orange
            size = len(q)
            step += 1
            for _ in range(size):
                neighbor = q.pop(0)
                visited[neighbor[0]][neighbor[1]] = 1
                if self.grid[neighbor[0]][neighbor[1]] == 2:
                    if step > self.maxTimeToRot:
                        self.maxTimeToRot = step
                    return True
                q += self.getAllValidSteps(neighbor, visited)

        # No rotten orange connected to a healthy orange
        return False
    
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs = BFS(grid)
        bfs.findAllGoodOranges()
        for goodOrange in bfs.goodOranges:
            if bfs.traverseToRottenOrange([goodOrange[0], goodOrange[1]]) == False:
                return -1
        return bfs.maxTimeToRot

s = Solution()
print (s.orangesRotting([[0,1],[0,0],[2,0]])) # -1
print (s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
print (s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
print (s.orangesRotting([[1,1,1,1],[0,0,0,1],[0,0,0,2]])) # 5
print (s.orangesRotting([[1,1,1,1],[0,0,0,1],[2,1,1,1]])) # 8
