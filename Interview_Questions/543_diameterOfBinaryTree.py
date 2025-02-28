'''
Intuition: The maximum path can be one of two cases for any binary tree
1) Connecting left and right path through the tree root
  (left height - 1) + (right height - 1) // -1 on each to rule out the root
2) The path of some subtree down the line

Clarification on 1)
        1
      2   3
      left height = 2
      right height = 2
      total path is 2 = (2-1) + (2-1)

Example of case 2)
        1
    2       3
          4   5
        6       7
      8
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        resultTuple = self.helper(root)
        return max(resultTuple[0]-1, resultTuple[1])
            
    def helper(self, root: Optional[TreeNode]) -> List[int]:
        leftStats, rightStats = [1,0], [1,0]
        currentBranch = 0 
        # I have a left height
        if root.left is not None:
            leftStats = self.helper(root.left)
            leftStats[0] += 1
            currentBranch += leftStats[0] - 1
        # I have a right height
        if root.right is not None:
            rightStats = self.helper(root.right)
            rightStats[0] += 1
            currentBranch += rightStats[0] - 1

        # Find my biggest height
        maxHeight = max(leftStats[0], rightStats[0])
        
        # Find my biggest branch
        maxBranch = max(
            currentBranch, # current branch (LH + RH - 1 - 1)
            max(leftStats[1], rightStats[1])# biggest branch I've seen
        )
        return [maxHeight, maxBranch]
