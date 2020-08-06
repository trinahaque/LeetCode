# peak valley method
# adding the height, not slope

#Time Complexity: O(n) --> loops through the whole array
#Space Complexity: O(1) --> only one variable created
def maxProfit(prices):
    #max profit will be 0 if stock prices keep going down
    max_profit = 0
    for i in range(1, len(prices)):
        #it means stock price is going up
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit

nums = [7,1,5,3,6,4]
print(maxProfit(nums))

nums = [7,6,4,3,1]
print(maxProfit(nums))