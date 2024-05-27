from typing import List

'''
Graph Valid Tree

Solution
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Constraints:
1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
'''

class UnionFind:
    def __init__(self, size):
        # initialize the root key list with each node pointing to itself - as its own root
        self.root = [i for i in range(size)]
        # initialize the rank list, for reference in keeping the tree height minimal
        self.rank = [1 for i in range(size)]

    # find x's root node and compress the path for all nodes along the way
    def find(self, x: int) -> int:
        # x it's own true root, change nothing
        if self.root[x] == x:
            return x
        
        # x is not it's own root
        # x's parent, grandparent, etc. may not be their own root
        # update x's heritage to all point to one true root
        self.root[x] = self.find(self.root[x])

        # return the true root
        return self.root[x]
    
    # unite two connected nodes, pointing them to one true root
    # where they already point to the same root, there is a cycle
    # when there is a cycle, the input does not represent a valid tree
    def union(self, i: int, j: int) -> bool:

        # gather each root for the nodes to be united
        iRoot = self.find(i)
        jRoot = self.find(j)

        # the nodes do not yet point to the same true root
        # unite the nodes on one true root and do so by the connecting the shortest possible tree
        if iRoot != jRoot:
            # left tree is bigger than right, tree height does not need to increase on connect
            if self.rank[i] > self.rank[j]:
                self.root[jRoot] = iRoot
            # right tree is bigger than left, tree height does not need to increase on connect
            elif self.rank[i] < self.rank[j]:
                self.root[iRoot] = jRoot
            # left and right tree are same height, tree height will increase by one on connect
            else:
                self.root[jRoot] = iRoot
                self.rank[iRoot] += 1
        # A cycle has been detected and the input cannot construct a valid tree
        elif (iRoot == jRoot):
            return False
        
        return True
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # handle base and edge case inputs
        # where input is 1 node, it should not have any connections
        # where input is > 1 node, constructing a valid tree necessitates edges to connect nodes
        if (len(edges) == 0 and n != 1):
            return False
        
        # unite all nodes in inputs by constructing a tree
        # if the tree is invalid, we know the input is bad
        uf = UnionFind(n)
        for i in range(0,len(edges)):
            if uf.union(edges[i][0], edges[i][1]) == False:
                return False
        
        # verify that we have 1 tree with one pure root
        firstRoot = uf.find(uf.root[0])
        for i in uf.root:
            # we have multiple valid trees, but not 1 valid tree
            if uf.find(i) != firstRoot:
                return False
        return True

s = Solution()
print (s.validTree(1,[]))                         # True
print (s.validTree(3, [[1,0],[2,0]]))             # True
print (s.validTree(3, [[1,0],[0,2],[2,1]]))       # False
print (s.validTree(4, [[0,1], [2,3]]))            # False
print (s.validTree(4,[[0,1],[2,3],[1,2]]))        # True
