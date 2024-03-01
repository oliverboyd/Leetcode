https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices):
        max = 0
        x = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            if prices[i] > x:
                x = prices[i]
            diff = x - prices[i]
            if diff > max:
                max = diff
        return max