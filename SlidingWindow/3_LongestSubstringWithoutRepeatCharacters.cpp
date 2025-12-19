/*
Medium
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
*/

class Solution {
public:
    //! Sliding window solution
    int lengthOfLongestSubstring(string s) {
        int start = 0;
        int maxLengthFound = 0;
        std::map<char, int> mapCharCounts; //! Track window state
        //! Go until window hits end of input
        for (int end=0; end < s.size(); end++) {
            //! No matter what, we increment this char count
           mapCharCounts[s[end]]++; 
           //! This count is more than 1? char is not distinct.
           //! Collapse window start forward until this char is unique
           while (mapCharCounts[s[end]] > 1) {
                //! Decrement counts for each char removed from window
                mapCharCounts[s[start]]--;
                //! Char is completely removed from window, remove from map 
                if (mapCharCounts[s[start]] == 0) 
                    mapCharCounts.erase(s[start]);
                start++;
           }
           //! Assess length of the window 
           //! Bigger than last max? Update new max
           maxLengthFound = max(maxLengthFound, end - start + 1);
        }
        return maxLengthFound;
    }
};
