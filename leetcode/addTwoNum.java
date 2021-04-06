package leetcode;

import java.util.Stack;

public class addTwoNum {

	public static void main(String[] args) {
		
		// problem setup ----------------------------
		ListNode temp11 = new ListNode(9, null);
		ListNode temp12 = new ListNode(9, temp11);
		ListNode temp13 = new ListNode(9, temp12);
		ListNode l1 = new ListNode(9, temp13);
		ListNode l1_copy = l1;
		
		ListNode temp21 = new ListNode(9, null);
		ListNode temp22 = new ListNode(9, temp21);
		ListNode temp23 = new ListNode(9, temp22);
		ListNode temp24 = new ListNode(9, temp23);
		ListNode temp25 = new ListNode(9, temp24);
		ListNode l2 = new ListNode(9, temp25);
		ListNode l2_copy = l2;
		// ------------------------------------------
		
		
		// Problem requires we flip LinkedList twice
		Stack<Integer> stack1 =  new Stack<Integer>();
		Stack<ListNode> stack2 =  new Stack<ListNode>();
		
		// sums two lists into one sum and flips order with stack insert
		int remainder = 0;
		while(l1_copy != null || l2_copy != null) {
			
			int left, right;
			if(l1_copy == null)
				left = 0;
			else
				left = l1_copy.val;
			if(l2_copy == null)
				right = 0;
			else
				right = l2_copy.val;
			
			
			int sum = left + right + remainder;
			if(sum > 9) {
				remainder = sum / 10;
				sum = sum % 10;
			}
			else {
				remainder = 0;
			}
			stack1.add(sum);
			if(l1_copy != null)
				l1_copy = l1_copy.next;
			if(l2_copy != null)
				l2_copy = l2_copy.next;
		}
		// if lingering remainder, place onto stack
		if(remainder > 0) {
			stack1.add(remainder);
		}
		
		// unflip stack and create new LinkedList with solution
		while(!stack1.empty()) {
			ListNode node = new ListNode();
			if(!stack2.empty())
				node.next = stack2.peek();
			node.val = stack1.pop();
			stack2.add(node);
		}
		
		// prints solution
		ListNode tempnode = stack2.peek();
		while(tempnode != null){
			System.out.print(tempnode.val + " ");
			tempnode = tempnode.next;
		}
	}
}