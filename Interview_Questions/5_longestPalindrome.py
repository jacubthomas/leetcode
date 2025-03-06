'''
Difficulty Medium
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''

# This is a brute-force O(N^2) Two-Pointer Solution
# There is also a Dynamic Programming solution O(N^2) and a O(N) solution I hope to find
def longestPalindrome(s: str) -> str:
  # A single character string is a palindrome
  if len(s) == 1:
      return s
  
  # Keep track of our best discovered palindrome
  longestPalindrome = 1
  palindromeIndex = 0
  
  # Consider the whole string and slowly narrow down with 2 pointer approach
  # Every iteration, shrink i -> j or i <- j
  # First consider all possibilities from i _ _ _ _ j to i j _ _ _ _
  # Then advance i such that _ i _ _ _ j now moves to _ i j _ _ _
  i, j = 0, 0
  while i < len(s):
      # Setup left and right pointers
      left, right = i, len(s)-1 - j
      # Looks like the start of a palindrome, continue digging into it
      while s[left] == s[right] and left < right:
          left += 1
          right -= 1
      # Substring was a palindrome, assess if biggest so far and move on
      if left >= right:
          length = len(s)-i-j
          if length > longestPalindrome:
              longestPalindrome = length
              palindromeIndex = i
          i += 1
          j = 0
          continue
      # No palindrome detected - shrink i <- j
      else:
          j += 1
  
  return s[palindromeIndex:palindromeIndex+longestPalindrome]
                
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
