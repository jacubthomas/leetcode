# You are given an integer array prices where prices[i] is the price of a given stock on
# the ith day. On each day, you may decide to buy and/or sell the stock. You can only 
# hold at most one share of the stock at any time. However, you can buy it then 
# immediately sell it on the same day. Find and return the maximum profit you can achieve.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to 
# achieve the maximum profit of 0.
 
# Constraints:
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104

from typing import List

def maxProfit(prices: List[int]) -> int:
    total = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            total += prices[i+1] - prices[i]
    return total


## TEST CASES 
# l = list(range(0, 100))
# print(maxProfit(l))
# print(maxProfit([1, 1, 2, 0, 1]))
# print(maxProfit([1, 6, 2, 4]))
# print(maxProfit([7, 1, 5, 3, 6, 4]))
# print(maxProfit([1, 1, 1, 2]))
# print(maxProfit([1, 2, 3, 4, 5]))
# print(maxProfit([7, 6, 5]))

# Recursive solution, needs memoization to speed up for larger lengths
######################################################################
# def help(prices: List[int], day, owns, current, sum):
#         if day == len(prices):
#             return sum

#         # can either sell off or hold for day
#         elif owns:
#             # sell or hold
#             return max(help(prices, day+1, False,  0, sum + prices[day]),  # sell
#                        help(prices, day+1, True, current, sum))  # hold

#         # can either buy up or hold for day
#         buy = prices[day] * (-1)
#         current = prices[day]
#         return max(help(prices, day+1, True, current, sum+buy),  # buy
#                    help(prices, day+1, False, 0, sum))  # hold

#     return max(help(prices, 0, True, prices[0], prices[0]*(-1)),
#                help(prices, 0, False, 0, 0))
######################################################################