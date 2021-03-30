package leetcode;

public class addTwoNum {

	public static String recurseSum(ListNode list){
        if(list == null) return "";
        String sumnum = recurseSum(list.next);
        String curnum = String.valueOf(list.val);
        sumnum += curnum;
        return sumnum;
    }
	
	public static ListNode recurseList(String s, int i) {
		if(i == s.length()-1) {
			int temp = Character.getNumericValue(s.charAt(i));
			ListNode ln = new ListNode(temp,null);
			return ln;
		}
		
		int temp = Character.getNumericValue(s.charAt(i));
		ListNode returned = recurseList(s, i+1);
		ListNode ln = new ListNode(temp,null);
		ListNode diver = returned;
		while(diver.next != null) {
			diver = diver.next;
		}
		diver.next = ln;
		return returned;
	}

	public static void main(String[] args) {
		
		ListNode temp1 = new ListNode(3, null);
		ListNode temp2 = new ListNode(4, temp1);
		ListNode l1 = new ListNode(2, temp2);
		
		
		ListNode temp3 = new ListNode(4, null);
		ListNode temp4 = new ListNode(6, temp3);
		ListNode l2 = new ListNode(5, temp4);
	
		
        String num1 = recurseSum(l1);
        String num2 = recurseSum(l2);
        System.out.println(num1  + " " + num2);
        
//        long long1 = Long.parseLong(num1);
//        long long2 = Long.parseLong(num2);
        int remainder = 0;
        String newsum = "";
        if(num1.length() >= num2.length()) {
	        for(int i = num1.length()-1; i>=0; i--) {
	        	int one = Character.getNumericValue(num1.charAt(i));
	        	int two = 0;
	        	if(i < num2.length()) {
	        		two = Character.getNumericValue(num2.charAt(i));
	        	}
	        	one += two + remainder;
	        	if(one > 9) {
	        		remainder = 1;
	        		one = one - 10;
	        	} else {
	        		remainder = 0;
	        	}
	        	newsum += String.valueOf(one);
	        }
        } else {
        	for(int i = 0; i<num2.length(); i++) {
        		int two = Character.getNumericValue(num2.charAt(i));
	        	int one = 0;
	        	if(i < num1.length()) {
	        		one = Character.getNumericValue(num1.charAt(i));
	        	}
	        	one += two + remainder;
	        	if(one > 9) {
	        		remainder = 1;
	        		one = one - 10;
	        	} else {
	        		remainder = 0;
	        	}
	        	newsum += String.valueOf(one);
	        }
        }
       System.out.println(newsum);
//////        System.out.println("int1: " + long1 );
//////        System.out.println("int2: " + long2 );
//////        
//////        long1 += long2;
////        num1 = String.valueOf(long1);
//        System.out.println("sum: " + num1 );
        
        //ListNode l3 = recurseList(newsum, 0);
       ListNode root = new ListNode(0,null);
       ListNode current_list = new ListNode(0,null);
       root.next = current_list;
       
       for(int i=0; i< newsum.length();i++) {
    	   ListNode temp_list = new ListNode(Character.getNumericValue(newsum.charAt(i)),null);
    	   current_list.next = temp_list;
    	   current_list =  temp_list;
       }
       root = root.next.next;
        while(root != null) {
        	System.out.print(root.val);
        	root = root.next;
        }
//        String test = "99999999999999";
//        int testing = Integer.parseInt(test);
//        long test2 = Long.parseLong(test);
//        System.out.println(test2); 
   
        
//        ListNode root = new ListNode(0,null);
//        ListNode current_list = new ListNode(0,null);
//        root.next = current_list;
//        
//        for(int i = num1.length()-1; i>=0; i--){
//            ListNode temp_list = new ListNode(num1.charAt(i),null);
//            current_list.next = temp_list;
//            current_list = temp_list;
//        }

//        return root.next.next;

	}

}
