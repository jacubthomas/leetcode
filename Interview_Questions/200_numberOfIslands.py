'''
Difficulty Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
from typing import List
from typing import Set
from typing import Tuple

class UnionFindSolution:

    def __init__(self):
        self.rootMap = {}
        self.rank = {}
    
    # Map will be used to see connected components
    def initializeUFMap(self, grid: List[List[str]]):
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                self.rootMap[(row,col)] = (row,col)
                self.rank[(row, col)] = 1


    def detectInbounds(self, coordinate_a: tuple[int, int], grid: List[List[str]]):
        return (coordinate_a[0] > -1 and 
                coordinate_a[0] < len(grid) and
                coordinate_a[1] > -1 and
                coordinate_a[1] < len(grid[0]))

    def detectMatchingGeography(self, coordinate_a: tuple[int, int], coordinate_b: tuple[int, int], grid: List[List[str]]) -> bool:
        return grid[coordinate_a[0]][coordinate_a[1]] == grid[coordinate_b[0]][coordinate_b[1]]

    def detectAdjacentCoordinates(self, coordinate_a: tuple[int, int], coordinate_b: tuple[int, int]) -> bool:
        if (coordinate_a[0] == coordinate_b[0] and
            (coordinate_a[1] == coordinate_b[1] + 1 or
            coordinate_a[1] == coordinate_b[1] - 1)):
            return True
        
        if (coordinate_a[1] == coordinate_b[1] and
            (coordinate_a[0] == coordinate_b[0] + 1 or
            coordinate_a[0] == coordinate_b[0] - 1)):
            return True
        
        return False

    # Find the root of this connected component
    # Other connected components will (eventually) match this root
    def find(self, coordinate: tuple[int, int]) -> tuple[int, int]:
        # A coordinate is it's own root
        if coordinate == self.rootMap[coordinate]:
            return coordinate
        
        # A coordinate is not it's own root, compress/update the path to its root
        self.rootMap[coordinate] = self.find(self.rootMap[coordinate])
        return self.rootMap[coordinate]

    # Union
    def union(self, coordinate_a: tuple[int, int], coordinate_b: tuple[int, int], grid: List[List[str]]):
        # Only attempt union if both coordinates are valid
        if self.detectInbounds(coordinate_a, grid) is False or self.detectInbounds(coordinate_b, grid) is False:
            return
        # Only attempt union if both coordinates have matching geography
        if self.detectMatchingGeography(coordinate_a, coordinate_b, grid) is False:
            return
        
        # Examine which sets each coordinate belongs
        root_a, root_b = self.find(coordinate_a), self.find(coordinate_b)

        # Coordinates are valid with matching geography, ensure they exist under a united root
        if root_a != root_b and self.detectAdjacentCoordinates(coordinate_a, coordinate_b):
            # using ranks (height of each root) we can be a little more performant
            if self.rank[root_a] > self.rank[root_b]:
                self.rootMap[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.rootMap[root_a] = root_b
            else:
                self.rootMap[root_b] = root_a
                self.rank[root_a] += 1

    def numIslands(self, grid: List[List[str]]) -> int:
        # Set up connected components map with each coordinate pointing to itself
        self.initializeUFMap(grid)

        # Unite all contiguous, geographically-matching coordinated
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                self.union((row,col), (row+1,col), grid)
                self.union((row,col), (row,col+1), grid)

        # Solution will be stored in this set
        islandSet = set()  

        # Find the root of each coordinate
        # Should that coordinate point to land, add it to the solution set
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                root = self.find((row,col))
                if grid[root[0]][root[1]] == "1":
                    islandSet.add(root)
        return len(islandSet)
    
s = Solution()

print(f'number of islands is: {s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])}')
print(f'''number of islands is: {s.numIslands([["1","1","0","0","0"],
                                               ["1","1","0","0","0"],
                                               ["0","0","1","0","0"],
                                               ["0","0","0","1","1"]]
                                               )}''')
