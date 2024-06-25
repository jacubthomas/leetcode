# This problem definition is misleading on the site
# The input appears as an adjacency list, but they do not give you that; rather a starting node
'''
Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node 
{
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node
with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an
adjacency list. An adjacency list is a collection of unordered lists used to represent a finite graph. Each
list describes the set of neighbors of a node in the graph. The given node will always be the first node 
with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
'''

# from typing import Dict
from typing import List
# from typing import Set
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class DFS:
    def __init__(self):
        # Build out Adjacency Map for ease of readability, marking Nodes as visited
        # Also, getting those node's neighbors by references
        self.adjacencyMap = dict()

    def traverseGraphEntireAndDeepCopy(self, node: Optional['Node']) -> Optional['Node']:
        # Create a new node, instead of shallow-referencing the input node
        deepCopyNode = Node(node.val, None)
        self.adjacencyMap[node.val] = deepCopyNode

        # Create deep-copy Nodes for each of this node's neighbors and add each as neighbor
        # Do not waste time exploring nodes previously explored, just add them to this node
        for x in node.neighbors:
            if x.val not in self.adjacencyMap:
                deepCopyNeighbor = self.traverseGraphEntireAndDeepCopy(x)
            deepCopyNode.neighbors.append(self.adjacencyMap[x.val])

        return deepCopyNode      

class Solution:

    def __init__ (self):
        # Create DFS class algorithm to aid deep copying the passed in graph
        self.dfs = DFS()

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # Sanity check, negliglible input
        if node is None:
            return None

        # Traverse graph and deep copy all nodes through neighbors
        resultNode = self.dfs.traverseGraphEntireAndDeepCopy(node)
        return resultNode
    
    # Helper to visualize the resulting graph
    def printAdjacencyMap(self) -> None:
        for x in self.dfs.adjacencyMap.keys():
            neighborString = ', '.join([str(y.val) for y in self.dfs.adjacencyMap[x].neighbors])
            print (f'node - val: {x}, neighbors: {neighborString}')

s = Solution()

# How example 1 above will actually be passed in
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors.append(n2)
n1.neighbors.append(n4)
n2.neighbors.append(n1)
n2.neighbors.append(n3)
n3.neighbors.append(n2)
n3.neighbors.append(n4)
n4.neighbors.append(n1)
n4.neighbors.append(n3)
s.cloneGraph(n1)
print (s.printAdjacencyMap())