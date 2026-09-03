class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        for i in range(len(prices)):
            sell = prices[i]
            res = max(sell - buy, res)

            buy = min(buy, prices[i])
        
        return res
