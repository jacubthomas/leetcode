from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.left = []
        self.right = []

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Check if optional is empty, return
        if root is None:
            return False
        
        elif root.left is None and root.right is None:
            return True
        
        elif root.left is None and root.right is not None:
            return False
        
        elif root.left is not None and root.right is None:
            return False
    
        self.left.append (root.left.val)
        self.right.append (root.right.val)
        self.helpLeft (root.left)
        self.helpRight (root.right)

        if self.left == self.right:
            return True
        return False

    # Center, left, right
    def helpLeft (self, node):
        if node is None:
            return

        if (node.left is not None):
            self.left.append (node.left.val)
        else:
            self.left.append (None)

        if (node.right is not None):
            self.left.append (node.right.val)
        else:
            self.left.append (None)

        self.helpLeft (node.left)
        self.helpLeft (node.right)

    # Center, right, left
    def helpRight (self, node):
        if node is None:
            return

        if (node.right is not None):
            self.right.append (node.right.val)
        else:
            self.right.append (None)

        if (node.left is not None):
            self.right.append (node.left.val)
        else:
            self.right.append (None)
            
        self.helpRight (node.right)
        self.helpRight (node.left)

    