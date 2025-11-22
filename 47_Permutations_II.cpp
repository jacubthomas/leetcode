/*!
* Difficulty Medium
* Given a collection of numbers, nums, that might contain duplicates, 
* return all possible unique permutations in any order.
* 
* Example 1:
* Input: nums = [1,1,2]
* Output:
* [[1,1,2],
*  [1,2,1],
*  [2,1,1]]
*  
* Example 2:
* Input: nums = [1,2,3]
* Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
* 
* Constraints:
* 1 <= nums.length <= 8
* -10 <= nums[i] <= 10
*/

#include <cstdlib>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
    public:
        vector<vector<int>> permuteUnique(vector<int>& nums) {
            vector<int> vecna = {};                             //! For individual permutations
            set<vector<int>> setSolution;                       //! Ensures only unique permutations
            recurseHelp(nums, nums.size(), vecna, setSolution);

            vector<vector<int>> vecSolution;                    //! Convert to expected return type
            for (vector<int> innerVec: setSolution)
                vecSolution.push_back(innerVec);

            return vecSolution;
        }
    
       void recurseHelp(vector<int>& nums, 
                        const int length,
                        vector<int> vecna, 
                        set<vector<int>>& setSolution) {
            //! Permutation found
            if (vecna.size() == length) {
                setSolution.insert(vecna);
                    return;
            }
            
            //! Explore all permutatations
            for (int i=0; i < length; i++) {
                    if (nums[i] > -11)
                    {
                        vecna.push_back(nums[i]);
                        const int currentNum = nums[i];
                        nums[i] = -11;
                        recurseHelp(nums, length, vecna, setSolution);
                        nums[i] = currentNum;
                        vecna.pop_back();
                    }
            }
       }
    };

    int main() {
        Solution sol;
        vector<int> nums = {1, 1, 2};
        vector<vector<int>> result = sol.permuteUnique(nums);
        for (vector<int> innerVec: result)
        {  
            cout << "[ ";
            for(int i: innerVec)
                cout << i;
            cout << "]" << endl;
        }
        return 0;
}
