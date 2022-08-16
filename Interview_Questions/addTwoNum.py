# You are given two non-empty linked lists representing two non-negative integers. The digits are
# stored in reverse order, and each of their nodes contains a single digit. Add the two numbers
# and return the sum as a linked list. You may assume the two numbers do not contain any leading 
# zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def calculate(self, v1, v2, stack: List[int], carry) -> int:
        val = v1 + v2 + carry
        if val > 9:
            carry = val // 10
            stack.append(val % 10)
        else:
            carry = 0
            stack.append(val)
        return carry


    def recurseSum(self, l1: Optional[ListNode], l2 : Optional[ListNode], stack : List[int], carry):
        if l1 is None and l2 is None:
            if carry > 0:
                stack.append(carry)
            return
        if l1 is not None:
            if l2 is None:
                carry = self.calculate(l1.val, 0, stack, carry)
                self.recurseSum(l1.next, l2, stack, carry)
        if l2 is not None:
            if l1 is None:
                carry = self.calculate(0, l2.val, stack, carry)
                self.recurseSum(l1, l2.next, stack, carry)
        if l1 is not None and l2 is not None:
            carry = self.calculate(l1.val, l2.val, stack, carry)
            self.recurseSum(l1.next, l2.next, stack, carry)
            
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        self.recurseSum(l1,l2,stack,0)
        root = ListNode(None,None)
        temp = root
        print(stack)
        for i in range(0, len(stack)):
            print(stack[i])
            temp.val = stack[i]
            if i < len(stack)-1:
               temp.next = ListNode(None,None)
               temp = temp.next
        return root
       
s = Solution()

# equal length LL
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))
s.addTwoNumbers(l1,l2)

# unequal length LL, L2 > L1
l1 = ListNode(2, ListNode(3, None))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))
s.addTwoNumbers(l1,l2)

# unequal length LL, L1 > L2
l2 = ListNode(2, ListNode(3, None))
l1 = ListNode(5, ListNode(6, ListNode(4, None)))
s.addTwoNumbers(l1,l2)

# unequal length LL, L1 > L2
l2 = ListNode(2, None)
l1 = ListNode(5, ListNode(6, ListNode(4, None)))
s.addTwoNumbers(l1,l2)

# L2 is None
l2 = ListNode(0, None)
l1 = ListNode(5, ListNode(6, ListNode(4, None)))
s.addTwoNumbers(l1,l2)

# Uneven with overflow carry
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
s.addTwoNumbers(l1,l2)