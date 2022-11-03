# Valid Parentheses
# Solution
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.



class Solution:
    def __init__ (self):
        self.mapping = {'(': ')', '[' : ']', '{' : '}'}
        
    def isValid(self, s: str) -> bool:
        s = [x for x in s]
        i = 0
        while -1 < i < len (s):
            if s[i] in self.mapping.values():
                return False
            elif s[i] in self.mapping.keys():
                i = self.help (s, i+1, self.mapping[s[i]])
            else:
                i += 1
        if i < 0:
            return False
        if i >= len (s):
            return True

    def help (self, s, i, c) -> int:
        while -1 < i < len(s):
            if s[i] == c:
                return i + 1
            elif s[i] in self.mapping.keys():
                i = self.help (s, i+1, self.mapping[s[i]])
            elif s[i] in self.mapping.values():
                return -1
            else:
                i += 1
        return -1

S = Solution()
print (S.isValid('(1'))                 # False
print (S.isValid('(1)'))                # True
print (S.isValid('((1)'))               # False
print (S.isValid('(1234{56}789)2]22'))  # False
print (S.isValid('(1234{56}789)222'))   # True
print (S.isValid('(1234{5)6}789)222'))  # False
print (S.isValid('()[]{}'))             # True
print (S.isValid('([)]'))               # False