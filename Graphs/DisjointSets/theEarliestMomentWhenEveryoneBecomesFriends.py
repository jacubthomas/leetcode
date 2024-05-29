from typing import List
from typing import Set

class UnionFind:
    def __init__ (self, size):
        self.numNodes = size
        # initialize the root key list with each node pointing to itself - as its own root
        self.root = [i for i in range(size)]
        # initialize the rank list, for reference in keeping the tree height minimal
        self.rank = [i for i in range(size)]

    # find x's root node and compress the path for all nodes along the way
    def find(self, x: int):
        # x it's own true root, change nothing
        if x == self.root[x]:
            return x
        # x is not it's own root
        # x's parent, grandparent, etc. may not be their own root
        # update x's heritage to all point to one true root
        self.root[x] = self.find(self.root[x])

        # return the true root
        return self.root[x]
    
    # unite two connected nodes, pointing them to one true root
    # then check all nodes' true root
    # when all nodes point to same true root, everyone is acquainted
    # return true if all acquainted, false otherwise
    def union(self, i: int, j: int) -> bool:
        # gather each root for the nodes to be united
        iRoot, jRoot = self.find(i), self.find(j)
        # the nodes do not yet point to the same true root
        # unite the nodes on one true root and do so by the connecting the shortest possible tree
        if (iRoot != jRoot):
            # left tree is bigger than right, tree height does not need to increase on connect
            if self.rank[iRoot] > self.rank[jRoot]: 
                self.root[jRoot] = iRoot
            # right tree is bigger than left, tree height does not need to increase on connect
            elif (iRoot != jRoot and self.rank[iRoot] < self.rank[jRoot]): 
                self.root[iRoot] = jRoot
            # left and right tree are same height, tree height will increase by one on connect
            else:
                self.root[jRoot] = iRoot
                self.rank[iRoot] += 1
        
        # check for all connected
        s = set()
        for j in range(self.numNodes):
            s.add(self.find(j))
        if len(s) == 1:
            return True
        return False

class Solution:
    def earliestAcq (self, logs: List[List[int]], n: int) -> int:
        # we have to consider entire length of logs in the case everyone is not acquainted
        numLogs = len(logs)
        # we cannot assume the logs are sorted on time, do so now
        logs = sorted(logs, key=lambda x: x[0])
        # connect nodes one log at a time and check for all connected
        uf = UnionFind(n)
        for i in range(0, numLogs):
            allConnected = uf.union(logs[i][1], logs[i][2])
            # short circuit here if everyone is acquainted
            if allConnected:
                return logs[i][0]
        # everyone is not acquainted 
        return -1
    

sol = Solution()
print (sol.earliestAcq([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], 4)) # 3
print (sol.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6)) # 20190301
print (sol.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190312,1,2],[20190322,4,5],[20190301,0,3]], 6)) # 20190301