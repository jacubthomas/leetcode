/*!
* Given an integer input array heights representing the heights of vertical lines, 
* write a function that returns the maximum area of water that can be contained by
* two of the lines (and the x-axis). The function should take in an array of 
* integers and return an integer.
*/

#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int max_area(vector<int> heights) {
        int left = 0;
        int right = heights.size()-1;
        int maxArea = -1;
        while (left < right) {
            const int area = min(heights[left], heights[right]) * (right-left);
            maxArea = max(maxArea, area);
            if (heights[left] > heights[right]) right--;
            else left++;
        }
        return maxArea;
    }
};

int main() {
    Solution s;
    // vector<int> vecInput = {1,8,6,2,5,4,8,3,7};   //! Test Case 1
    vector<int> vecInput = {3,4,1,2,2,4,1,3,2};      //! Test Case 2
    cout << s.max_area(vecInput) << endl;
    return 0;
}
