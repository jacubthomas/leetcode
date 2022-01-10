
# Given an integer array nums, move all 0's to the end of it while maintaining the
# relative order of the non-zero elements. Note that you must do this in-place without
# making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

# Follow up: Could you minimize the total number of operations done?

from typing import List


def moveZeroes(nums: List[int]) -> None:
    i = 0
    zeroes = 0
    for x in nums:
        if x != 0:
            nums[i] = x
            i += 1
        else:
            zeroes += 1
    while i < len(nums):
        nums[i] = 0
        i += 1

# TEST CASES
# l = [0, 4, 100, 0, -1, 2, 3, 0, 7]
# print(l)
# moveZeroes(l)
# print(l)
