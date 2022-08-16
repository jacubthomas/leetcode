# Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
# that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note 
# that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods

from typing import List

class Solution:
    two   = "abc"
    three = "def"
    four  = "ghi"
    five  = "jkl"
    six   = "mno"
    seven = "pqrs"
    eight = "tuv"
    nine  = "wxyz"
    numpad = [two, three, four, five, six, seven, eight, nine]

    # returns the letters associated with a given number [2,9]
    def getLetters (self, num: chr) -> List[chr]:
        return list(self.numpad[int(num)-2])

    # explores all permutations of input, one num at a time
    # once permutation length = input length, append to combos
    def permute (self, digits: str, combos : List[str], permutation: str):

        # end of the line, permutation complete
        if len (digits) == len (permutation):
            combos.append(permutation)
            return

        # get list of letters for a given digit, depending on where we are
        # in the permutation
        letters = self.getLetters (digits[len (permutation)])
        
        # explore all letters, and make recursive call with each
        for i in letters:
            permutation += i
            self.permute (digits, combos, permutation)
            permutation = permutation[0:len (permutation)-1]

                
    # Driving function
    def letterCombinations (self, digits: str) -> List[str]:

        # base cases
        if len (digits) == 0:
            return []
        elif len (digits) == 1:
            return self.getLetters (digits[0])
        
        combos = []
        self.permute (digits, combos, "")
        print (combos)                    # Debug
        return combos
        

s = Solution ()

s.letterCombinations ("")
print ()

s.letterCombinations ("2")
print ()

s.letterCombinations ("23")
print ()

s.letterCombinations ("234")
print ()

s.letterCombinations ("2345")
print ()
