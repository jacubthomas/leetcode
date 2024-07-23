'''
Min Cost to Connect All Points

Solution involves a combination of union-find (by rank with path compression) and Kruskal's algorithm

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
'''

from typing import List
from typing import Tuple
import math

class Point:
    def __init__ (self, x: int, y:int):
        self.x = x
        self.y = y

# Union find by rank with path compression
# Serves as an efficient means to determine the graph's connectedness as we set forth connecting the graph
class UnionFind:
    def __init__ (self, points: List[List[int]]):
        self.root = {}
        self.rank = {}
        for x in range(len(points)):
            self.root[tuple([points[x][0], points[x][1]])] = tuple([points[x][0], points[x][1]])
            self.rank[tuple([points[x][0], points[x][1]])] = 1

    # Connected nodes will point to the same root
    def find (self, coordinate: Tuple[int, int]):
        # We have found the root, return it
        if coordinate == self.root[coordinate]:
            return coordinate
        # This node is not it's own root, compress the path to root along the way
        self.root[coordinate] = self.find(self.root[coordinate])
        # Return this node's root
        return self.root[coordinate]
    
    # How we will connect the graph (efficiently) as we proceed
    def union (self, coordinate1: Tuple[int, int], coordinate2: Tuple[int, int]) -> bool:
        # Determine if these two nodes are already connected
        root1, root2 = self.find(coordinate1) , self.find(coordinate2)
        # Nodes are not already connected, do so efficiently using ranking system
        # which keeps the root tree short
        if root1 != root2 and self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
        elif root1 != root2 and self.rank[root1] < self.rank[root2]:
            self.root[root1] = root2
        elif root1 != root2:
            self.root[root2] = root1
            self.rank[root1] += 1
        # Nodes are already connected, indicate such back to calling function
        else:
            return False
        # Nodes were just now connected, indicate such back to calling function
        return True

class Solution:
    # Return manhattan distance between two points
    def computeCost (self, coordinates: Tuple[Point,Point]):
        return abs(coordinates[0][0] - coordinates[1][0]) + abs(coordinates[0][1] - coordinates[1][1])

    # Main thread of solution
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Handle negligible case
        if len(points) <= 1:
            return 0
        # Enact Union-Find structure, to be leveraged with Kruskal's algorithm
        uf = UnionFind(points)
        # Build out a mapping of the costs of each node to each other
        coordinateCosts = {}
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                twoPoints = (points[i],points[j])
                coordinateCosts[tuple([points[i][0], points[i][1], points[j][0], points[j][1]])] = self.computeCost(twoPoints)
        # Sort that mapping, so the cheapest connections are attempted first
        coordinateCosts = dict(sorted(coordinateCosts.items(), key=lambda item: item[1]))
        # End result will be summed here
        sumCost = 0
        # We will always know precisely how many connections to meet the solution
        edgesToConnect = len(points) - 1 
        # In order, greedily connect the graph Kruskal style
        for x,y in coordinateCosts.items():
            p1 = tuple([x[0],x[1]])
            p2 = tuple([x[2],x[3]])
            # When new connections are made, update accordingly
            if uf.union(p1, p2) == True:
                sumCost += y
                edgesToConnect -= 1
                # All done!
                if edgesToConnect <= 0:
                    return sumCost
s = Solution()
print(s.minCostConnectPoints([[0,0]])) # 0
print(s.minCostConnectPoints([[3,12],[-2,5],[-4,1]])) # 18
print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])) # 20
print (s.minCostConnectPoints([[2,-3],[-17,-8],[13,8],[-17,-15]]))