/*
 * Difficulty Medium
 * Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
 * Each row must contain the digits 1-9 without repetition.
 * Each column must contain the digits 1-9 without repetition.
 * Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
 * 
 * Note:
 * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
 * Only the filled cells need to be validated according to the mentioned rules.
 * 
 * Example 1:
 * Input: board = 
 * [["5","3",".",".","7",".",".",".","."]
 * ,["6",".",".","1","9","5",".",".","."]
 * ,[".","9","8",".",".",".",".","6","."]
 * ,["8",".",".",".","6",".",".",".","3"]
 * ,["4",".",".","8",".","3",".",".","1"]
 * ,["7",".",".",".","2",".",".",".","6"]
 * ,[".","6",".",".",".",".","2","8","."]
 * ,[".",".",".","4","1","9",".",".","5"]
 * ,[".",".",".",".","8",".",".","7","9"]]
 * Output: true
 * 
 * Example 2:
 * Input: board = 
 * [["8","3",".",".","7",".",".",".","."]
 * ,["6",".",".","1","9","5",".",".","."]
 * ,[".","9","8",".",".",".",".","6","."]
 * ,["8",".",".",".","6",".",".",".","3"]
 * ,["4",".",".","8",".","3",".",".","1"]
 * ,["7",".",".",".","2",".",".",".","6"]
 * ,[".","6",".",".",".",".","2","8","."]
 * ,[".",".",".","4","1","9",".",".","5"]
 * ,[".",".",".",".","8",".",".","7","9"]]
 * Output: false
 * Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the
 * top left 3x3 sub-box, it is invalid.
 *  
 * Constraints:
 * board.length == 9
 * board[i].length == 9
 * board[i][j] is a digit 1-9 or '.'.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isValidLinear(vector<vector<char>>& board, int index, bool isRow)
    {
        if (index < 0 || index > 8) return false;

        //! Track what's been used in row/col - repeats are invalid
        vector<bool> vecNumUsed = {false, false, false, false, false, false, false, false, false, false};

        if (isRow) {
            for (int col=0; col < 9; col++) {
                if (board[index][col] == '.') continue;
                int numericalValue = board[index][col] - '0'; //! Convert ascii to int
                if (vecNumUsed.at(numericalValue)) return false;
                vecNumUsed[numericalValue] = true;
            }
        } else {
            for (int row=0; row < 9; row++) {
                if (board[row][index] == '.') continue;
                int numericalValue = board[row][index] - '0'; //! Convert ascii to int
                if (vecNumUsed.at(numericalValue)) return false;
                vecNumUsed[numericalValue] = true;
            }
        }
        return true;
    }

    bool hasValidBoxes(vector<vector<char>>& board) {

        for (int boxOffset=0; boxOffset < 9; boxOffset++) {
            //! Track what's been used in row/col - repeats are invalid
            vector<bool> vecNumUsed = {false, false, false, false, false, false, false, false, false, false};
            for (int row=0; row < 3; row++) {
                for (int col=0; col < 3; col++) {
                    if (boxOffset < 3) {
                        if (board[row][col + (boxOffset*3)] == '.') continue;
                        int numericalValue = board[row][col + (boxOffset*3)] - '0'; //! Convert ascii to int
                        if (vecNumUsed.at(numericalValue)) 
                            return false;
                        vecNumUsed[numericalValue] = true;
                    }
                    else if (boxOffset < 6) {
                        if (board[row + 3][col + (boxOffset - 3) * 3] == '.') continue;
                        int numericalValue = board[row + 3][col + (boxOffset - 3)*3] - '0'; //! Convert ascii to int
                        if (vecNumUsed.at(numericalValue)) 
                            return false;
                        vecNumUsed[numericalValue] = true;
                    } else {
                        if (board[row + 6][col + (boxOffset - 6) * 3] == '.') continue;
                        int numericalValue = board[row + 6][col + (boxOffset - 6) * 3] - '0'; //! Convert ascii to int
                        if (vecNumUsed.at(numericalValue)) 
                            return false;
                        vecNumUsed[numericalValue] = true;
                    }
                }
            }
        }
        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        bool result;
        for (int i = 0; i < 9; i++) {
            result = isValidLinear(board, i, true);
            if (result == false) return false;
            result = isValidLinear(board, i, false);
            if (result == false) return false;
        }
        return hasValidBoxes(board);
    }
};

int main() {
    Solution s;
    vector<vector<char>> board = {{'5','3','.','.','7','.','.','.','.'},
                            {'6','.','.','1','9','5','.','.','.'},
                            {'.','9','8','.','.','.','.','6','.'},
                            {'8','.','.','.','6','.','.','.','3'},
                            {'4','.','.','8','.','3','.','.','1'},
                            {'7','.','.','.','2','.','.','.','6'},
                            {'.','6','.','.','.','.','2','8','.'},
                            {'.','.','.','4','1','9','.','.','5'},
                            {'.','.','.','.','8','.','.','7','9'}};
    cout << s.isValidSudoku(board) << endl;

    board = {{'8','3','.','.','7','.','.','.','.'}
            ,{'6','.','.','1','9','5','.','.','.'}
            ,{'.','9','8','.','.','.','.','6','.'}
            ,{'8','.','.','.','6','.','.','.','3'}
            ,{'4','.','.','8','.','3','.','.','1'}
            ,{'7','.','.','.','2','.','.','.','6'}
            ,{'.','6','.','.','.','.','2','8','.'}
            ,{'.','.','.','4','1','9','.','.','5'}
            ,{'.','.','.','.','8','.','.','7','9'}};
    cout << s.isValidSudoku(board) << endl;

}
