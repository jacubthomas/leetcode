/*

You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists. Return the head of the merged 
linked list.
 
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

*/
public class MergeTwoSortedLists 
{
    // Definition for singly-linked list.
    public class ListNode 
    {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    public void mergeHelp(ListNode list1, ListNode list2, ListNode head)
    {
        // end of list checks
        if(list1 == null)
            head.next = list2;
        else if(list2 == null)
            head.next = list1;
        // compare, chain next element and step forward
        else if(list1.val <= list2.val)
        {
            head.next = list1;
            head = list1;
            mergeHelp(list1.next, list2, head);
        }
        else 
        {
            head.next = list2;
            head = list2;
            mergeHelp(list1, list2.next, head);
        }
    }
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) 
    {
        // empty list check; no comparison needed
        if(list1 == null)
            return list2;
        else if(list2 == null)
            return list1;  

        // root new list
        ListNode head;
        if(list1.val <= list2.val)
        {
            head = list1;
            mergeHelp(list1.next, list2, head);
        }
        else 
        {
            head = list2;
            mergeHelp(list1, list2.next, head);
        }
        return head;
    }
}