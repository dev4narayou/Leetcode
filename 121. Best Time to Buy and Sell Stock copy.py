
def maxProfit(prices) -> int:
    # alternative approach
    l, r = 0, 1
    highest_profit = 0
    
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            highest_profit = max(profit, highest_profit)
        else:
            l = r
        r += 1
    return highest_profit
    
if __name__ == "__main__":
    print(maxProfit([2,1,2,1,0,1,2]))
                


