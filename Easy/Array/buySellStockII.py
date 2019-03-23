# Time Complxity: O(n) --> one for loop
# Space Complexity: O(1) --> constant for one variable
def buySellStockII(prices):
        sum = 0
        if len(prices) < 2:
            return 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                sum += prices[i+1] - prices[i]
        return sum

# Edde cases

# 1) Empty array
prices = []
print(buySellStockII(prices))

# 2) Only 1 value
prices = [7]
print(buySellStockII(prices))

# 3) All values going down
prices = [7,6,4,3,1]
print(buySellStockII(prices))

# 4) Multiple transaction options
prices = [7,1,5,3,6,4]
print(buySellStockII(prices))