class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            current_price = prices[i]
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                if diff > maxProfit:
                    maxProfit = diff
        return maxProfit