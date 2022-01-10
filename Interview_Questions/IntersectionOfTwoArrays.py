from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    # nums1.sort()
    # nums2.sort()
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


l1 = [1, 2, 2, 3, 3, 1]
l2 = [2, 3]
print(intersect(l1, l2))

l1 = [1, 2, 2, 3, 3, 1]
l2 = [2]
print(intersect(l1, l2))

l1 = [1, 2, 2, 3, 3, 1]
l2 = [2, 2]
print(intersect(l1, l2))

l1 = [4, 9, 5]
l2 = [9, 4, 9, 8, 4]
print(intersect(l1, l2))

l1 = [9, 4, 9, 8, 4]
l2 = [4, 9, 5]
print(intersect(l1, l2))

# nums3 = [x for x in nums2 if x in nums1]
