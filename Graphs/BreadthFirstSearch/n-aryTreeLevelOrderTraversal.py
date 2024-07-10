'''
Given an n-ary tree, return the level order traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
'''

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Negligible case 1: empty input
        if root is None:
            return []
        
        # Store our result in here
        solution = [[root.val]]

        # Negligible case 2: empty input
        if len(root.children) == 0:
            return solution
        
        # Proceeding with BFS to trace out tree using FIFO queue
        q = []

        # Add all root's children to queue
        for child in root.children:
            q.append(child)

        # Keep going until we've run out of nodes to explore
        while len(q) > 0:

            # Helps us explore the tree in levels 
            size = len(q)

            # Store each level in its own List[int]
            level = []

            # Explore a level
            for _ in range(size):
                # Get a node from front of queue
                node = q.pop(0)
                # Add into level's result list
                level.append(node.val)
                # Add this's node children to the queue
                for child in node.children:
                    q.append(child)
            # Entire level has been traced, add its result to our solution, List[List[int]]
            solution.append(level)

        return solution