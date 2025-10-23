class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices : return 0

        minp = float('inf')
        maxp  = 0

        for i in range(len(prices)):
            minp = min(minp,prices[i])
            cp = prices[i] - minp
            maxp = max(maxp, cp)
        return maxp
