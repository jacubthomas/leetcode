# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes 
# the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21
 
# Constraints:
# -2^31 <= x <= 2^31 - 1 

class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
        if x < 0:
            isNeg = True
            x = abs(x)
        # convert int -> string
        converted_num = str(x)
        # convert string -> list
        word = [char for char in  converted_num]
        # flip list elements
        word.reverse()
        # consolidate elements into string
        y = "".join(word)
        # convert string -> int
        y = int(y)
        # look for 32-bit overflow
        if isNeg:
            y  *= (-1)
        if y < -(2**31) or y > (2**31)-1:
            return 0
        return y

s = Solution()
print(s.reverse(-123))
print(s.reverse(123))
print(s.reverse(2**32))
print(s.reverse(1534236469))
