class Solution {
public:
                                    //!  UP    RIGHT   DOWN   LEFT
    vector<vector<int>> directions = { {-1,0}, {0,1}, {1,0}, {0,-1} };
    int numIslands(vector<vector<char>>& grid) {
        const int rows = grid.size();
        const int cols = (rows > 0) ? grid[0].size() : 0;
        
        //! Initialize O(1) lookup visited
        vector<vector<int>> visited = vector<vector<int>>(rows, vector<int>(cols, 0));

        int islands = 0;
        for (int row=0; row < rows; row++) {
            for (int col=0; col < cols; col++) {
                vector<int> coordinate = {row, col};
                if (grid[row][col] == '1' &&  //! Land Ho!
                    visited[row][col] == 0) //! Unvisited
                {
                    vector<int> coordinate = {row, col};
                    dfs(grid, visited, coordinate);
                    islands++;
                }
            }
        }

        return islands;
    }
    void dfs(vector<vector<char>>& grid, vector<vector<int>>& visited, vector<int> coordinate) {
        //! Bounds check
        if (coordinate[0] < 0 || coordinate[0] >= grid.size() ||
            coordinate[1] < 0 || coordinate[1] >= grid[0].size())
            return;

        //! Don't care about ocean
        if (grid[coordinate[0]][coordinate[1]] == '0')
            return;
        //! Don't revisit
        if (visited[coordinate[0]][coordinate[1]] == 1) 
            return;
        //! Mark visit
        visited[coordinate[0]][coordinate[1]] = 1;
        //! Look in all compass directions 
        for (vector<int> direction: directions) {
            vector<int> nextCoordinate = { 
                                            coordinate[0] + direction[0], 
                                            coordinate[1] + direction[1] 
                                        };
            dfs(grid, visited, nextCoordinate);
        }
    }
};
