package Recursion1;

import leetcode.ListNode;

public class SwapNodesInPairs {

	public static ListNode swapPairs(ListNode head) {
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
    public static ListNode help(ListNode a, ListNode prev){
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
    
    public static void printResult(ListNode node) {
    	if(node == null)
    		return;
    	if(node.next != null)
    		System.out.print(node.val + "->");
    	else
    		System.out.print(node.val);
    	printResult(node.next);
    }
    
	public static void main(String[] args) {
		
		ListNode node4 = new ListNode(4);
		ListNode node3 = new ListNode(3,node4);
		ListNode node2 = new ListNode(2,node3);		
		ListNode head = new ListNode(1,node2);
		
		ListNode result = swapPairs(head);
		
		printResult(result);
	}

}
