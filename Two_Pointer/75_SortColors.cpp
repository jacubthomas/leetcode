class Solution {
public:
    void sortColors(vector<int>& nums) {
        int nextGoodSpot = 0;
        for(int color=0; color < 3; color++) { //! For each color, moveColor
            moveColor(nums, color, nextGoodSpot);
        }
    }

    void moveColor(vector<int>& nums, int color, int &nextGoodSpot) {
        //! Look at every value from the nextGoodSpot on
        for (int i=nextGoodSpot; i < nums.size(); i++) {
            //! Move color to the next good spot
            if (nums[i] == color)
                std::swap(nums[i], nums[nextGoodSpot++]);
        }

    }
};
