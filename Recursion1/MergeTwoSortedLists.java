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
        if(list1 == null)
            head.next = list2;
        else if(list2 == null)
            head.next = list1;
        
        else if(list1.val <= list2.val)
        {
            head = list1;
            mergeHelp(list1.next, list2, head);
        }
        else 
        {
            head = list2;
            mergeHelp(list1, list2.next, head);
        }
    }
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) 
    {
        // handle edge cases
        if(list1 == null)
            return list2;
        else if(list2 == null)
            return list1;
        
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