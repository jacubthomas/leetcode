# Given an integer array nums sorted in non-decreasing order, remove the duplicates
# in-place such that each unique element appears only once. The relative order of the
# elements should be kept the same. Since it is impossible to change the length of
# the array in some languages, you must instead have the result be placed in the first
# part of the array nums. More formally, if there are k elements after removing the
# duplicates, then the first k elements of nums should hold the final result. It does
# not matter what you leave beyond the first k elements. Return k after placing the
# final result in the first k slots of nums. Do not allocate extra space for another
# array. You must do this by modifying the input array in-place with O(1) extra
# memory. Custom Judge: The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums
# being 1 and 2 respectively. It does not matter what you leave beyond the returned k
# (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:
# 0 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.
from typing import List


def removeDuplicates(nums: List[int]):
    # index and return count
    index = 0
    duplicates = 0

    # loop through length of current list
    # if list length shrinks w/ every duplicate discovered
    while index < (len(nums) - duplicates):

        # peek variable and duplicate flag
        recon = 1
        doubles = False

        # capture count of streak duplicates
        # don't look beyond (current) end of list
        while index + recon < len(nums)-duplicates and nums[index] >= nums[index + recon]:
            recon += 1
            doubles = True
        # if flagged
        if doubles:
            duplicates += recon - 1
            i = 1
            j = index + recon
            # overwrite list duplicates w/ latter list elements
            while j < len(nums):
                nums[index + i] = nums[j]
                i += 1
                j += 1
        # increment loop
        index += 1
    return len(nums) - duplicates


# # TEST CASES
# l = [1, 1, 2]
# idx = removeDuplicates(l)
# print("idx = ", idx)
# i = 0
# while i < idx:
#     print(l[i])
#     i += 1

# print("-----------------------------")

# l = [0, 0, 1, 1, 1, 2, 2, 3, 4]
# idx = removeDuplicates(l)
# print("idx = ", idx)
# i = 0
# while i < idx:
#     print(l[i])
#     i += 1

# print("-----------------------------")


# l = [1, 1, 1]
# idx = removeDuplicates(l)
# i = 0
# print("idx = ", idx)
# while i < idx:
#     print(l[i])
#     i += 1

# print("-----------------------------")


# l = [1, 2, 2, 3]
# idx = removeDuplicates(l)
# print("idx = ", idx)
# i = 0
# while i < idx:
#     print(l[i])
#     i += 1
