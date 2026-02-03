class Solution {
public:
    vector<vector<int>> directions = {{0,-1}, {1,0}, {0,1}, {-1,0}};

    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        set<vector<int>> visited;
        vector<int> startCoord = {sr, sc};
        const int floodPixel = image[sr][sc];
        dfsFloodFill(image, {sr, sc}, color, floodPixel, visited);
        return image;
    }

    void dfsFloodFill(vector<vector<int>>& image,                       //! Image under process
                      vector<int> coordinate,                           //! Coordinate under flood consideration
                      const int color,                                  //! New color being flooded
                      const int floodPixel,                             //! The first pixel we call flood on is the color we will flood
                      set<vector<int>>& visited) {                      //! Preventing infinity loops
        if (visited.find(coordinate) != visited.end()) return;          //! Already colored

        visited.insert(coordinate);                                     //! Track visit                                   
        image[coordinate[0]][coordinate[1]] = color;                    //! Color

        for (vector<int> direction: directions) {                       //! All directions
            vector<int> nextCoordinate = {                              //! For readability
                coordinate[0]+direction[0],
                coordinate[1]+direction[1]
                };
            if (nextCoordinate[0] >= 0 && nextCoordinate[0] < image.size()    &&   //! Within Bounds
                nextCoordinate[1] >= 0 && nextCoordinate[1] < image[0].size() &&   //! Within Bounds continued
                image[nextCoordinate[0]][nextCoordinate[1]] == floodPixel)       //! Only flooding connected 'floodPixel's
                dfsFloodFill(image, nextCoordinate, color, floodPixel, visited);    //! Recurse
        }
    }
};
