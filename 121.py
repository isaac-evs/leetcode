# Array Easy: 121 Best Time to Buy and Sell Stock

def solution(prices):

    # Prices lenght
    n = len(prices)

    # variables
    min_value = 0 # store index
    max_profit = 0

    # Iterate trough the lenght of the array
    for i in range(n):
        # if the value is smaller, store it to the min variable
        if prices[i] < prices[min_value]:
            min_value = i

        # Check the profit if you sell
        profit = prices[i] - prices[min_value]

        # Update max profit
        if profit > max_profit:
            max_profit = profit

    return max_profit

# Test
prices = [7,6,4,3,1]
result = solution(prices)
print(result)
