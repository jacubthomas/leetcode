
# Given an array, rotate the array to the right by k steps,
# where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

# Follow up:
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

from typing import List


def rotate(nums: List[int], k) -> None:
    if k == 0 or k % len(nums) == 0:
        return
    while k >= len(nums):
        print(k)
        k -= len(nums)

    begin = nums[len(nums)-k:]
    end = nums[:len(nums)-k]

    i = 0
    if i < len(nums):
        for j in begin:
            nums[i] = j
            i += 1
        for k in end:
            nums[i] = k
            i += 1

# TEST CASES
# nums = list(range(1, 8))
# print(nums)
# rotate(nums, 3)
# print(nums)
# print("-----------------------------")
# nums = [-1, -100, 3, 99]
# print(nums)
# rotate(nums, 2)
# print(nums)
# print("-----------------------------")
# nums = [1, 2]
# print(nums)
# rotate(nums, 1)
# print(nums)
# print("-----------------------------")
# nums = [1, 2]
# print(nums)
# rotate(nums, 3)
# print(nums)
# print("-----------------------------")
# nums = [1, 2, 3]
# print(nums)
# rotate(nums, 2)
# print(nums)
# print("-----------------------------")
# nums = [1, 2, 3, 4]
# print(nums)
# rotate(nums, 3)
# print(nums)
# print("-----------------------------")
# nums = [1, 2, 3, 4, 5]
# print(nums)
# rotate(nums, 3)
# print(nums)

# easiest solution, but not an in place modify
# def rotate(nums: List[int], k):
#     l = nums[k+1::] + nums[:k+1]
#     return l
