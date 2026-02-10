class Solution {
public:
    vector<pair<int,int>> directions = {
        {-1, 0}, {0, 1}, {1, 0}, {0, -1}
    };
    int orangesRotting(vector<vector<int>>& grid) {
        int minutes = -1;
        //! Trivial case(s)
        if (grid.size() == 0) return minutes;

        queue<pair<int,int>> qCoordinates;
        bool hasFreshOranges = false;
        //! Search the grid entire for initial "Rotten" oranges - queue them up
        for (int row=0; row < grid.size(); row++) {
            for (int col=0; col < grid[0].size(); col++) {
                if (grid[row][col] == 2)
                    qCoordinates.push({row, col});
                if (grid[row][col] == 1)
                    hasFreshOranges = true;
            }
        }

        //! No rotten oranges in grid to kick things off
        if (qCoordinates.empty()) {
            if (hasFreshOranges) return -1;     //! But fresh oranges present - invalid puzzle
            else return 0;                      //! No fresh oranges either - valid puzzle
        }
        
        //! BFS - tracking level size as we go
        while (!qCoordinates.empty()) {

            const int currentLevelSize = qCoordinates.size();
            minutes++;
            
            for (int i=0; i < currentLevelSize; i++) {
                pair<int,int> coordinate = qCoordinates.front();
                qCoordinates.pop();
                for (pair<int,int> direction : directions) {
                    pair<int,int> nextCoordinate = {
                        coordinate.first + direction.first,
                        coordinate.second + direction.second
                        };

                    if (nextCoordinate.first > -1 && 
                        nextCoordinate.first < grid.size() && 
                        nextCoordinate.second > -1 && 
                        nextCoordinate.second < grid[0].size() &&
                        grid[nextCoordinate.first][nextCoordinate.second] == 1){
                            qCoordinates.push(nextCoordinate);
                            grid[nextCoordinate.first][nextCoordinate.second] = 2;
                        }
                }
            }
        }

        //! Check for any unreached - still fresh - fruit
        for (int row=0; row < grid.size(); row++) {
            for (int col=0; col < grid[0].size(); col++) {
                if (grid[row][col] == 1)
                    return -1;
            }
        }

        return minutes;
    }
};
