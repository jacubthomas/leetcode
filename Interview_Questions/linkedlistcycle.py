# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 

# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        head.val = (-1)*pow(10,5) - 1
        if head.next is not None and head.next.val == head.val:
            return True

        return self.help(head.next, head.val)
    
    def help (self, node, pos):
        if node is None:
            return False

        if node.val <= pos:
            return True
        
        node.val = pos
        
        return self.help(node.next, pos)

S = Solution ()
L1 = ListNode (1)
print (S.hasCycle(L1))



# def __init__(self):
    #     self.seen = set()

# def hasCycle(self, head: Optional[ListNode]) -> bool:
#     if head is None:
#         return False
#     if head.next is not None and head.next.val == head.val:
#         return True

#     self.seen.add(head)
#     return self.help(head.next)

# def help (self, node):
#     if node is None:
#         return False
    
#     self.seen.add(node)

#     if node.next is not None and node.next.val in self.seen:
#         return True
    
#     return self.help(node.next)