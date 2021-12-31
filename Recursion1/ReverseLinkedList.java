/*

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

*/

package Recursion1;
import leetcode.ListNode;

public class ReverseLinkedList 
{	
	public static void help(ListNode a, ListNode b) 
	{
		if(b.next==null) 
		{
			b.next = a;
			return;
		}
		help(b, b.next);
		b.next = a;
	}
	public static ListNode reverseList(ListNode head) 
	{
		// base case 1: empty list
		if(head == null)
            return null;
		// base case 2: solo item in list
        else if(head.next ==  null)
            return head;
		ListNode tail = head;
		while(tail.next != null)
			tail = tail.next;
		
		help(head, head.next);
		head.next = null;
	    return tail;
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
		
		ListNode result = reverseList(head);
		
		printResult(result);
	}
}
