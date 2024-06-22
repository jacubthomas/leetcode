from typing import List

# Simple Union-Find structure (by rank with Path Compression)
# Helps determine which vertices share an edge in an efficient manner
class UnionFind:
    def __init__ (self, size: int):
        self.size = size
        self.root = [i for i in range(size)]
        self.rank = [1 for x in range(size)]

    # Two vertices share an edge they point to the same root
    def isConnected (self, nodeX: int, nodeY: int) -> bool:
        return self.find(nodeX) == self.find(nodeY)
    
    # Find a vertex's root node, and path compress along the way to reduce compute
    def find (self, node: int) -> int:
        # A vertex which points to itself is a true root node
        if node == self.root[node]:
            return node
        
        # Recursively search this node's parent a pure root node point this node
        # Path Compress - update this node to directly point to true root for efficiency
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    # Union by rank, so we keep the connected vertex trees short!
    def union (self, nodeX: int, nodeY: int):
        # Gather each vertex's true root
        rootX, rootY = self.find(nodeX), self.find(nodeY)
        # Not already connected, do so now
        if rootX != rootY:
            # Vertex X's root tree is taller, so pointing vertex Y's root tree at it will not grow the tree
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            # Vertex Y's root tree is taller, so pointing vertex X's root tree at it will not grow the tree
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            # Arbitrarily point Y's root at X's root
            # Since both root height's are equal, X's root tree will need to grow by 1
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

class DFS:
    def __init__ (self, size: int, edges: List[List[int]]):
        self.size = size
        self.edges = edges
        self.visited = [0 for i in range(size)]
        self.connectedVerticesPerVertex = [set() for _ in range(size)]

    def mapOutDirectlyConnectedVerticesPerVertex(self):
        for edge in self.edges:
            self.connectedVerticesPerVertex[edge[0]].add(edge[1])
            self.connectedVerticesPerVertex[edge[1]].add(edge[0])

    def findValidPath(self, 
                    source: int, 
                    destination: int, 
                    pathThusFar: List[int]) -> List[int]:
        # For readability's sake, pull out where we are from the current proposed solution path
        currentVertex = pathThusFar[len(pathThusFar)-1]

        # Path is valid, bottom of recursion
        if destination == currentVertex:
            return pathThusFar

        # Since we are only concerned with finding 1 valid path, we only need to explore vertices once
        # Marking them as visited will make things faster
        self.visited[currentVertex] = 1
        
        # Consider all unexplored edges from this vertex
        for v in self.connectedVerticesPerVertex[currentVertex]:
            # Don't waste time exploring vertices we've already evaluated
            if self.visited[v] == 0:
                # Temporarily append vertex on other side of this edge to solution path
                pathThusFar.append(v)
                # Recursively DFS
                result = self.findValidPath(source, destination, pathThusFar)
                # Short circuit if we found a valid path
                if result != None:
                    return result
                # Pop off trialed vertex from solution path, as it did not lead to destination
                pathThusFar.pop()
        # No destination found along connected edges from this vertex
        return None


class UnionFindSolution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # UnionFind structure will help determine if vertices are connected via edge in an efficient manner
        uf = UnionFind(n)
        # First, we need to feed it all the edges in the graph
        for edge in edges:
            uf.union(edge[0], edge[1])
        
        # There is a at least one path if these nodes are connected to the same root with UF structure
        return (uf.find(source) == uf.find(destination))

class DepthFirstSearchSolution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # Setup our Depth-First Search algorithm class
        dfs = DFS(n, edges)
        dfs.mapOutDirectlyConnectedVerticesPerVertex()
        
        # Mark the source as visited, so we don't waste time reconsidering it
        dfs.visited[source] = 1

        # true, if any path is returned
        return (dfs.findValidPath(source,destination, [source]) != None)

ufs = UnionFindSolution()
print (ufs.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)) # True
print (ufs.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) # False
print (ufs.validPath(10, [[2,9],[7,8],[5,9],[7,2],[3,8],[2,8],[1,6],[3,0],[7,0],[8,5]],1,0)) # False

dfs = DepthFirstSearchSolution()
print (dfs.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)) # True
print (dfs.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) # False
print (dfs.validPath(10, [[2,9],[7,8],[5,9],[7,2],[3,8],[2,8],[1,6],[3,0],[7,0],[8,5]],1,0)) # False