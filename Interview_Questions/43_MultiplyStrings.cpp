#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {

        if (num1 == "0" || num2 == "0") return "0";

        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        string result;
        if (num1.size() > num2.size()) num1.swap(num2);

        //! Do multiplications
        vector<string> vecResults;
        for (int i=0; i < num2.size(); i++) {
            int remainder = 0;
            vecResults.push_back("");
            for (int r=0; r<i; r++) {
                vecResults[i] += "0";
            }
            for (int j=0; j < num1.size(); j++) {
                int topDigit = num1[j] - '0';
                int bottomDigit = num2[i] - '0';
                int product = topDigit * bottomDigit + remainder;
                remainder = product / 10;
                vecResults[i] += to_string(product%10);
            }
            if (remainder > 0) vecResults[i] += to_string(remainder);
        }

        //! Sum products
        result = vecResults[0];
        for (int resultIdx=1; resultIdx < vecResults.size(); resultIdx++) {
            int remainder = 0;
            for (int digitIdx=0; digitIdx < vecResults[resultIdx].size(); digitIdx++) {
                int digit1 = 0;
                int digit2 = 0;
                if (digitIdx < result.size() && result.size() > 0)
                    digit1 = result[digitIdx] - '0';
                if (digitIdx < vecResults[resultIdx].size() && vecResults[resultIdx].size() > 0)
                    digit2 = vecResults[resultIdx][digitIdx] - '0';
                int sum = digit1 + digit2 + remainder;
                remainder = sum / 10;
                sum = sum % 10;
                if (digitIdx < result.size() && result.size() > 0)
                    result[digitIdx] = sum + '0';
                else
                    result += sum + '0';
            }
            if (remainder > 0) result += remainder +'0';
        }
        
        reverse(result.begin(), result.end());
        return result;
    }
};

int main() {
    Solution s;
    cout << "9 x 0 = " << s.multiply("9", "0") << endl; //! 0
    cout << "2 x 3 = " << s.multiply("2", "3") << endl; //! 6
    cout << "123 x 456 = " << s.multiply("123", "456") << endl; //! 56088
    cout << "999 x 999 = " << s.multiply("999", "999") << endl; //! 998001
    cout << "123456789 x 987654321 = " << s.multiply("123456789", "987654321") << endl; //! "121932631112635269"
}
