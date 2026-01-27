#include <algorithm>
class Solution {
public:
    int findKthLargest(vector<int> nums, int k) {
        //! Create a max-heap from vector
        priority_queue<int, vector<int>, std::less<int>> maxHeap; //! max by less, min by greater
        maxHeap = priority_queue<int, vector<int>, std::less<int>>(nums.begin(), nums.end());
        
        //! Trivial - edge case, k = 0
        if (k == 0) return maxHeap.top();

        //! Pop the heap k-1 times
        while (k != 1) {
            maxHeap.pop();
            k--;
        }

        //! Peak at the heap top and return
        return maxHeap.top();
    }
};
