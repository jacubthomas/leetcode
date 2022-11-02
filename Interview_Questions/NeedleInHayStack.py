# Implement strStr()
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Constraints:
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

class Solution:
    '''Pythonic Solution'''
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            return -1
        elif needle not in haystack:
            return -1
        return len(haystack.split(needle)[0])
        # OR
        # return haystack.index(needle)

    '''
    Initial Solution

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if len(needle) == len(haystack):
            if needle == haystack:
                return 0
            else:
                return -1

        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                match = True
                for j in range(0,len(needle)):
                    if haystack[i+j] != needle[j]:
                        match = False
                        break
                if match == True:
                    return i
        return -1
    '''

test = ''
for i in range(0, pow(10,4)):
    test += 'l'
needle = ''
for i in range(0, pow(10,3)):
    needle += 'l'
needle += 'e' 
S1 = Solution()
print (S1.strStr(test, needle))

print(S1.strStr('hello', 'll'))


print(S1.strStr('helello', 'll'))