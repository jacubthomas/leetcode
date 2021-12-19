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
