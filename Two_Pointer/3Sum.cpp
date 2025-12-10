#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int> nums) {
        //! Sort in ascending order
        std::sort(nums.begin(), nums.end(), std::less<int>());
        
        //! Stores function output
        vector<vector<int>> vecVecResult;

        for (int i=0; i < nums.size()-2; i++) {

            //! Skip duplicate values for the first element to avoid duplicate triplets
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            //! Establish `Two Pointers`
            int left = i+1;
            int right = nums.size()-1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    vecVecResult.push_back({nums[i], nums[left], nums[right]});

                    //! Skip duplicate values by moving to new values - i.e. (1)  1   1   2
                    //! Note that we always stop one short            - i.e.  1   1  (1)  2
                    while (left < right && nums[left] == nums[left +1]) left++; //! Left
                    while (left < right && nums[right] == nums[right-1]) right--; //! Right
                    //! No matter what, always condense left and right pointers
                    left++;
                    right--;

                } else if (sum < 0) {
                    left++;
                } else { //! sum > 0
                    right--;
                }
            }
        }

        return vecVecResult;
};

int main() {
    Solution s;
    vector<int> vecInput = {-1,0,1,2,-1,-4};
    vector<vector<int>> vecVecResult = s.threeSum(vecInput);
    for (vector<int> vec3Sum: vecVecResult)
    cout << "{ " << vec3Sum[0] << ", " << vec3Sum[1] << ", " << vec3Sum[2] <<  " }" << endl;
    return 0;
}
