'''
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight). 

Example 1:
Input: n = 11
Output: 3
Explanation: The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation: The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation: The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
1 <= n <= 231 - 1

Follow up: If this function is called many times, how would you optimize it?'''

import math
class Solution:
    def hammingWeight(self, n: int) -> int:
        bitCounts = 0
        while (n > 0):
            n -= 2 ** math.floor(math.log2(n))
            bitCounts += 1
        return bitCounts


s = Solution()


s.hammingWeight(1)
s.hammingWeight(2)
s.hammingWeight(3)
s.hammingWeight(4)
s.hammingWeight(7)
s.hammingWeight(66)
s.hammingWeight(67)
s.hammingWeight(127)
s.hammingWeight(1024)