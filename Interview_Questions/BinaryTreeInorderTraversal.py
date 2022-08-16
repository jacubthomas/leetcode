# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
class Solution:

    def traverse(self, node: Optional[TreeNode], sequence: List[int]):
        if node is None:
            return
        
        self.traverse(node.left, sequence)
        sequence.append(node)
        self.traverse(node.right, sequence)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sequence = []
        self.traverse(root, sequence)
        for x in sequence:
            print (x)
        return sequence


s = Solution ()
rootnode = TreeNode (None,None,None)
s.inorderTraversal (rootnode)
print ()

rootnode = TreeNode (1,None,TreeNode (2, None, None))
s.inorderTraversal(rootnode)
print ()

rootnode = TreeNode (1,TreeNode (2, None, None),TreeNode (3, None, None))
s.inorderTraversal (rootnode)
print ()

rootnode = TreeNode (1,TreeNode (2, TreeNode (3, None, None), TreeNode (4, None, None)),TreeNode (5, TreeNode (6, None, None), TreeNode (7, None, None)))
s.inorderTraversal (rootnode)
print ()
