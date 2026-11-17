/*!
58. Length of Last Word
Easy

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
*/

class Solution {
public:
    int lengthOfLastWord(string s) 
    {
        int idx = 0;              //! current char
        int length = 0;           //! ongoing word
        int lastWordLength = 0;   //! last word encountered
        while (idx < s.size())
        {
            if (s[idx] == ' ') 
            {
                //! Only track when a word actually runs its course - not just a blank space
                if (length > 0) lastWordLength = length;
                length = 0;
            }
            else
            {
                length++;
            }
            idx++;
        }

        //! Handles edge case where last word is not followed by empty space
        return (length > 0) ? length : lastWordLength;
    }
};
