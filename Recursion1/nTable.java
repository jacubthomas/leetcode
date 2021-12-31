public class nTable 
{
    public int kthGrammar(int n, int k)
    {
        // base cases for first and second row
        if(n == 1 || (n == 2 && k == 1))
            return 0;
        if(n == 2 && k == 2)
            return 1;

        // data points from current state
        int row_length = (int) Math.pow(2, n-1);
        int half = row_length/2;

        // pre-computed in prior state
        if( k <= half)
            return kthGrammar(n-1, k);
        
        // still pre-computed in prior, but back-half elements are inverse front-half
        int temp = (k-half)%2;
        if(temp == 1)
            return kthGrammar(n-1, k-half+1);
        return kthGrammar(n-1, k-half-1);
    }    
    public static void main(String args[])
    {
        nTable n = new nTable();
        int result = n.kthGrammar(30,20000000);
        System.out.println(result);
    }
}