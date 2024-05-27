from typing import List
from typing import Set

'''
Number of Provinces

Solution
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''

class Solution:

    # are these vertices actually connected from input 2D-array
    def connected(self, 
                  isConnected: List[List[int]], 
                  i: int, 
                  j: int):
        return (isConnected[i][j] and isConnected[j][i])
    
    def findRoot(self, isConnected: List[List[int]], rootKey: List[int], x: int):
        # When vertex has it's own root
        if x == rootKey[x]:
            return x
        
        # Path compression
        # Update trail of keys leading to root to all point directly to root
        rootKey[x] = self.findRoot(isConnected, rootKey, rootKey[x])
        return rootKey[x]

        # Without Path Compression
        # return self.findRoot(isConnected, rootKey, rootKey[x])
            

    def union(self, isConnected: List[List[int]], n: int) -> List[int]:
        '''
        Array used to track unique sets
        A city can point to itself in this array, as a province root
        Or it can point to another city
        That other city can be a province root, or it can be another link in the chain for a province
        '''
        # initialize rootKey array with n-cities each pointing to their own index
        rootKey = [i for i in range(n)]

        # initialize the rankKey array, to help connect n-cities in a tree with shorter height
        rankKey = [1 for i in range(n)]
        
        # compare all cities against each other
        for i in range(n):
            for j in range (n):
                iRoot = self.findRoot(isConnected, rootKey, i)
                jRoot =  self.findRoot(isConnected, rootKey, j)
                if (self.connected(isConnected,i,j)         # are these vertices actually connected from input 2D-array
                    and iRoot != jRoot):                    # are these vertices recognized as connected by our algorithm
                    # union by rank, keep the tree height short
                    if rankKey[i] > rankKey[j]:
                        rootKey[jRoot] = iRoot
                    elif rankKey[j] > rankKey[i]:
                        rootKey[iRoot] = jRoot
                    else:
                        rootKey[jRoot] = iRoot
                        rankKey[iRoot] += 1
        return rootKey

    def fastUnionByCount(self, isConnected: List[List[int]], n: int) -> int:
        '''
        Array used to track unique sets
        A city can point to itself in this array, as a province root
        Or it can point to another city
        That other city can be a province root, or it can be another link in the chain for a province
        '''
        # initialize rootKey array with n-cities each pointing to their own index
        rootKey = [i for i in range(n)]

        # initialize the rankKey array, to help connect n-cities in a tree with shorter height
        rankKey = [1 for i in range(n)]

        # we count down as we connect provinces so we don't have to do processing of the rootKey later
        count = n
        
        # compare all cities against each other
        for i in range(n):
            for j in range (n):
                iRoot = self.findRoot(isConnected, rootKey, i)
                jRoot =  self.findRoot(isConnected, rootKey, j)
                if (self.connected(isConnected,i,j)         # are these vertices actually connected from input 2D-array
                    and iRoot != jRoot):                    # are these vertices recognized as connected by our algorithm
                    count -= 1
                    # union by rank, keep the tree height short
                    if rankKey[i] > rankKey[j]:
                        rootKey[jRoot] = iRoot
                    elif rankKey[j] > rankKey[i]:
                        rootKey[iRoot] = jRoot
                    else:
                        rootKey[jRoot] = iRoot
                        rankKey[iRoot] += 1
        return count
    

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        # rootKey = self.union(isConnected, n)
        count = self.fastUnionByCount(isConnected, n)

        # readySeto = set()

        # # Only add true roots, not parents, to set
        # # Given the nature of sets, only distinct root values will be represented
        # for x in rootKey:
        #     readySeto.add(self.findRoot(isConnected, rootKey, x))
        
        # # With path compression, only true roots will be in rootKey
        # for x in rootKey:
        #     readySeto.add(x)

        # return len(readySeto)
        return count
    


s = Solution()

isConnected1V_1P = [[1]]
isConnected2V_1P = [[1,1], [1,1]]
isConnected2V_2P = [[1,0], [0,1]]
isConnected4V_1P = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]

print (s.findCircleNum(isConnected = isConnected1V_1P))
print (s.findCircleNum(isConnected = isConnected2V_1P))
print (s.findCircleNum(isConnected = isConnected2V_2P))
print (s.findCircleNum(isConnected = isConnected4V_1P))