class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        //! Trivial case: mat is empty
        if (mat.size() == 0) return mat;

        //! Convenience variables
        const int m = mat.size();
        const int n = mat[0].size();

        //! Special case when mat has no 0-squares
        bool atLeastOneZeroExists = false;

        //! Gather all 0-squares
        //! BFS from them is more efficient than from each 1 square
        queue<pair<int,int>> q;
        for (int row=0; row < m; row++) {
            for (int col=0; col < n; col++) {
                if (mat[row][col] == 0) {
                    q.push({row, col});
                    atLeastOneZeroExists = true;
                }
            }
        }
        //! No zeroes exist! return -1 all squares
        if (!atLeastOneZeroExists) {
            for (int row=0; row < m; row++)
                for (int col=0; col < n; col++)
                    mat[row][col] = -1;
                    
            return mat;
        }

        //! Perform BFS - update squares as we go along
        int stepCount = 1;
        while (!q.empty()) {
            const int levelSize = q.size();

            for (int i=0; i<levelSize; i++) {
                pair<int,int> coordinate = q.front();
                q.pop();
                for (const pair<int,int> direction: directions) {
                    pair<int,int> nextCoordinate = { 
                        coordinate.first + direction.first,
                        coordinate.second + direction.second
                    };
                    //! With BFS, we only need to account for 1-squares
                    //! If we've already arrived, we've already updated shortest path
                    if (isInbounds(nextCoordinate, m, n) && 
                        mat[nextCoordinate.first][nextCoordinate.second] == 1) {
                        //! We handle special condition for all step squares, so as to avoid double queue
                        mat[nextCoordinate.first][nextCoordinate.second] = stepCount == 1 ? -1 : stepCount;
                        q.push(nextCoordinate);
                    }
                }
            }
            stepCount++;
        }

        //! Convert all true 1-step squares to reflect such
        for (int row=0; row < m; row++)
            for (int col=0; col < n; col++)
                if (mat[row][col] == -1)
                    mat[row][col] = 1;

        return mat;
    }

private:
    const vector<pair<int,int>> directions = {
        {-1,0}, {1,0}, {0,-1}, {0,1}
    };

    const bool isInbounds(const pair<int,int> coordinate, const int rowSize, const int colSize) {
        return (coordinate.first > -1 &&
                coordinate.first < rowSize &&
                coordinate.second > -1 &&
                coordinate.second < colSize);
    }

};
