#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    string decodeString(string s) {
        stack<int> stackScalars;
        stack<string> stackSubstrings;
        int index = 0;
        string digitString = "";
        string currentString = "";

        //! Cover entire input string
        while(index < s.length()) {
            //! Encountered an int - gather all digits
            while (std::isdigit(s[index]))
                digitString += s[index++];
            //! Case: scalar int
            if (digitString.empty() == false) {
                stackScalars.push(stoi(digitString));
                digitString = "";
            }

            //! Case: new encoded substring starts
            else if (s[index] == '[') {
                index++;
                //! Preserve our current string on the stack
                stackSubstrings.push(currentString);
                 //! Start fresh substring to handle upcoming encoded string
                currentString = "";
            }

            //! Case: end of an encoded substring
            else if (s[index] == ']') {
                index++;
                //! Get the most recent scalar value
                int scalar = stackScalars.top();
                stackScalars.pop();
                //! Decoding is just repeating, so gather what we're repeating
                string repeatString = currentString;
                //! Preserve order, gather prefix substring, then append the new decoded string to prefix
                currentString = stackSubstrings.top();
                stackSubstrings.pop();
                //! Decode by repeat
                for (int i=0; i < scalar; i++)
                    currentString += repeatString;
            }

            //! Case: any character of a substring
            else
                currentString += s[index++];
        }

        return currentString;
    }
};


int main () {
    Solution s;
    cout << "3[a]2[bc] = " << s.decodeString("3[a]2[bc]") << ", expected: " << "aaabcbc" << endl;
    cout << "3[a2[c]] = " << s.decodeString("3[a2[c]]") << ", expected: " << "accaccacc" << endl;
    cout << "2[abc]3[cd]ef = " << s.decodeString("2[abc]3[cd]ef") << ", expected: " << "abcabccdcdcdef" << endl;
    cout << "abc3[cd]xyz = " << s.decodeString("abc3[cd]xyz") << ", expected: " << "abccdcdcdxyz" << endl;
    cout << "10[a] = " << s.decodeString("10[a]") << ", expected: " << "aaaaaaaaaa" << endl; 
    cout << "2[3[a]b] = " << s.decodeString("2[3[a]b]") << ", expected: " << "aaabaaab" << endl; 
    cout << "3[z2[xy]] = " << s.decodeString("3[z2[xy]]") << ", expected: " << "zxyxyzxyxyzxyxy" << endl;
    return 0;
}
