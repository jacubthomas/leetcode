#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    /*! 
     * You are given a 1-indexed integer array nums of length n.
     * An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
     * Return the sum of the squares of all special elements of nums.
     *
     * `example 1:` nums = [1,2,3,4]
     * (1*1) + (2*2) + (4*4)
     *   1  +    4   +   16          = 21
     *
     * `example 2:` nums = [2,7,1,19,18,3]
     * (2*2) + (7*7) + (1*1) + (3*3)
     *   4   +   49   +   1   +  9   = 63
     */
    int sumOfSquares(vector<int>& nums) {
        const int n = nums.size();
        int sum = 0;
        for (int i=0; i<n; i++)
        {
            //! Special Element - nums[i]
            if (n % (i+1) == 0) //! i+1, 1st element equals 0th index and so on...
                sum += (pow(nums[i],2));
        }
        return sum;
    }
};
