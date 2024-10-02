'''
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''
import math
from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Do not return anything, modify head in-place instead.
"""
class Solution:
    def copy(self, node:Optional[ListNode]) -> ListNode:
        if node is None:
            return None
        copyNode = ListNode(node.val, node.next)
        return copyNode
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None or head.next.next is None:
            return
        node = head
        # Determine the length of the list
        nodeCount = 2
        while node.next.next is not None:
            node = node.next
            nodeCount += 1

        # Identify halfway point, as we will flip the back half into the first half
        halfwayIndex = int((math.floor(nodeCount)) / 2)
        
        # Reverse order of back half of list
        currentNode = head
        for i in range(halfwayIndex):
            currentNode = currentNode.next
        previousNode = None
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        # Merge lists now
        leftListNode, rightListNode = head, previousNode
        newHead = None
        mergedList = None
        while leftListNode is not None or rightListNode is not None:
                onlyGoLeft = False
                if leftListNode == rightListNode:
                    onlyGoLeft = True
                if leftListNode is not None:
                    if leftListNode == mergedList:
                        break
                    if mergedList is None:
                        mergedList = leftListNode
                        newHead = mergedList
                    else:
                        mergedList.next = leftListNode
                        mergedList = mergedList.next
                    leftListNode = leftListNode.next
                if rightListNode is not None:
                    if onlyGoLeft == False:
                        if mergedList is None:
                            mergedList = rightListNode
                            newHead = mergedList
                        else:
                            mergedList.next = rightListNode
                            mergedList = mergedList.next
                    rightListNode = rightListNode.next
        head = newHead


        # # Print our results for DEBUG purposes
        node = head
        while node is not None:
            if node.next is None:
                print (f'node: {node.val} next: None')
            else:
                print (f'node: {node.val}, next: {node.next.val}')
            node = node.next

s = Solution()

print (s.reorderList(ListNode(1,ListNode(2,ListNode(3,None)))))
print (s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4, None))))))
print (s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4, ListNode(5,None)))))))
print (s.reorderList(ListNode(1,ListNode(2,ListNode(3,ListNode(4, ListNode(5,ListNode(6,None))))))))



'''
def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None or head.next.next is None:
            return
        
        pointerFront = head
        pointerRear = head
        nodeCount = 2
        while pointerRear.next.next is not None:
            pointerRear = pointerRear.next
            nodeCount += 1

        # if nodeCount % 2 == 0:
        while pointerFront.next != pointerRear:
            copyFrontNode = self.copy(pointerFront.next)
            copyRearNode = self.copy(pointerRear.next)
            pointerFront.next = copyRearNode
            pointerRear.next = copyFrontNode
            pointerFront = pointerFront.next
            # pointerFront.next.next = pointerRear
            # pointerRear.next = copyBnode
            # copyBnode.next = None
            # pointerFront = pointerFront.next
        # else:
        #     while pointerFront != pointerRear:
        #         copyBnode = self.copy(pointerFront.next)
        #         pointerFront.next = pointerRear.next
        #         pointerFront.next.next = pointerRear
        #         pointerRear.next = copyBnode
        #         copyBnode.next = None
        #         pointerFront = pointerFront.next
'''