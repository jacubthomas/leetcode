
# def help(prices: List[int], memo: List[int], day):
#     # base case, outside date range
#     if day >= len(prices):
#         return 0
#     elif day == len(prices)-1:
#         return prices[day]
#     # if precomputed
#     elif memo[day] != -1:
#         return memo[day]

#     memo[day] = max(0, help(prices, memo, day+1) - prices[day],
#                          )
from typing import List


def maxProfit(prices: List[int]) -> int:
    total = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            total += prices[i+1] - prices[i]
    return total


l = list(range(0, 100))
print(maxProfit(l))
print(maxProfit([1, 1, 2, 0, 1]))
print(maxProfit([1, 6, 2, 4]))
print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 1, 1, 2]))
print(maxProfit([1, 2, 3, 4, 5]))
print(maxProfit([7, 6, 5]))

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