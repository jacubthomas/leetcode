from typing import List
from typing import Optional
from typing import Set
import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
In order to tell if a TreeNode is valid in its place, it is not enough to assess that it abides its immediate parent
A valid TreeNode must abide its entire heritage, which is where min & max come in
'''
class ExtendedTreeNode:
    def __init__(self, node: TreeNode, min:int, max:int):
        self.val = node.val
        self.left= node.left
        self.right = node.right
        self.min = min
        self.max = max
    # Debugging help
    def printNode(self):
        print(f'val = {self.val}, left = {"NONE" if self.left is None else self.left.val}, right = {"NONE" if self.right is None else self.right.val}, min = {self.min}, max = {self.max}')

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Keep track of where we've been so we don't waste compute or loop indefinitely
        seen = set()
        
        # Visit nodes in FIFO order
        queue = []

        # First node is the root
        # We need to track bounds as we progress down so that n-levels down, we can assess validity
        # Root will be unbounded
        ''' Such a case of an invalid tree
        #               5
        #       3               6
        #    2     4                8
        #               7
        '''
        eRoot = ExtendedTreeNode(root, -math.inf, math.inf)
        queue.append(eRoot)
        seen.add(eRoot)

        # Kickoff traversal until all nodes have been explored
        while len(queue) > 0:
            # Take front of queue
            eNode = queue.pop(0)
            # eNode.printNode()         # Debug

            # Left child is good node
            if eNode.left is not None:
                # Valid left child has not been seen before, is less than parent and greater than minimum
                if (eNode.left not in seen and
                    eNode.left.val < eNode.val  and
                    eNode.left.val > eNode.min):
                    leftChild = ExtendedTreeNode(eNode.left, eNode.min, min(eNode.val, eNode.max))
                    queue.append(leftChild)
                    seen.add(leftChild)
                else: # Stop immediately if tree is invalid
                    return False
            
            if eNode.right is not None:
                # Valid right child has not been seen before, is less than parent and less than maximum
                if (eNode.right not in seen and
                    eNode.right.val > eNode.val and
                    eNode.right.val < eNode.max):
                    rightChild = ExtendedTreeNode(eNode.right, max(eNode.val, eNode.min), eNode.max)
                    queue.append(rightChild)
                    seen.add(rightChild)
                else: # Stop immediately if tree is invalid
                    return False
        # No inconsistencies detected, tree is valid
        return True
    

s = Solution()

print(s.isValidBST(TreeNode(2, TreeNode(1, None), TreeNode(3, None))))
print(s.isValidBST(TreeNode(2, TreeNode(2, None), TreeNode(2, None))))
print(s.isValidBST(TreeNode(5, TreeNode(3, TreeNode(2, None, None), TreeNode(6, None, None)), TreeNode(7, None,None))))
print(s.isValidBST(TreeNode(5, TreeNode(3, TreeNode(2, None, None), TreeNode(4, None, TreeNode(8, None, None))), TreeNode(6, None, TreeNode(7, None, None)))))