class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        maxProfit returns difference in prices[i] where maximum profit can be obtained 
            returns 0 if no profit can be made
        prices array (1 <= prices.length <= 105), (0 <= prices[i] <= 104)
            list of prices on consecutive days
        """
        min_price = prices[0]                                   #set min_price to 1st value in prices    
        max_price = prices[0]                                   #set max_price ot 1st value in prices
        diff_price = 0
        for price in prices:                                    
            if price < min_price:                               #iterate through prices
                min_price = price                               #assign lowest value in prices to min_price
                max_price = price                               #assign lowest value in prices to max_price
            elif price > max_price:
                max_price = price                               #assign highest value in prices to max_price
                if diff_price < max_price - min_price:
                    diff_price = max_price - min_price          #calculate difference in prices
        return diff_price
