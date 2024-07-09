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
                
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Negligible input case where tree is length 0
        if not root:
            return root
        # Build a queue to traverse the tree BFS
        q = [root]
        # Traverse tree until queue is empty
        while len(q) > 0:
            # We can have up to two levels in queue at once
            # Tracking size here helps us determine if we're dealing with a rightmost node
            size = len(q)
            # Pop nodes from left -> right
            node = q.pop(0)
            for i in range(size):
                if node is root:
                    node.next = None
                else:
                    if i < size - 1:
                        node.next = q[0]
                q.append(node.left)
                q.append(node.right)

        return root

s = Solution()
print(s.connect(Node(1, Node(2), Node(3))))




class DFS:
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

class Solution2:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        dfs = DFS()
        dfs.traverseTree(root, None, False)
        return root
    
s2 = Solution2()
print(s2.connect(Node(1, Node(2), Node(3))))