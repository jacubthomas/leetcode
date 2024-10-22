from typing import List

class Solution:
    
    # Merge-sort
    def sortArray(self, nums: List[int]) -> List[int]:
        # base case - sublist is sorted
        # Plus, D&C divides to n >= 2
        if len(nums) <= 1:
            return nums
        
        # Divide the (sub)list in two
        pivot = int(len(nums) / 2)
        
        # Recursively call until sublists reach base case
        leftList = self.sortArray(nums[:pivot])
        rightList = self.sortArray(nums[pivot:])
        
        # Merge two sorted sublists into one
        return self.merge(leftList, rightList)
    
    def merge(self, leftList: List[int], rightList: List[int]) -> List[int]:
        
        # Recombine sublists into this sorted result
        mergedList = []
        
        # Merge in smallest elements from each presorted sublist one at a time
        while len(leftList) > 0 and len(rightList) > 0:
            if leftList[0] < rightList[0]:
                mergedList.append(leftList[0])
                leftList.pop(0)
            else:
                mergedList.append(rightList[0])
                rightList.pop(0)
        
        # Add remaining elements from left and right to back of merged list
        mergedList.extend(leftList)
        mergedList.extend(rightList)
        
        return mergedList

s = Solution()

print (s.sortArray([5,3,4,1]))