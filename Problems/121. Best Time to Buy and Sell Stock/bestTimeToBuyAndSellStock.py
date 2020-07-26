class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        min_buy = prices[0]

        for curr_price in prices:
            min_buy = min(min_buy, curr_price)
            profit_today = curr_price - min_buy
            max_profit = max(max_profit, profit_today)

        return max_profit