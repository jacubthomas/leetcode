
/*

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem
without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

*/
package Recursion1;
import leetcode.ListNode;

public class SwapNodesInPairs 
{
	public static ListNode swapPairs(ListNode head) 
    {
        if(head == null)
            return null;
        else if(head.next == null)
            return head;
        
        ListNode b = head.next;
        ListNode c = b.next;
        b.next = head;
        head.next = c;
        help(c, head); 
        return b;
    }
    public static ListNode help(ListNode a, ListNode prev)
    {
        if(a == null)
            return null;
        else if(a.next == null)
            return a;
        
        ListNode b = a.next;
        ListNode c = b.next;
        b.next = a;
        a.next = c;
        prev.next = b;
        help(c, a);
        return b;
    }
    public static void printResult(ListNode node) 
    {
    	if(node == null)
    		return;
    	if(node.next != null)
    		System.out.print(node.val + "->");
    	else
    		System.out.print(node.val);
    	printResult(node.next);
    }
	public static void main(String[] args) 
    {
		
		ListNode node4 = new ListNode(4);
		ListNode node3 = new ListNode(3,node4);
		ListNode node2 = new ListNode(2,node3);		
		ListNode head = new ListNode(1,node2);
		
		ListNode result = swapPairs(head);
		
		printResult(result);
	}
}
