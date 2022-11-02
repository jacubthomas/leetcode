# House Robber
# Solution
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

from typing import List
class Solution:
    def __init__ (self):
        self.memo = {}
        self.nums = []

    def rob(self, nums: List[int]) -> int:
        _length_ = len (nums)
        # State 0
        if _length_ == 1:
            return nums[0]
        # State 1
        elif _length_ == 2:
            return max (nums[0], nums[1])
        # Setup for State 2
        self.nums = nums
        self.memo[_length_-1] = nums[_length_-1]
        self.memo[_length_-2] = nums[_length_-2]
        return self.help (0)
    
    def help (self, index):
        # prevent double work
        if index in self.memo:
            return self.memo[index]
        
        # consider best option of starting one house prior or here - order matters
        best_grab = max (
            self.help (index + 1),
            (self.nums[index] + self.help (index + 2))
        )

        # update our memo with the best, since we can only see 2 houses back
        self.memo[index+1] = max ( 
            self.help (index + 1),
            self.help (index + 2)
        )

        return best_grab


S = Solution()
S1 = Solution()
S2 = Solution()
print (S.rob ([1,2,3,1]))
print (S1.rob ([2,7,9,3,1]))
print (S2.rob ([2,1,1,2]))
 

S3 = Solution()
S4 = Solution()
print (S3.rob ([1]))
print (S4.rob ([1,4]))


S5 = Solution()
print (S5.rob ())