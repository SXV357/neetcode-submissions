class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if all(prices[i + 1] <= prices[i] for i in range(n - 1)):
            return 0
        
        max_profit = 0
        curr, left = 0, 0

        for right in range(1, n):
            curr = prices[right] - prices[left]
            if curr <= 0:
                left = right
            
            max_profit = max(max_profit, curr)
        
        return max_profit
