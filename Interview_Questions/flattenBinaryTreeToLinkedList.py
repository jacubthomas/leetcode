from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Idea, use a preorder traversal to flatten the tree
    # Navigating through recursive calls
    # Preorder being: Root, Left (subtree), Right (subtree)
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Reach an end to tree - no more work to be done on this path
        if root is None:
            return 

        # Capture the child nodes for later reference
        nodeLeft = root.left
        nodeRight = root.right
        
        # Explore left subtree 
        if nodeLeft is not None:
            # Keep going left down the tree
            self.flatten(nodeLeft)
            # To flatten, we put all nodes to the right as linked list
            # This is fine, because we still have reference to left & right child
            root.left = None
            # Overwrite right child with left
            # We will restore right child later
            root.right = nodeLeft
            # Move ourselves down our linked list
            root = nodeLeft
            # All the left's children have formed a linked list on nodeLeft.right
            # And all these children will be higher in the linked list than root's right child
            # The lowest child will point to right child
            while root.right is not None:
                root = root.right
        # Explore right subtree
        if nodeRight is not None:
            # Ensure we flatten tree by closing off left paths 
            root.left = None
            # Keep diving into right's subtree
            self.flatten(nodeRight)
            # Don't point any node's at themselves!
            if root != nodeRight:
                # Finally, we can connect right child and it's flattened subtree to root and nodeLeft's subtree
                root.right = nodeRight


s = Solution()

answer = s.flatten(TreeNode(1,TreeNode(2,TreeNode(3,None,None),TreeNode(4,None,None)),TreeNode(5, None, TreeNode(6,None,None))))
print (answer)
# []
# [0]
# [1,2,5,3,4,null,6]
# [1,null,2,3]