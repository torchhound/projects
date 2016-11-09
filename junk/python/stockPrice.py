def maxProfit(stock_prices_yesterday):
    mx = max(stock_prices_yesterday)
    mn = min(stock_prices_yesterday)
    mxI = stock_price_yesterday.index(mx)
    mnI = stock_price_yesterday.index(mn)
    if mxI > mnI:
        return mx - mn
    else:
        #find second largest max or min perhaps based on index
