class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        # Build max_after array
        max_after = [0] * (len(prices) - 1)
        max_after[-1] = prices[-1]
        
        for idx in reversed(range(len(max_after) - 1)):
            max_after[idx] = max(prices[idx + 1], max_after[idx + 1])
        
        # Find max profit
        max_profit = 0
        
        for idx in range(len(prices) - 1):
            max_profit = max(max_profit, max_after[idx] - prices[idx])
        
        return max_profit
