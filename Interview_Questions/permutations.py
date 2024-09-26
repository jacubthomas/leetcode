'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

from typing import List

class Solution:
    def permuteHelp(self, nums:List[int], permutation:List[int]):
        # We have reached a complete permutation, return in format [[1,2,3]]
        if len(nums) == 0:
            return [permutation]
        
        # Gather all returned permutations from deeper recursive calls here
        permutations = []

        # Consider each remaining num
        for num in nums:
            # We want local copies to work with
            subsetNums, copyPermutation= nums.copy(), permutation.copy()
            # Add this num to the permutation under construction
            copyPermutation.append(num)
            # Remove this num from list of future options in recursive calls
            # It's now part of the permutation in construction
            subsetNums.remove(num)
            # Recurse
            permutations.extend(self.permuteHelp(subsetNums, copyPermutation))
        return permutations
            

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permuteHelp(nums, [])
    

s = Solution()

print (s.permute([1,2,3,4]))