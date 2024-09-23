from typing import List
from typing import Tuple
import math

class Solution:
    def isValidPoint(self, p1: Tuple[int,int], p2: Tuple[int,int]) -> bool:
        return True if (p1[0] == p2[0] or p1[1] == p2[1]) else False
    def manhattanDistance(self, p1: Tuple[int,int], p2: Tuple[int,int]) -> int:
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_index = -1
        min_distance = math.inf
        for p in range(len(points)):
            coordinate = (points[p][0],points[p][1])
            if self.isValidPoint((x,y), coordinate)
            distance = self.manhattanDistance((x,y), coordinate)
            if distance < min_distance:
                min_index = p
                min_distance = distance
        return min_index

s = Solution()

print(s.manhattanDistance((1,0), (2,3)))
