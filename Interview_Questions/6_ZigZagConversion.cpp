#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        string solution = "";
		for (int row=0; row < numRows; row++) {
			int down = (numRows - row - 1) * 2;
			int up = row * 2;
			if (!up) up = down;
            else if (!down) down = up;
			zigZag(s, solution, row, down, up, true);
		}
		return solution;
    }

	void zigZag(string& s, string& solution, int index, int down, int up, bool isDown) {
		if (index >= s.length()) return;

        solution += s[index];

        if (isDown && down == 0) return;
        if (!isDown && up == 0) return; 

		index += isDown ? down : up;
		zigZag(s,solution,index,down,up,!isDown);
	}
};

int main() {
        Solution sol;
        // string result = sol.convert("A", 1);
        // string result = sol.convert("AB", 1);
        // string result = sol.convert("PAYPALISHIRING", 3);
        string result = sol.convert("PAYPALISHIRING", 7);
        cout << result << endl;
        return 0;
}
