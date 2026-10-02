class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxP = 0
        while right<len(prices):
            profit = prices[right]-prices[left]
            maxP = max(profit, maxP)
            if profit>=0:
                right+=1
            else:
                left=right
                right+=1
        return maxP
        


        