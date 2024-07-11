from typing import List

class BFS:
    def __init__ (self, grid: List[List[int]]):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.goodOranges = []
        self.maxTimeToRot = 0

    def findAllGoodOranges(self) -> None:
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    self.goodOranges.append([i,j])

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

    def traverseToRottenOrange (self, coordinate: List[int]) -> bool:
        visited = [[0 for _ in range(self.n)] for _ in range(self.m)]

        q = self.getAllValidSteps(coordinate, visited)
        step = 0
        while len(q) > 0:
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
