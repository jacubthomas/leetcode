from typing import List
from typing import Set

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
    def union(self, i: int, j: int):

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
    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # handle base and edge case inputs
        # where there are no edges between nodes, the number of nodes is the number connected components
        if (len(edges) == 0):
            return n
        
        # unite all nodes in inputs by constructing trees
        # each tree of nodes represents one connected component
        uf = UnionFind(n)
        for i in range(0,len(edges)):
            uf.union(edges[i][0], edges[i][1])
        
        # verify add each tree tree to set
        # given that sets inherently store distinct elements
        # the size of the set will be our solution
        readySeto = set()
        for i in uf.root:
            readySeto.add(uf.find(i))
        
        return len(readySeto)

s = Solution()

print (s.validTree(3, [[1,0],[2,0]]))             # 1
print (s.validTree(3, [[1,0],[0,2],[2,1]]))       # 1
print (s.validTree(4, [[0,1], [2,3]]))            # 2
print (s.validTree(4,[[0,1],[2,3],[1,2]]))        # 1
print (5, [[0,1],[1,2],[3,4]])                    # 2