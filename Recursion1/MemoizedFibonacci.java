import java.util.HashMap;

public class MemoizedFibonacci 
{
    public int fibHelp(int n, HashMap<Integer,Integer> map)
    {
        // base case
        if(map.containsKey(n))
            return map.get(n);
        
        // memoize
        map.put(n, fibHelp(n-2, map) + fibHelp(n-1, map));
        return map.get(n);
    }
    public int fib(int n) 
    {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        map.put(0, 0);
        map.put(1, 1);
        return fibHelp(n, map);
    }
}
