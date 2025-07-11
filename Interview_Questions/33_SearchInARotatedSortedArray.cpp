/*
 * Difficulty Medium
 * There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, 
 * nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k],
 * nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated
 * at pivot index 3 and become [4,5,6,7,0,1,2]. Given the array nums after the possible rotation and an integer target, 
 * return the index of target if it is in nums, or -1 if it is not in nums.
 * 
 * You must write an algorithm with O(log n) runtime complexity.
 * 
 * Example 1:
 * Input: nums = [4,5,6,7,0,1,2], target = 0
 * Output: 4
 * 
 * Example 2:
 * Input: nums = [4,5,6,7,0,1,2], target = 3
 * Output: -1
 * 
 * Example 3:
 * Input: nums = [1], target = 0
 * Output: -1
 * 
 * Constraints:
 * 1 <= nums.length <= 5000
 * -104 <= nums[i] <= 104
 * All values of nums are unique.
 * nums is an ascending array that is possibly rotated.
 * -104 <= target <= 104
*/

#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:

    pair<int,int>  assessForRotation(vector<int>& nums, int lastIndex) {
        //! No rotation in effect
        if (lastIndex >= nums.size()) return {-1,-1};
        //! Calculate next move
        int newIndex = ((nums.size() - lastIndex) / 2) + lastIndex;
        if (newIndex == lastIndex) return {-1,-1};
        //! Rotation discovered?
        if (nums[newIndex] < nums[lastIndex]) return {lastIndex, newIndex};
        //! Press on
        return assessForRotation(nums, newIndex);
    }

    pair<int,int> findRotationEdge(vector<int>& nums, pair<int,int>rangePair) {
        if (rangePair.second - rangePair.first == 1) return rangePair;

        int newIndex = ((rangePair.second - rangePair.first) / 2) + rangePair.first;
        if (nums[newIndex] < nums[rangePair.first])
            return findRotationEdge(nums, {rangePair.first, newIndex});
        
        return findRotationEdge(nums, {newIndex, rangePair.second});
    }

    int logSearch(vector<int>& nums, int target, pair<int,int>rangePair, int index) {
        //! Safety - target not in nums
        if (index < 0 || index > rangePair.second) return -1;
        //! Last check
        if (rangePair.first == rangePair.second) {
            if (nums[rangePair.first] == target) return rangePair.first; //! Target acquired
            else return -1; //! Target not in nums
        }

        //! Check for match
        if (nums[index] == target) return index;

        //! Reduce & Continue Search
        if (nums[index] > target) { //! Go Left
            return logSearch(nums, target, {rangePair.first, index-1}, ((index - rangePair.first) / 2) + rangePair.first);
        } else { //! Go Right
            return logSearch(nums, target, {index + 1, rangePair.second}, ((rangePair.second - (index + 1)) / 2) + (index + 1));
        }
    }

    int search(vector<int>& nums, int target) {
        //! Trivial case
        if (nums.size() == 1) {
            if (nums[0] == target) return 0;
            else return -1;
        }

        //! Identify if there is a rotation at play - logarithmically
        pair<int,int> rotation = assessForRotation(nums, 0);
        
        //! Rotation at play? Determine partition - logarithmically
        //! Log search each subarray
        if (rotation.first != -1) {
            pair<int,int> rotationEdges = findRotationEdge(nums, rotation);

            int leftResult = logSearch(nums, target, {0,rotationEdges.first}, rotationEdges.first / 2);
            int rightResult = logSearch(nums, target, {rotationEdges.second, nums.size()-1}, ((nums.size() - rotationEdges.second)/2) + rotationEdges.second);

            return (leftResult != -1) ? leftResult : rightResult;
        }
        
        //! No rotation at play input is sorted in ascending order - normal log search
        return logSearch(nums, target, {0, nums.size()-1}, nums.size() / 2);
    }
};

int main() {
    Solution s;
    vector<int> v = {4,5,6,7,0,1,2};
    cout << "Answer is: " << 4 << ", result is: " << s.search(v, 0) << endl;
    cout << "Answer is: " << -1 << ", result is: " << s.search(v, 3) << endl;
    cout << "Answer is: " << 2 << ", result is: " << s.search(v, 6) << endl;
    v = {1};
    cout << "Answer is: " << -1 << ", result is: " << s.search(v, 0) << endl;
    cout << "Answer is: " << 0 << ", result is: " << s.search(v, 1) << endl;
    v = {2, 1};
    cout << "Answer is: " << 0 << ", result is: " << s.search(v, 2) << endl;
    cout << "Answer is: " << 1 << ", result is: " << s.search(v, 1) << endl;
    cout << "Answer is: " << -1 << ", result is: " << s.search(v, 3) << endl;
    v = {1, 3};
    cout << "Answer is: " << -1 << ", result is: " << s.search(v, 0) << endl;
    v = {3,5,1};
    cout << "Answer is: " << -1 << ", result is: " << s.search(v, 0) << endl;
    v = {5,1,2,3,4};
    cout << "Answer is: " << 4 << ", result is: " << s.search(v, 4) << endl;
    v = {1,3};
    cout << "Answer is: " << -1 << ", result is: " << s.search(v, 2) << endl;
    v = {7,8,1,2,3,4,5,6};
    cout << "Answer is: " << 3 << ", result is: " << s.search(v, 2) << endl;
}
