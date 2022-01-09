
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
    if k == 0:
        return
    while k >= len(nums):
        k -= len(nums)
    end = begin = []
    for i in range(k):

        # if k+1 == len(nums) and len(nums) % 2 == 1:
        #     end = nums[:k-1]
        #     begin = nums[k-1:]
        # elif k+1 == len(nums) and len(nums) % 2 == 0:
        #     end = nums[:k-2]
        #     begin = nums[k-2:]
        # el
        if len(nums) % 2 == 1:
            end = nums[:i+1]
            begin = nums[i+1:]
        else:
            end = nums[:i]
            begin = nums[i:]
    j = 0
    for i in begin:
        nums[j] = i
        j += 1
    for i in end:
        nums[j] = i
        j += 1


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

# Solution 2: inefficient for large list
# def rotate(nums: List[int], k) -> None:
# length = len(nums)
# for i in range(k):
#     j = 0
#     temp = temp2 = nums[0]
#     while j+1 < length:
#         temp2 = nums[j+1]
#         nums[j+1] = temp
#         temp = temp2
#         j += 1
#     nums[0] = temp

#   0   1   2   3   4   5
#   1   20  3   7   88  0
#   i   +1  +2  +3
#       1   20  3   7   88
