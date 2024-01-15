'''
Generate Parentheses

Solution
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
'''

from typing import Set
from typing import List

class Solution:
    # Set will prevent redundant permutations
    permutations = set()

    # Base function call
    def generateParenthesis(self, n: int) -> List[str]:
        # Base case
        if n == 1:
            return {"()"}
        else:
            self.helper (n, n, n, "")

        # Convert Set to List for solution return
        return list(self.permutations)
    
    # Generate all acceptable permutations and add to master set
    # n - how many complete sets we should have for one permtution
    # left - how many left parentheses remain 
    # right - how many right parentheses remain 
    # permutation - temporary string attempting to become an accepted permutation
    def helper(self, n: int, left: int, right: int, permutation: str):

        # Clear for new problem
        self.permutations.clear()

        # Going left "("
        if (left > 0):
            self.helper(n, left-1, right, permutation + "(")

        # Adding pair "()"
        if (left > 0 and right > 0):
            self.helper(n, left-1, right-1, permutation + "()")

        # Going right ")"
        if (right > 0 and right > left):
            self.helper(n, left, right-1, permutation + ")")

        # Acceptable permutation, add to master solution list
        if left == 0 and right == 0 and len(permutation) == n*2:
            self.permutations.add(permutation)


s = Solution()

for i in range (3,4):
    print (s.generateParenthesis(i))
    print ()
