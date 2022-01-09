package leetcode;

import java.util.Arrays;

public class twoSum 
{
	static int[] nums = {3, 7, 9, 13, 19, 2, 6};
	static int target = 21;
	
	public static void print(int[] arr) 
	{
		for(Integer i: arr) {
			System.out.print(i + ", ");
		}
		System.out.println();
	}
	public static int[] twoSum(int[] nums, int target) 
	{
		for(int i=0; i<nums.length; i++) {
			int temp = target - nums[i];
			int index = Arrays.binarySearch(nums, temp);
			if(index < nums.length) {
				int[] result = {  nums[i], nums[index] };
				return result;
			}
		}
		return nums;
	}
	// Driver code
	public static void main(String args[])
	{	
		print(nums);
		Arrays.sort(nums);
		print(nums);
		int[] result = twoSum(nums,  target);
		if(result.length == 2) {
			System.out.println(result[0] + " + " + result[1] + " = " + target);
		} else {
			System.out.println("Solution not in nums!");
		}
	}
}