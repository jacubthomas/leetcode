from typing import List

class BFS:
    def __init__(self, graph: List[List[int]]):
        self.numNodes = len(graph)
        self.graph = graph
        self.visited = [0 for i in range(self.numNodes)]
        self.visited[0] = 1
        self.source = 0
        self.target = self.numNodes - 1
        self.solutionPaths = []

    def findAllPathsFromSourceToTarget(self, currentPath: List[int]):
        # Ease of readability
        currentNode = currentPath[len(currentPath)-1]

        # Found another valid path to target, keep a copy for end result
        if currentNode == self.target:
            self.solutionPaths.append(currentPath.copy())

        queue = []

        for neighbor in self.graph[currentNode]:
            if self.visited[neighbor] == 0:
                queue.append(neighbor)
        
        while len(queue) > 0:
            neighbor = queue.pop(0)
            self.visited[neighbor] = 1
            currentPath.append(neighbor)
            self.findAllPathsFromSourceToTarget(currentPath)
            self.visited[neighbor] = 0
            currentPath.pop(len(currentPath)-1)

        

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        bfs = BFS(graph)
        bfs.findAllPathsFromSourceToTarget([0])
        return bfs.solutionPaths
    
s = Solution()

print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))