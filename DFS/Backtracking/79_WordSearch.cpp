#include <iostream>
#include <vector>

using namespace std;

//! Solution #2 - BETTER 
class Solution {
public:
    bool exist(vector<vector<char>> board, string word) {
        const int m = board.size();
        if (m == 0) return false;
        const int n = board[0].size();
        if (n == 0) return false;
        if (word.length() == 0) return false;
        
        bool foundMatch = false; 
        int currentWordIndex = 0;
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (word[currentWordIndex] == board[row][col]) {
                    //! Mark this spot as visited by temporarily marking with `#`
                    char temp = board[row][col];
                    board[row][col] = '#';
                    currentWordIndex += 1;
                    if (currentWordIndex == word.length()) return true;
                    //! Recursive search
                    const pair<int,int> coordinate = {row, col};
                    foundMatch = dfsBacktrack(board, coordinate, word, currentWordIndex);
                    if (foundMatch) return true;

                    //! Restore this board square as unexplored - another path may lead through it later
                    board[row][col] = temp;
                    currentWordIndex -= 1;
                }
            }
        }
        return false;
    }

private:

    bool dfsBacktrack(vector<vector<char>>& board, 
                   const pair<int,int> coordinate,
                   const string& target, 
                   int currentWordIndex) {

        int directionsChecked = 0;
        //! Search all posible directions
        for (pair<int, int> direction: directions) {
            const pair<int,int> nextCoordinate = {
                coordinate.first + direction.first,
                coordinate.second + direction.second
            };

            directionsChecked++;
            if (isInbounds(board, nextCoordinate) == false) continue;
            if (board[nextCoordinate.first][nextCoordinate.second] == '#') continue; //! Already visited
            if (board[nextCoordinate.first][nextCoordinate.second] == target[currentWordIndex]) {
                currentWordIndex++;
                if (currentWordIndex == target.length()) return true;
                //! Mark this spot as visited by temporarily marking with `#`
                char temp = board[nextCoordinate.first][nextCoordinate.second];
                board[nextCoordinate.first][nextCoordinate.second] = '#';

                bool matchFound = dfsBacktrack(board, nextCoordinate, target, currentWordIndex);
                if (matchFound) return true;

                //! Restore this board square as unexplored - another path may lead through it later
                board[nextCoordinate.first][nextCoordinate.second] = temp;
                currentWordIndex--;
            }
        }
        return false;
    }

    bool isInbounds(const vector<vector<char>>& board, const pair<int,int>& coordinate) {
        return (
            coordinate.first >= 0 &&
            coordinate.first < board.size() &&
            coordinate.second >= 0 &&
            coordinate.second < board[0].size()
        );
    }

    vector<pair<int, int>> directions = {
        {-1,0}, 
        {1,0}, 
        {0,-1}, 
        {0,1}
    };
};

int main() {
    Solution s;
    // vector<vector<char>> board = {
    //     {'b', 'l', 'c', 'h'},
    //     {'d', 'e', 'l', 't'},
    //     {'d', 'a', 'k', 'a'}
    // };
    // string word = "bleak";
    // vector<vector<char>> board = {
    //     {'a', 'b', 'c', 'e'},
    //     {'s', 'f', 'c', 's'},
    //     {'a', 'd', 'e', 'e'}
    // };
    // string word = "abcb";
    vector<vector<char>> board ={
        {'a','b','c','e'},
        {'s','f','e','s'},
        {'a','d','e','e'}
    };
    string word = "abceseeefs";
    cout << s.exist(board, word) << endl;
    return 0;
}


/*
FIRST WORKING SOLUTION

class Solution {
public:
    bool exist(vector<vector<char>> board, string word) {
        string result = "";
        const int m = board.size();
        if (m == 0) return false;
        const int n = board[0].size();
        if (n == 0) return false;
        if (word.length() == 0) return false;
        
        vector<vector<bool>> visited = vector<vector<bool>>(board.size(), vector<bool>(n, false));
        bool foundMatch = false; 
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                const pair<int,int> coordinate = {row, col};
                visited[row][col] = true;
                result += board[row][col];

                foundMatch = backtrack(board, visited, coordinate, word, result);
                if (foundMatch) return true;

                //! Backtrack
                result.pop_back();
                visited[row][col] = false;
            }
        }
        return false;
    }

private:

    bool backtrack(const vector<vector<char>>& board, 
                   vector<vector<bool>>& visited,
                   const pair<int,int> coordinate,
                   const string& target, 
                   string& word) {
        //! Current character compare to target, if no match, prune this path
        if (word[word.size()-1] != target[word.size()-1]) return false;
        else { //! Potential solution, compare and return results
            if (target.length() == word.length()) return true;
        }

        //! Consider all directions
        for (pair<int,int> direction: directions) {
            const pair<int,int> nextCoordinate = {
                coordinate.first + direction.first,
                coordinate.second + direction.second
            };
            if (isInbounds(board, nextCoordinate) &&
                visited[nextCoordinate.first][nextCoordinate.second] == false) {
                    //! Append new character and mark visited
                    word += board[nextCoordinate.first][nextCoordinate.second];
                    visited[nextCoordinate.first][nextCoordinate.second] = true;

                    bool foundMatch = backtrack(board, visited, nextCoordinate, target, word);
                    if (foundMatch) return true;

                    //! Backtrack
                    word.pop_back();
                    visited[nextCoordinate.first][nextCoordinate.second] = false;
                }
        }
        
        return false;
    }

    bool isInbounds(const vector<vector<char>>& board, const pair<int,int>& coordinate) {
        return (
            coordinate.first >= 0 &&
            coordinate.first < board.size() &&
            coordinate.second >= 0 &&
            coordinate.second < board[0].size()
        );
    }

    vector<pair<int, int>> directions = {
        {-1,0}, {1,0}, {0,-1}, {0,1}
    };
};
*/
