#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int countTriangles = 0;

        std::sort(nums.begin(), nums.end(), std::less<int>());

        for (int i = nums.size()-1; i > 1; i--) {
            int left = 0;
            int right = i - 1;
            while (left < right) { //! Probably want something here to detect edge
                const int sum = nums[left] + nums[right];
                if (sum > nums[i]) {
                    countTriangles += (right - left);
                    right--;
                } else {
                    left++;
                }
            }
        }
        
        return countTriangles;
    }
};

int main() {
    Solution s;
    vector<int> vecNums = {11,4,9,6,15,18};
    int triangles = s.triangleNumber(vecNums);
    return 0;
}
