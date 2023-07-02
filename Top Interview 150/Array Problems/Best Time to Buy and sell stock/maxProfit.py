#Problem description:You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the 
# future to sell that stock.Return the maximum profit you can achieve from this transaction. If you cannot achieve 
# any profit, return 0.


#url:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

def maxProfit(self, prices) -> int:
    """ Time Complexity: O(n)
        Space Complexity: O(1)
    """
    
    l,r=0,1 # left = buy and right = sell
    maxP=0

    while r< len(prices):
        # profitable
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP,profit)
        else:
            l = r
        
        r+=1
    return maxP
