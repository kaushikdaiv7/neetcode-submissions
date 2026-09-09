class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        buying_price = prices[0]

        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - buying_price)
            if buying_price > prices[i]:
                buying_price = prices[i]

        return max_profit