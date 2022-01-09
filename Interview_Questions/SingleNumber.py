# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one. You must implement a solution with a linear runtime complexity
# and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104

# Each element in the array appears twice except for one element which appears only once.

from typing import List


def singleNumber(nums: List[int]) -> int:
    n = len(nums)
    r = nums[0]
    for i in range(1, n):
        r = r ^ nums[i]

    return r

    # Solution 1
    # if len(nums) == 0:
    #     return None
    # doubles_check = []
    # for i in range(len(nums)):
    #     if nums[i] in doubles_check:
    #         doubles_check.remove(nums[i])
    #     else:
    #         doubles_check.append(nums[i])
    # return doubles_check[0]


# TEST CASES
# l = [2, 1, 4, 2, 3, 4, 1]
# print(singleNumber(l))

# l = []
# print(singleNumber(l))

# l = [1]
# print(singleNumber(l))
