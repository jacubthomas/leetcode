/*

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

*/
public class nthPower 
{
    public double powHelp(double product, double x, int count, int n)
    {
        // result calculated
        if(n-count == 0)
            return product;
        // result has zeroed or exceeded double capacity
        else if(product == 0 || product == Double.NEGATIVE_INFINITY 
                             || product == Double.POSITIVE_INFINITY)
            return product;
        // approaching solution
        if(count * 2 > n)
        {
            return powHelp(product*x, x, ++count, n);
        }
        // reduce recursive call stack, increase speed of calculation
        return powHelp(product*product, x, count*2, n);
    }
    public double myPow(double x, int n) 
    {
        // handle immediate calculations
        if (n == 0)
            return 1.0;
        else if(x == 1)
            return 1.0;
        else if(x == -1)
        {
            if(n%2 == 0)
                return 1.0;
            else
                return -1.0;
        }
        // differentiate negative exponents
        if(n<0)
        {
            n *= -1;
            return (1.0/powHelp(x, x, 1, n));
        }
        return powHelp(x, x, 1, n);
    }
    public static void main(String args[])
    {
        nthPower n = new nthPower();
        double result = n.myPow(1.0,-2147483648);
        System.out.println(result);
    }
}
