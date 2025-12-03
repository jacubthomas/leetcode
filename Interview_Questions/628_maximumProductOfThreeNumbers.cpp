class Solution {
public:
    int recurseMaxProduct(vector<int>& nums, vector<int> vecNumsGathered, int product) {
        //! Base case
        if (vecNumsGathered.size() == 3) return vecNumsGathered[0] * vecNumsGathered[1] * vecNumsGathered[2];

        //! Any product should beat this
        int maxProduct = -1000000000;
        for (int i=0; i < nums.size(); i++) {
            //! We will mark used elements by temp setting them to invalid input parameter value
            if (nums[i] == -1001)
                continue;
            //! Save for later restore
            int tempNum = nums[i];
            //! Mark element as used
            nums[i] = -1001;
            vecNumsGathered.push_back(tempNum);
            //! Recurse and assess for new max
            maxProduct = max(maxProduct, recurseMaxProduct(nums, vecNumsGathered, product));
            
            //! Restore
            vecNumsGathered.pop_back();
            nums[i] = tempNum;
        }
        return maxProduct;
    }

    int maximumProduct(vector<int>& nums) {
        //! Trivial case
        if (nums.size() == 3) return nums[0] * nums[1] * nums[2];
        //! Sort in descending order
        std::sort(nums.begin(), nums.end(), std::greater<int>());

        //! Gather edges - both (+) & (-) values could be useful
        //! But we can also shrink the problem space
        vector<int> newNums = {nums[0], nums[1], nums[2]};
        int tailPointer = nums.size()-1;
        while (tailPointer > 2 && newNums.size() < 6) {
            newNums.push_back(nums[tailPointer--]);
        }

        //! Call helper to solve for us
        vector<int> numsGathered = {};
        return recurseMaxProduct(newNums, numsGathered, 0);
    }
};
