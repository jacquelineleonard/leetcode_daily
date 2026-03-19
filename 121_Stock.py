class Solution(object):
    def maxProfit(self, prices):
        minp = float('inf')
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < minp:
                minp = prices[i]
            elif prices[i] - minp > maxprofit:
                maxprofit = prices[i] - minp

        return maxprofit
    
#both r O(n)