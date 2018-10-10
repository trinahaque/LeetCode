# LeetCode: 121: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Given an array with stock prices, find the maximum profit
# Can not sell a stock before buying one

def maxProfit(prices):
    if len(prices) < 1:
        return 0
    profit = 0
    buy = 0
    #sell = 0

    for i in range(1, len(prices)):
        if (prices[i] < prices[buy]):
            buy = i
        elif (prices[i] - prices[buy]) > profit:
            profit = prices[i] - prices[buy]
            #sell = i
    return profit

# Edge Cases:
# 1) Stock prices can keep going down. In that case, max profit will be 0
# 2) Array can be empty
# 3) Array can have one value, it will return profit = 0 in that case


nums = [7, 1, 5, 3, 6, 4]
nums2 = [7, 6, 4, 3, 1, 8, 12]

print(maxProfit(nums2))