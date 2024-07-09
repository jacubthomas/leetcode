from typing import List
from typing import Optional
import math

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class BFS:
    def traverseTree(self, currentNode: Optional[Node], parentNode: Optional[Node], wentLeft: bool):
        # End of recursion, beyond the tree
        if currentNode is None:
            return
    
        # Root of tree
        if parentNode is None:
            currentNode.next = None
        # Anywhere else along the tree
        else:
            # Given the structure of the tree, 
            # left leafs will always have sibling right leafs
            if wentLeft:
                currentNode.next = parentNode.right
            # Given the structure of the tree, 
            # right leafs will rely on its parent node's sibling to the right
            # Since we are tracing this tree right to left, top to bottom, 
            # we will always know the answer to whether our parent has a rightbound sibling
            # if so, it is guaranteed to have a child at this node's height
            else:
                if parentNode.next is not None:
                    currentNode.next = parentNode.next.left
                else:
                    currentNode.next = None

        # Continue mapping out tree - we go right -> left
        # because we are building additional connections to the right
        # These additional connections are not just to solve the problem
        # they can also be used for our benefit
        self.traverseTree(currentNode.right, currentNode, False)
        self.traverseTree(currentNode.left, currentNode, True)

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        bfs = BFS()
        bfs.traverseTree(root, None, False)
        return root

s = Solution()
print(s.connect(Node(1, Node(2), Node(3))))