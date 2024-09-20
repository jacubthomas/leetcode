'''
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two 
indices in a string (not necessarily different) and swap the characters at these indices. Return true if
it is possible to make both strings equal by performing at most one string swap on exactly one of the 
strings. Otherwise, return false.

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

Constraints:
1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
'''

from typing import List

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Let's keep track of how many mismatches we find
        mismatchingChars = 0
        # Let's keep track of the mismatch indices
        mismatchingIndices = []
        # Consider every letter in both strings - guaranteed to be equal length
        for i in range(len(s1)):
            # Mismatch detected
            if s1[i] != s2[i]:
                # Update our tracking
                mismatchingIndices.append(i)
                mismatchingChars += 1
                # There can not be more than 2 mismatches resolved by just one swap
                if mismatchingChars > 2:
                    return False
        # Can't resolve by swapping if there's no where to swap with
        if mismatchingChars == 1:
            return False
        # Ensure the swap takes - two mismatches doesn't alone guarantee we are in the clear
        elif mismatchingChars == 2:
            if (s1[mismatchingIndices[0]] != s2[mismatchingIndices[1]]) or ((s1[mismatchingIndices[1]] != s2[mismatchingIndices[0]])):
                return False
        # We are all good
        return True
    
s = Solution()
print(s.areAlmostEqual("bank","kanb"))
print(s.areAlmostEqual("attack","defend"))
print(s.areAlmostEqual("kelb","kelb"))
print(s.areAlmostEqual("ac","aa"))