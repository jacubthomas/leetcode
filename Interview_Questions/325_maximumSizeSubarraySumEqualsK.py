class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Compute the prefix sum - zero-based approach
        # Also a hashmap of values to index locations for quick lookup
        prefixSum = 0
        hashMap = {}

        # Look at all the differences between sums equal to k, choose the largest subarray summing to k
        # Because we pre-summed everything, we don't have add an additional loop here adding values between i & j
        maxLengthSumToK = 0
        for i in range(0, len(nums)):
            # Sum of all values leading up to this index
            prefixSum += nums[i]
            # All values leading to this index sum to target k - this is the largest subarray summing to k
            # [X][X][X][X][X][][][][][][][][][][][][]
            if prefixSum == k:
                maxLengthSumToK = i + 1
            # Check if there is a subarray of sums that amount to k from what we've already seen
            # [][][X][X][X][X][][][][][][][][][][][]
            valueToFind = prefixSum - k
            if valueToFind in hashMap:
                # Take longest subarray - what we have already, or the length of the newly detected summing to k
                maxLengthSumToK = max(maxLengthSumToK, i - hashMap[valueToFind])
            
            # Mark this Prefix Sum as seen, iff this is the first time we've come across it
            # We're looking for the longest subarray, so need to update with later detected index
            if prefixSum not in hashMap:
                hashMap[prefixSum] = i
            
        return maxLengthSumToK
