#include <iostream>
#include <cmath>    //! abs()
#include <string>   //! std::to_string()
#include <vector>

using namespace std;

class Solution {
public:

/*!
 * Helper func
 * we need to cast these nums to a larger bit representation to handle edge cases
 */
const bool peekedNumIsContiguous(const int64_t num, 
                                 const int64_t peekedNum) const {
    return abs(peekedNum - num) == 1;
}

/*!
 * Note inputs are sorted, unique
 * So we need not consider range mins, only if the next number is continuous
 */
    vector<string> summaryRanges(vector<int>& nums) {
        //! Output
        vector<string> vecResults;
        
        //! Trivial case
        if (nums.size() == 0) return vecResults;

        //! Look for contiguous ranges
        int i = 0;
        while (i < nums.size()) {
            //! We will always include the starting num
            std::string subResult = std::to_string(nums[i]);
            //! Look for range following starting num
            int j = i;
            
            while (j+1 < nums.size() &&                          //! Valid peek index
                    peekedNumIsContiguous(nums[j], nums[j+1]))   //! Peeked num is continuous
                        j++;

            //! At least one num following starting num, so we have a range
            if (i != j && 
                j < nums.size())
                subResult += "->" + std::to_string(nums[j]);

            //! Append result
            vecResults.push_back(subResult);

            //! Increment for next iteration
            i = j + 1;
        }
        return vecResults;
    }
};
