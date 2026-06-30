# revisiting - almost had right idea last time and even got my code working but had a small logical issue
# causing me to be stuck

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        naive: for every possible buy price compute profit against all other selling prices
        and return maximum profit - O(n^2)

        selling has to be some day in future
        ex: [10, 1, 5, 6, 7, 1]
             0   1  2  3  4  5
        
        the largest price on a day after index 5 is 0
        largest price on a day after index 4 is 1
        largest price on day after index 3 is 7
        "" ...... after index 2 is 7
        "" ...... after index 1 is 7
        "" ...... after index 0 is 7

        we compute maximums for all indices then do one sweep to compute
        O(n) time but takes O(n) space
        '''

        n = len(prices)
        
        left, max_profit = 0, 0
        for right in range(1, n):
            # left pointer reflects day on which we buy neetcoin and right ptr reflects
            # day on which we sell it 
            profit = prices[right] - prices[left]

            # idea is we want to try and achieve a non-zero profit so if this is the case
            # its hurting gains (we don't want to really use the left pointer or wherever it's
            # at as a buying day since its not optimal so we shift it to where right is and try
            # using current location as potential buy date)
            if profit <= 0:
                left = right
            else:
                # we update as normal because there's still a chance it could go higher
                max_profit = max(max_profit, profit)
        
        return max_profit