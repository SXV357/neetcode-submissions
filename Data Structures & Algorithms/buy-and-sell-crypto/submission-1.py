class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        suffix = [0] * n
        curr_max = 0
        for i in range(n - 1, -1, -1):
            suffix[i] = curr_max
            curr_max = max(curr_max, prices[i])
        
        max_profit = 0
        for j in range(n):
            max_profit = max(max_profit, suffix[j] - prices[j])
        
        return max_profit