'''
One-pass algorithm using only constant extra space

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same
color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to
represent the color red, white, and blue, respectively. You must solve this problem without using the library's 
sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
'''

from typing import List

class Solution:

    # Do not return anything, modify nums in-place instead.
    def sortColors(self, nums: List[int]) -> None:
        
        # For readability's sake
        red, white, blue = 0, 1, 2

        # Gameplan, move all red to front, redIndex
        # Move all blue to end, blue index
        redIndex, blueIndex = 0, len(nums) - 1

        i = 0

        while (i < len(nums)):
            # Stop early
            if i >= blueIndex and nums[i] == blue:
                return
            # Identified red, swap current element to redIndex 
            elif nums[i] == red:
                nums[i], nums[redIndex] = nums[redIndex], nums[i]
                # Don't advance if the new current element is something other than red
                if i == redIndex:
                    i += 1
                redIndex += 1
            # Identified white, do nothing and press on
            elif nums[i] == white:
                i += 1
            # Identified blue, swap current element to blueIndex
            else:
                nums[i], nums[blueIndex] = nums[blueIndex], nums[i]
                # Don't advance if the new current element is something other than blue
                if i == blueIndex:
                    i += 1
                blueIndex -= 1

    def printItems(self, nums: List[int]) -> None:
        for i in  nums:
            print(i, end=' ')
        print()


s = Solution()

nums = [1,2,0]
s.printItems(nums)
s.sortColors(nums)
s.printItems(nums)

print()

nums = [2,0,2,1,1,0]
s.printItems(nums)
s.sortColors(nums)
s.printItems(nums)
