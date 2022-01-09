package leetcode;

import java.util.Vector;

public class medianTwoSorted {

	public int medianTwoSorted(Vector<Integer> vec1, Vector<Integer> vec2) {
		int size1 = vec1.size();
		int size2 = vec2.size();
		return help(vec1, vec2, 0, 0, size1, size2);
	}
	
	public int help(Vector<Integer> vec1, Vector<Integer> vec2, int lo1, int lo2, int hi1, int hi2) {
		if(hi1 <= 0) {
			
		}
		else if(hi2 <= 0) {
			
		}
		int mid1 = (lo1 + hi1 - 1)/2;
		int mid2 = (lo2 + hi2 - 1)/2;
		int at1 = vec1.get(mid1);
		int at2 = vec2.get(mid2);
		if(at1 < at2) {
			return help(vec1, vec2, lo1, mid2+1, mid1, hi2);
		} else if(at1 > at2) {
			return help(vec1, vec2, mid1+1, lo2, hi1, mid2);
		} else {
			
		}
	}

	public static void main(String[] args) {
		Vector<Integer> vec1 = new Vector<Integer>();
		Vector<Integer> vec2 = new Vector<Integer>();
		
		vec1.add(1);
		vec1.add(2);
		vec1.add(4);
		vec2.add(0);
		vec2.add(3);
		vec2.add(5);
	}

}
