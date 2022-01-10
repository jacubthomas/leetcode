
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result
# must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

from typing import List


# Initial Solution
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums3 = []
    i = 0
    while i < len(nums1):
        if nums1[i] in nums2:
            nums3.append(nums1[i])
            nums2.remove(nums1[i])
            nums1.remove(nums1[i])
        else:
            i += 1
    return nums3

# Solution 2, Sorted
# def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    # nums1, nums2 = sorted(nums1), sorted(nums2)
    # nums3 = []
    # i, j = 0, 0
    # while True:
    #     if(i == len(nums1) or j == len(nums2)):
    #         break
    #     if nums1[i] > nums2[j]:
    #         j += 1
    #     elif nums1[i] < nums2[j]:
    #         i += 1
    #     else:
    #         nums3.append(nums1[i])
    #         i += 1
    #         j += 1
    # return nums3


# TEST CASES
# l1 = [1, 2, 2, 3, 3, 1]
# l2 = [2, 3]
# print(intersect(l1, l2))

# l1 = [1, 2, 2, 3, 3, 1]
# l2 = [2]
# print(intersect(l1, l2))

# l1 = [1, 2, 2, 3, 3, 1]
# l2 = [2, 2]
# print(intersect(l1, l2))

# l1 = [4, 9, 5]
# l2 = [9, 4, 9, 8, 4]
# print(intersect(l1, l2))

# l1 = [9, 4, 9, 8, 4]
# l2 = [4, 9, 5]
# print(intersect(l1, l2))

# handy expression [x for x in nums2 if x in nums1]
