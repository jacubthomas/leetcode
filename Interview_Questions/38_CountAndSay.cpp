/*
 * Difficulty Medium
 * 
 * The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
 * countAndSay(1) = "1"
 * countAndSay(n) is the run-length encoding of countAndSay(n - 1).
 * Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical
 * characters (repeated 2 or more times) with the concatenation of the character and the number marking the
 * count of the characters (length of the run). For example, to compress the string "3322251" we replace 
 * "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the 
 * compressed string becomes "23321511".
 * 
 * Given a positive integer n, return the nth element of the count-and-say sequence.
 * 
 * Example 1:
 * Input: n = 4
 * Output: "1211"
 * Explanation:
 * countAndSay(1) = "1"
 * countAndSay(2) = RLE of "1" = "11"
 * countAndSay(3) = RLE of "11" = "21"
 * countAndSay(4) = RLE of "21" = "1211"
 * 
 * Example 2:
 * Input: n = 1
 * Output: "1"
 * Explanation:
 * This is the base case.
 * 
 * Constraints:
 * 1 <= n <= 30
 */

#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int assessSubsequence(string sequence, char lastDigit) {
        if (sequence.length() == 0) return 1;
        int count = 1;
        for (int i = 0; i < sequence.length(); i++) {
            if (sequence[i] == lastDigit) {
                count++;
                continue;
            }
            break;
        }
        return count;
    }

    string countAndSayRecurse(int n, string sequence) {
        if (n == 0) return sequence;

        int i = 0;
        string newSequence = "";
        while (i < sequence.length()) {
            int count = assessSubsequence(sequence.substr(i+1), sequence[i]);
            newSequence += to_string(count) + sequence[i];
            i += count;
        }

        return countAndSayRecurse(n-1, newSequence);
    }

    string countAndSay(int n) {
        if (n == 1) return "1";
        return countAndSayRecurse(n-1, "1");
    }
};

int main() {
    Solution s;
    
    for (int i=1; i < 31; i++)
        cout << s.countAndSay(i) << endl;
}



/*
1
11
21
1211
111221
312211
13112221
1113213211
*/

/*
1
11
21
1211
111221
312211
13112221
1113213211
*/
