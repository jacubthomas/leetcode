from typing import List

class BFS:
    def __init__ (self, n, edges: List[List[int]], source: int, destination: int):
        # Capture all problem inputs for reference
        self.n = n
        self.edges = edges
        self.source = source
        self.destination = destination
        # Ease any given node's connectivity within the graph
        self.adjacencyList = [set() for i in range(self.n)]
        # Help prevent redundant, wasted compute
        self.visited = [0 for i in range(self.n)]
        # We will assume the input always has a valid source, where we will always start
        self.visited[self.source] = 1

        # Graph is bidirectional
        for edge in edges:
            self.adjacencyList[edge[0]].add(edge[1])
            self.adjacencyList[edge[1]].add(edge[0])

    def findAnyValidPath(self, currentPath: List[int]) -> bool:
        # Ease of readability
        currentNode = currentPath[len(currentPath)-1]

        # We made it from source -> destination
        if currentNode == self.destination:
            return True
        
        # Consider all neighbors in FIFO order
        queue = []
        for edge in self.adjacencyList[currentNode]:
            if self.visited[edge] == 0:
                queue.append(edge)

        # Delve into each neighbor
        while len(queue) > 0:
            # Get node from neighbor queue
            edge = queue.pop(0)
            # Temporarily update path to include this node
            currentPath.append(edge)
            # Mark it as visited so we don't waste compute exploring it again
            self.visited[edge] = 1
            # Recurse to next level of tree
            result = self.findAnyValidPath(currentPath)
            # Check if we found a path - short circuit when we do
            if result == True:
                return True
            # Nothing on this node's path, let's explore other nodes
            currentPath.pop(len(currentPath)-1)

        # We found no such path and have no more options
        return False

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        bfs = BFS(n, edges, source, destination)
        return bfs.findAnyValidPath([source])
    
s = Solution()

# print(s.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2)) # True
# print(s.validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5)) # False
print(s.validPath(10, [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]], 7, 5)) 