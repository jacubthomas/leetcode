'''
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0

Constraints:
0 <= n <= 104

Follow up: Could you write a solution that works in logarithmic time complexity?
'''
import math

'''
There is a pattern in factorial trailing zeroes:
- for every factor of 5 in `n` where we want to assess `n!`, there will be a zero
    with the smallest example: 5! = 5 * 4 * 3 * 2 * 1, and 5*2 creates a zero
    as `n` grows, the number of 5 * 2 combos grow, i.e. 1*10, 12*15, .etc
    
    1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10          = 3628800
    if we remove the factors of 5, by dividing by 5 we see
    1 * 2 * 3 * 4 * 1 * 6 * 7 * 8 * 9 * 2           = 145152

- for every factor of 5^x, we need to consider that more zeroes are created
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
    after we account 5^1 factors, 
    1 2 3 4 1 6 7 8 9  2 11 12 13 14  3 16 17 18 19  4 21 22 23 24  5
    we see that a 5 remains, creating a trailing zero
- so to account for trailing zero, we must find the number of factors of 5^1 - > 5^x
    such that 5^x < n. Then simply sum these counts of factors and we have our answer
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroCount = 0
        if n < 5:
            return zeroCount

        factorsOfFive = math.floor(n / 5)
        factorsOfFiveSquare = math.floor(n / (5**2))
        factorsOfFiveCube = math.floor(n / (5**3))
        factorsOfFiveQuad = math.floor(n / (5**4))
        factorsOfFiveQuint = math.floor(n / (5**5))
        zeroCount = factorsOfFive + factorsOfFiveSquare + factorsOfFiveCube + factorsOfFiveQuad + factorsOfFiveQuint

        return zeroCount

s = Solution()

print (f'n = 12,  Zeros: {s.trailingZeroes(12)},  actual factorial: {math.factorial(12)}')
print (f'n = 24,  Zeros: {s.trailingZeroes(24)},  actual factorial: {math.factorial(24)}')
print (f'n = 63,  Zeros: {s.trailingZeroes(63)},  actual factorial: {math.factorial(63)}')
print (f'n = 66,  Zeros: {s.trailingZeroes(66)},  actual factorial: {math.factorial(66)}')
print (f'n = 100, Zeros: {s.trailingZeroes(100)}, actual factorial: {math.factorial(100)}')