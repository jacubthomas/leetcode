'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] 
and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer 
for Cj / Dj = ?. Return the answers to all queries. If a single answer cannot be determined, return -1.0. Note: The
input is always valid. You may assume that evaluating the queries will not result in division by zero and that there 
is no contradiction. Note: The variables that do not occur in the list of equations are undefined, so the answer cannot 
be determined for them.


Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
'''

''' 
Do not simplify input equations
If given (bc / cd), don't assume you have (b / d)

On the other hand,
If given (bc / cd), you can assume you have inverse (cd / bc)
'''

from typing import List
from typing import Tuple

class UnionFind:
    def __init__ (self, equations: List[List[int]], values: List[float]) -> None:
        # Result values for given equations, which define connected variables
        self.values = values
        # Key for telling which groups of variables each variable is connected to
        self.root = {}
        # Each variable's weight or cost of path to its root
        # Say, a -> b -> c, and we know (a/b) = 2, (b/c) = 3, then a's weight is 6
        self.weight = {}

        # Initialize structures so each variable is its own root and has a weight of 1 (because a/a = 1)
        for x in equations:
            self.root[x[0]] = x[0]
            self.weight[x[0]] = 1
            self.root[x[1]] = x[1]
            self.weight[x[1]] = 1

    # Determines if two variables are connected from given equations
    def isConnected (self, i: str, j: str) -> bool:
        # Gather each variable's root
        iRoot, jRoot = self.find(i)[0], self.find(j)[0]
        # At least one has no root, it was not provided in the given equations
        if iRoot == None or jRoot == None:
            return False
        # True when both variables belong to the same root group; Otherwise, false
        return iRoot == jRoot

    # Find with path-compression and weight recalcution
    def find (self, x: str) -> tuple[str, float]:
        # Variable is not in our root key, it was not provided in the given equations
        if x not in self.root:
            return None
        # Variable is its own root, return itself and it's weight - bottom of recursion
        elif x == self.root[x]:
            return (x, self.weight[x])
        # Variable is not its own root, recursively call find on this variable's root until true root is returned
        result = self.find(self.root[x])
        # Update this variable's root - Path Compress
        self.root[x] = result[0]
        # Update this variable's weight for the cost to get to root - Weight Recalculation
        self.weight[x] *= result[1]
        # Return this variable's true root and this variable's weight to get to that root
        return (self.root[x], self.weight[x])
    
    # Unite two variables on a single root group and update the cost to get that root
    def union (self, i: str, j: str, valIndex: int) -> None:
        # Gather each variable's root
        iRoot, jRoot = self.find(i)[0], self.find(j)[0]
        # When not in the same root group, update the numerator -> denominator and update cost
        if iRoot != jRoot:
            # Numerator's root -> denominator's root - when we start off, most roots will be their own
            self.root[iRoot] = jRoot
            # The cost for numerator to get to denominator's root will entail
            # The result of the given equation that combines the numerator and denominator
            # Multiplied by the inverse of the numerator and denominator's weight - the path costs the cost of this connection plus denom's connection to root
            # Say, (a/b) = 2.0; a -> a w/ weight 1; b -> c w/ weight 3
            # Now a = 2 * (3/1) = 6
            # a -> b -> c
            # --2--*--3--*--1           
            # Reminding that we multiply costs because our variables are related through cross-multiplication
            self.weight[iRoot] = self.values[valIndex] *  (self.weight[j] / self.weight[i])

''' 
IDEA 1) We can easily tell when variables are connected through disjoint's set, Union-Find.
IDEA 2) We can discern knew variable combinations through cross-multiplication of connected variables
IDEA 3) We can track the relation of variable's relative to their cost to their root 
'''
class Solution:
    def calcEquation(self, 
                    equations: List[List[str]], 
                    values: List[float], 
                    queries: List[List[str]]) -> List[float]:
        
        # We will build the solution string here
        result: List[float] = [0.0] * len(queries)
        
        # Weighted Union-Find
        uf = UnionFind(equations, values)

        # Unite all connected coordinates in WUF structures
        for i in range(len(equations)):
            uf.union(equations[i][0], equations[i][1], i)

        # Assess queries
        for q in range(len(queries)):
            # Gather numerator & denominator roots
            leftRoot, rightRoot = uf.find(queries[q][0]), uf.find(queries[q][1])
            # Case 1: we have at least 1 bad query variable and cannot possibly produce a result
            if leftRoot is None or rightRoot is None:
                result[q] = -1.0
            # Case 2: both query variables are valid, but they are not connected through provided equations
            elif uf.isConnected(leftRoot[0], rightRoot[0]) == False:
                result[q] = -1.0
            # Case 3: both query variables are valid and connected - compute result (q1 / q2)
            else:
                result[q] = uf.weight[queries[q][0]] / uf.weight[queries[q][1]]
        # Return solution set
        return result
    
s = Solution()

print(s.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])) # [6.0, 0.5, -1.0, 1.0, -1.0][6.0, 0.5, -1.0, 1.0, -1.0]
print(s.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])) # [3.75, 0.4, 5.0, 0.2]
print(s.calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]])) # [0.5, 2.0, -1.0, -1.0]
print(s.calcEquation(equations = [["a","b"], ["b","c"] ,["c","d"] , ["d","e"]], values = [2.0, 3.0,4.0, 0.1], queries = [["a","e"]])) # [2.40]
print(s.calcEquation(equations = [["a","b"], ["b","c"] ,["c","d"] , ["e", "d"]], values = [2.0, 3.0,4.0, 0.1], queries = [["a","e"]])) # [240.0]
print(s.calcEquation(equations =[["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], values = [3.0,4.0,5.0,6.0], queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]])) # [360.0, 0.008333333333333333, 20.0, 1.0, -1.0, -1.0]
print(s.calcEquation([["a","b"],["b","c"],["d","e"],["a","d"]],[1.0,2.0,3.0,4.0],[["c","e"]])) # [6.00000]
print(s.calcEquation([["a","b"],["c","b"],["d","b"],["w","x"],["y","x"],["z","x"],["w","d"]], [2.0,3.0,4.0,5.0,6.0,7.0,8.0], [["a","c"],["b","c"],["a","e"],["a","a"],["x","x"],["a","z"]])) # [0.66667,0.33333,-1.00000,1.00000,1.00000,0.04464]