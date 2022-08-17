# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
import numpy as np
from typing import List

class Solution:

    # finds continguous target values given an index and returns all indices as list
    def determineRange (self, nums: List[int], target: int, index: int) -> List[int]:
        i = j = index
        length = len (nums)

        while nums[i] == target:
            if i > 0 and nums[i-1] == target:
                i -= 1
            else:
                break
        while nums[j] == target:
            if j < len (nums) - 1 and nums[j+1] == target:
                j += 1
            else:
                break
        return [i,j]
    
    # finds/rules out target in O(log n)
    def binarysearch (self, nums: List[int], target: int, lower: int, upper):
        index = (lower+upper)//2
        if lower >= upper and nums[index] != target:
            return -1

        if nums[index] == target:
            return index
        
        if nums[index] > target: 
            upper = index - 1 
        else: 
            lower = index + 1

        return self.binarysearch(nums, target, lower, upper)

    # driver code
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            # edge case, empty list
            if len (nums) == 0:
                return [-1,-1]
            # find index with target value
            index = self.binarysearch (nums, target, 0, len (nums)-1)
            if index == -1:         # nothing found
                return [-1,-1]
            else:                   # at least one value
                return self.determineRange (nums, target, index)
    
    
    # An alternate solution using numpy
    def searchRange2 (self, nums: List[int], target: int) -> List[int]:
            # print (nums)
            arr = np.array(nums)
            # print (arr)
            arr = np.where (arr == target)
            indices = list (arr[0])
            # print (indices)
            if len (indices) == 0:
                return [-1,-1]
            
            sol = [indices[0], indices[0] + len (indices) - 1]
            return sol

# SOME TEST CASES

s = Solution ()

nums = []
a0 = s.searchRange (nums, 0)
print (a0)

nums = [1]
a1 = s.searchRange (nums, 1)
print (a1)

nums = [0, 1, 2]
a2 = s.searchRange (nums, 0)
print (a2)

nums = [0,1,2,3]
a3 = s.searchRange (nums, 2)
print (a3)

nums = list (range (0,8))
a4 = s.searchRange (nums, 5)
print (a4)

nums = [0] * 100
a5 = s.searchRange (nums, 0)
print (a5)

# Again with numpy solution

nums = []
a0 = s.searchRange2 (nums, 0)
print (a0)

nums = [1]
a1 = s.searchRange2 (nums, 1)
print (a1)

nums = [0, 1, 2]
a2 = s.searchRange2 (nums, 0)
print (a2)

nums = [0,1,2,3]
a3 = s.searchRange2 (nums, 2)
print (a3)

nums = list (range (0,8))
a4 = s.searchRange2 (nums, 5)
print (a4)

nums = [0] * 100
a5 = s.searchRange2 (nums, 0)
print (a5)