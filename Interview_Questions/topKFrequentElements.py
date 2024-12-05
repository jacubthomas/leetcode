from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        leaderlist = []
        for num in nums:
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
            
        leaderlist = sorted(numMap.items(), key=lambda x:x[1], reverse=True)
        
        i = 0
        for numTuple in leaderlist:
            if i == k:
                break
            print (f'{numTuple[0]} : {numTuple[1]}')
            leaderlist.append(numTuple[0])
            i += 1
        return leaderlist[len(leaderlist)-k:]

s = Solution()

print(s.topKFrequent([4,3,2,4,1,-6,7,-6,4,-6,5,0], 2))