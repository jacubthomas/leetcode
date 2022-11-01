# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
from typing import List
class Solution:
    def __init__(self) -> None:
        self.max_seen = -1   # memoize largest potential selling point seen
        self.best_profit = 0 # to be returned, initialized to handle unprofitable

    def maxProfit(self, prices: List[int]) -> int:
        index = len (prices) - 1
        if index == 0:
            return 0
        self.max_seen = prices[index]
        # start from back of prices
        return self.help (prices, index-1)

    def help (self, prices, index):
        if index < 0:
            return self.best_profit
        
        elif self.max_seen - prices[index] > self.best_profit:
            self.best_profit = self.max_seen - prices[index]
        
        if prices[index] > self.max_seen:
            self.max_seen = prices[index]
        
        return self.help (prices, index-1)

S = Solution()
S2 = Solution()
S3 = Solution()
print (S.maxProfit ([7,1,5,3,6,4]))
print (S2.maxProfit ([7,6,4,3,1]))
print (S3.maxProfit ([3,2,6,5,0,3]))

    # def help (self, prices, index):
    #     if index < 0:
    #         if self.sell[1] == (-1) or self.buy[1] == (-1) or self.sell[0] - self.buy[0] < 0:
    #             return 0
    #         return self.sell[0] - self.buy[0]
        
    #     if prices[index] < self.buy[0]:
    #         self.buy = (prices[index], index)
        
    #     if prices[index+1] > self.sell[0] and self.buy[1] < index + 1:
    #         self.sell = (prices[index + 1], index + 1)

    #     return self.help (prices, index-1)