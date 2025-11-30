/*!
* Difficulty Medium
* You are given an m x n grid rooms initialized with these three possible values.
* -1 A wall or an obstacle.
* 0 A gate.
* INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
* Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
* 
* Example 1:
* Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
* Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
* 
* Example 2:
* Input: rooms = [[-1]]
* Output: [[-1]]
* 
* Constraints:
* m == rooms.length
* n == rooms[i].length
* 1 <= m, n <= 250
* rooms[i][j] is -1, 0, or 231 - 1.
*/

#include <deque>
#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

struct Coordinate {
    int row;
    int col;
    int step;
};

class Solution {
    public:
        //! Might be useful to return an int, to return more information
        bool canIStepDirection(vector<vector<int>>& rooms, const int direction, const Coordinate coordinate) {
            //! Up
            if (direction == 0) {
                return (coordinate.row - 1 >= 0 &&  //! On map
                       rooms[coordinate.row-1][coordinate.col] != -1); //! Not a barrier
            } else if (direction == 1) { //! Right
                return (coordinate.col + 1 < rooms[0].size() &&  //! On map
                       rooms[coordinate.row][coordinate.col+1] != -1); //! Not a barrier
            } else if (direction == 2) { //! Down
                return (coordinate.row + 1 < rooms.size() &&  //! On map
                       rooms[coordinate.row+1][coordinate.col] != -1); //! Not a barrier
            } else { //! Left
                return (coordinate.col - 1 >= 0 && //! On map
                        rooms[coordinate.row][coordinate.col-1] != -1); //! Not a barrier
            }
        }
    
        /*! IDEA
        * Let's do a BFS from each gate, counting our steps
        * When we reach an empty room, if room is unmarked or steps is less than current
        * count, then we update.
        */
        void wallsAndGates(vector<vector<int>>& rooms) {
            const int m = rooms.size();
            const int n = rooms[0].size();
            
            //! Gather all the gates
            vector<Coordinate> vecGates;
            for (int i=0; i < m; i++) {
                for (int j=0; j < n; j++) {
                    if (rooms[i][j] == 0) vecGates.push_back(Coordinate{i,j,0});
                }
            }
    
            //! BFS - considering at least each gate
            BFS(rooms, vecGates, m, n);
        }
    
        void BFS(vector<vector<int>>& rooms, vector<Coordinate> vecGateCoordinates, const int m, const int n) {
            const int up = 0;
            const int right = 1;
            const int down = 2;
            const int left = 3;
            vector<vector<bool>> vecVisited(m, vector<bool>(n, false));
    
            deque<Coordinate> deqCoordinates;
            for (Coordinate coord: vecGateCoordinates)
                deqCoordinates.push_back(coord);
    
            while (deqCoordinates.size() > 0) {
                Coordinate coordinate = deqCoordinates.front();
                //! 3rd element is the step count! Right now, we aren't tracking our steps accurately
                deqCoordinates.pop_front();
                // stepCount++;
                if (canIStepDirection(rooms, up, coordinate)) {
                    Coordinate nextCoordinate = Coordinate{coordinate.row-1, coordinate.col, coordinate.step+1};
                    int nextCoordinateValue = rooms[nextCoordinate.row][nextCoordinate.col];
                    if (nextCoordinateValue != 0 && //! Don't need to add gates
                        (nextCoordinateValue == 2147483647 || //! Unmarked empty room
                         nextCoordinateValue > nextCoordinate.step)) { //! New shortest path
                        if (vecVisited[nextCoordinate.row][nextCoordinate.col] == false) {
                            deqCoordinates.push_back(nextCoordinate);
                            vecVisited[nextCoordinate.row][nextCoordinate.col] = true;
                        }
                        rooms[nextCoordinate.row][nextCoordinate.col] = nextCoordinate.step;
                    }
                }
    
                if (canIStepDirection(rooms, right, coordinate)) {
                    Coordinate nextCoordinate = Coordinate {coordinate.row, coordinate.col+1, coordinate.step+1};
                    int nextCoordinateValue = rooms[nextCoordinate.row][nextCoordinate.col];
                    if (nextCoordinateValue != 0 && //! Don't need to add gates
                        (nextCoordinateValue == 2147483647 || //! Unmarked empty room
                         nextCoordinateValue > nextCoordinate.step)) { //! New shortest path
                        if (vecVisited[nextCoordinate.row][nextCoordinate.col] == false) {
                            deqCoordinates.push_back(nextCoordinate);
                            vecVisited[nextCoordinate.row][nextCoordinate.col] = true;
                        }
                        rooms[nextCoordinate.row][nextCoordinate.col] = nextCoordinate.step;
                    }
                }
    
                if (canIStepDirection(rooms, down, coordinate)) {
                    Coordinate nextCoordinate = Coordinate {coordinate.row+1, coordinate.col, coordinate.step+1};
                    int nextCoordinateValue = rooms[nextCoordinate.row][nextCoordinate.col];
                    if (nextCoordinateValue != 0 && //! Don't need to add gates
                        (nextCoordinateValue == 2147483647 || //! Unmarked empty room
                         nextCoordinateValue > nextCoordinate.step)) { //! New shortest path
                        if (vecVisited[nextCoordinate.row][nextCoordinate.col] == false) {
                            deqCoordinates.push_back(nextCoordinate);
                            vecVisited[nextCoordinate.row][nextCoordinate.col] = true;
                        }
                        rooms[nextCoordinate.row][nextCoordinate.col] = nextCoordinate.step;
                    }
                }
    
                if (canIStepDirection(rooms, left, coordinate)) {
                    Coordinate nextCoordinate = Coordinate {coordinate.row, coordinate.col-1, coordinate.step+1 };
                    int nextCoordinateValue = rooms[nextCoordinate.row][nextCoordinate.col];
                    if (nextCoordinateValue != 0 && //! Don't need to add gates
                        (nextCoordinateValue == 2147483647 || //! Unmarked empty room
                         nextCoordinateValue > nextCoordinate.step)) { //! New shortest path
                        if (vecVisited[nextCoordinate.row][nextCoordinate.col] == false) {
                            deqCoordinates.push_back(nextCoordinate);
                            vecVisited[nextCoordinate.row][nextCoordinate.col] = true;
                        }
                        rooms[nextCoordinate.row][nextCoordinate.col] = nextCoordinate.step;
                    }
                }
            }
        }
    };

    int main() {
        Solution s;
        vector<vector<int>> rooms = {
            {2147483647,    0,         2147483647},
            {2147483647,    -1,        2147483647},
            {2147483647,    2147483647, 0}
        };
        s.wallsAndGates(rooms);
        return 0;
    }
