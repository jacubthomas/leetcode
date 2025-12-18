/*
917. Reverse Only Letters
Easy

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
*/

class Solution {
public:
    string reverseOnlyLetters(string s) {
        int left = 0;
        int right = s.size()-1;
        while (left < right) {
            const int asciiLeft = static_cast<int>(s[left]);
            const int asciiRight = static_cast<int>(s[right]);
            //! A-Z = 65 - 90
            //! a-z = 97 - 122
            if (asciiLeft < 65 || 
                (asciiLeft > 90 && asciiLeft < 97) || 
                asciiLeft > 122)
                left++;
            else if (asciiRight < 65 || 
                    (asciiRight > 90 && asciiRight < 97) || 
                    asciiRight > 122)
                    right--;
            else if ((asciiLeft > 64 && asciiLeft < 91) ||
                    (asciiLeft > 96 && asciiLeft < 123))
                std::swap(s[left++], s[right--]);
            else left++;
        }
        return s;
    }
};
