/*

You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb
1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45

*/
import java.util.HashMap;
public class climbStairs 
{
    public int climbHelp(int n, HashMap<Integer, Integer>memo)
    {
        // check if precomputed / base case
        if(memo.containsKey(n))
            return memo.get(n);

        // find (n) and memoize
        memo.putIfAbsent(n, 
        
            (climbHelp(n-1, memo)) +
            (climbHelp(n-2, memo))

        );

        return memo.get(n);
    }
    
    public int climb(int n) 
    {
        HashMap<Integer, Integer> memo = new HashMap<Integer, Integer>();
        memo.put(0,0);
        memo.put(1,1);   
        memo.put(2,2);  
        return climbHelp(n, memo);
    }

    public static void main(String args[])
    {
        climbStairs c = new climbStairs();
        c.climb(8);
    }
}
