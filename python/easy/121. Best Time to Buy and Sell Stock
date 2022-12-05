class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = prices[0]
        diff_price = 0
        for price in prices:
            if price < min_price:
                min_price = price
                max_price = price
            elif price > max_price:
                max_price = price
                if diff_price < max_price - min_price:
                    diff_price = max_price - min_price
        return diff_price
