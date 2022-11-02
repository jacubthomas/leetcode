# Rotate Image

# Solution
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # trivial case, nothing to rotate
        if len (matrix[0]) == 1:
            return matrix
        return self.flip_by_column_and_transpose (matrix)
    
    def flip_by_column_and_transpose(self, matrix: List[List[int]]) -> None:
        # flip column elements
        for i in range(0, len(matrix[0])):
            for j in range(0, int(len(matrix[0])/2)):
                precomputed = len(matrix[i])-1-j
                matrix[j][i], matrix[precomputed][i] = matrix[precomputed][i], matrix[j][i]
        # transpose matrix
        for i in range(1, len(matrix[0])):
            j = 0
            while j < i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

S1 = Solution ()
print (S1.rotate ([[1]]))
print (S1.rotate ([[1,2],[3,4]]))
print (S1.rotate ([[1,2,3],[4,5,6],[7,8,9]]))
print (S1.rotate ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))