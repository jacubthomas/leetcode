class Solution {
public:

    //! Optimal
    void moveZeroes(vector<int>& nums) {
        int nextNonZero = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                swap(nums[nextNonZero], nums[i]);
                nextNonZero++;
            }
        }
    }

    //! Sub-Optimal
    void moveZeroes2(vector<int>& nums) {
        for (int i = 0; i < nums.size()-1; i++) {
            if (nums[i] != 0) continue;
            int left = i;
            int right = i+1;
            while (right < nums.size()) {
                if (nums[left] == 0 && nums[right] != 0) {
                    std::swap(nums[left], nums[right]);
                    break;
                }
                else { right++; }
            }
        }
    }
};
