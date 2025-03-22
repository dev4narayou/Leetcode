
def maxProfit(prices) -> int:
    highest_profit = 0
    low = None
    high = None
    profit = None

    for price in prices:
        if low is None:
            low = price
        elif price < low:
            profit = high - low
            highest_profit = profit if profit > highest_profit else highest_profit
            low = price
            high = price
            continue
        if high is None:
            high = price
        elif price > high:
            high = price
    
    profit = high - low
    highest_profit = profit if profit > highest_profit else highest_profit

    return highest_profit


if __name__ == "__main__":
    print(maxProfit([2,1,2,1,0,1,2]))
                


