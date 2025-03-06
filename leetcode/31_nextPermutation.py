'''
Difficulty Medium
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
'''

from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return
        # Start from the tail of the list
        left, right = len(nums)-2, len(nums)-1
        while 0 <= left < right < len(nums):
            # Easy swap [1, 2, 3] ------> [1, 3, 2]
            if nums[left] < nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                break
            else: # [_, _, _, x, 3, 2]
                goingRight = False
                # Assess elements to the right (pointer) for the lowest possible swap
                while left - 1 >= 0 and nums[right] > nums[left-1]: # [1, 3, 2] ------> [2, 1, 3]
                    goingRight = True
                    # Room to keep looking right
                    if right+1 < len(nums) and nums[right+1] > nums[left-1]:
                        right += 1
                    # Out of runaway to the right
                    else:
                        break
                # Best swap is to the right (pointer)
                if goingRight:
                    nums[left-1], nums[right] = nums[right], nums[left-1]
                    break
                # Best swap is adjacent (left pointer)
                if left - 1 >= 0 and nums[left] > nums[left-1]: # [2, 3, 1] ------> [3, 1, 2]
                    nums[left-1], nums[left] = nums[left], nums[left-1]
                    break
                else: # No swap yet, continue assessing
                    left -= 1
                    right -= 1 

        # Bubble sort following array
        for i in range(left, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums

s = Solution()
assert s.nextPermutation([1,2,3]) == [1,3,2]
assert s.nextPermutation([3,2,1]) == [1,2,3]
assert s.nextPermutation([1,1,5]) == [1,5,1]
assert s.nextPermutation([1,4,3,2,5]) == [1,4,3,5,2]
assert s.nextPermutation([1,3,2]) == [2,1,3]
assert s.nextPermutation([5,4,7,5,3,2]) == [5,5,2,3,4,7]
assert s.nextPermutation([2,2,7,5,4,3,2,2,1]) == [2,3,1,2,2,2,4,5,7]
