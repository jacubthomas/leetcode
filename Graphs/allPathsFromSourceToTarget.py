from typing import List
from typing import Dict
class DFS:
    def __init__ (self, graph: List[List[int]]):
        self.visited = [0 for x in range(len(graph))]
        # For determining which vertices are connected to each vertex
        self.adjacenyMap = {}
        for x in range(len(graph)):
            self.adjacenyMap[x] = graph[x]
        # For storing the resulting path permutations from source to destination
        self.solutionPaths = []

    def allPathsFromSourceToDestination(self, source: int, destination: int, currentPath: List[int]) -> None:
        # For ease of readability
        currentVertex = currentPath[len(currentPath)-1]

        # Temporarily mark this vertex as visited so we don't recurse onto it
        self.visited[currentVertex] = 1

        # When we reach the destination, append shallow copy of result into solution
        # Unmark this vertex as visited, as another path may lead through here - and we want ALL paths
        if currentVertex == destination:
            self.solutionPaths.append(currentPath.copy())
            self.visited[currentVertex] = 0
            return
        
        # Explore all adjacent vertices
        for x in self.adjacenyMap[currentVertex]:
            if self.visited[x] == 0:
                # Temporarily update the path with this vertex
                currentPath.append(x)
                # Recursively trace out the connected vertex
                self.allPathsFromSourceToDestination(source, destination, currentPath)
                # Undo this most recently traced vertex and possibly consider another
                currentPath.pop()

        # Unmark this vertex as visited, as another path may lead through here - and we want ALL paths
        self.visited[currentVertex] = 0

        

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dfs = DFS(graph)
        dfs.allPathsFromSourceToDestination(0, len(graph)-1, [0])
        return dfs.solutionPaths


s = Solution()

print (s.allPathsSourceTarget([[1,2],[3],[3],[]]))
print (s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))