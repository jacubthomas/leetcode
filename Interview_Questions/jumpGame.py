'''
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
'''

from typing import List


# Dynamic Programming Top-Down
# Not the optimal approach, but it is the strategy I was going for

class Solution:

    # Memoize where we've already been so we don't repeat efforts
    def __init__ (self):
        self.canReachFinalStep = {}
        self.nums = []
    

    def canJumpHelp(self, currentIndex: int) -> bool:
        # Current index is at the goal final step, memoize and return true
        if currentIndex == len(self.nums)-1:
            self.canReachFinalStep[currentIndex] = True
            return True

        # We have already evaluated this position before, return that memoized result
        if currentIndex in self.canReachFinalStep:
            return self.canReachFinalStep[currentIndex]
        
        # Consider all possible jumps within bounds of input
        jumps = min(self.nums[currentIndex], len(self.nums) - currentIndex - 1) 
        # Current position is guilty until proven innocent 
        self.canReachFinalStep[currentIndex] = False
        while jumps > 0:
            # Recurse and track result
            self.canReachFinalStep[currentIndex] = self.canJumpHelp(currentIndex + jumps)
            # Short circuit if we found a path
            if self.canReachFinalStep[currentIndex] == True:
                return True
            jumps -= 1
        # No path found and all jump possibilities have been exhausted
        return False

    def canJump(self, nums: List[int]) -> bool:
        # Keep track of input so we don't have to keep passing it in calls
        self.nums = nums
        self.canJumpHelp(0)
        return self.canReachFinalStep[0]


s = Solution()

print (s.canJump([2, 3, 1, 1, 4]))
s.canReachFinalStep.clear()
print (s.canJump([3, 2, 1, 0, 4]))