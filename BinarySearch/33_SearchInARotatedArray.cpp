
////////////////////////////////////
////// Solution 1
////////////////////////////////////
class Solution {
public:
    /*! 
     * We will leverage the fact that the arrays is sorted ascending before * and after pivot. Calling this func, we know a pivot exists. We will
     * conduct a binary search to find the smallest value less than the last
     * num in nums.
     * i.e. [4,5,6,7,0,1,2] - find smallest num < 2
     */
    int binarySearchForPivotPoint(vector<int>& vecIntNums, const int ciTargetHint) {
        int iLeft = 0;
        int iRight = vecIntNums.size() - 2;           //! Don't need to reconsider iTargetHint
        int iSmallestValueIndex = vecIntNums.size()-1;
        while (iLeft <= iRight) {
            int iMid = iLeft + ((iRight - iLeft) / 2);
            //! Left of Pivot, shrink to right
            if (vecIntNums[iMid] > ciTargetHint) {
                iLeft = iMid + 1;
            } else if (vecIntNums[iMid] < ciTargetHint) { //! Right of Pivot, shrink to left
                iRight = iMid - 1;
                if (vecIntNums[iSmallestValueIndex] > vecIntNums[iMid]) //! There are no duplicates, so should never need an else ... == case
                    iSmallestValueIndex = iMid;
            } //! There are no duplicates, so should never need an else ... == case
        }
        return iSmallestValueIndex;
    }

    int binarySearch(vector<int>& vecIntNums, 
                    const int ciTarget, 
                    int iLeft, 
                    int iRight) {
        while (iLeft <= iRight) {
            int iMid = iLeft + ((iRight-iLeft) / 2);
            if (vecIntNums[iMid] == ciTarget) return iMid;  //! Found our target
            else if (vecIntNums[iMid] < ciTarget) { //! Left of target, shrink to right
                iLeft = iMid + 1;
            } else { //! Right of target, shrink to left
                iRight = iMid - 1;
            }
        }
        return -1;  //! Target not present
    }

    int search(vector<int>& nums, int target) {
        //! Trivial case(s):
        if (nums.size() == 0) return -1;
        if (nums.size() == 1) {
            if (nums[0] == target) return 0;
            else return -1;
        }

        const bool cbPivotExists = nums[0] > nums[nums.size()-1];

        //! Pivot exists, search the section appropriate to pivot and target
        if (cbPivotExists) {
            const int ciPivotIndex = binarySearchForPivotPoint(nums, nums[nums.size()-1]);
            //! We can do one section elimination here
            if (target >= nums[0]) { //! Search left of pivot
                return binarySearch(nums, target, 0, ciPivotIndex-1);
            } else { //! Search right, including pivot point
                return binarySearch(nums, target, ciPivotIndex, nums.size()-1);
            }
        }
        //! No pivot point, just binary search nums entire
        return binarySearch(nums, target, 0, nums.size()-1);
    }
};

////////////////////////////////////
////// Solution 2
////////////////////////////////////
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
}
