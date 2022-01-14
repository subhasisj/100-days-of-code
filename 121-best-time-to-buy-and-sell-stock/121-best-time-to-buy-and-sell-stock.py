class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0] # Consider the 1st element in the list to be the lowest
        max_profit = 0
        for i in range(1,len(prices)): # Start chaecking from the 2nd elements onwards
            current_price = prices[i]
            if current_price < lowest_price:
                lowest_price = current_price # if the current price is less than lowest price then make it the lowest price 
            else:
                max_profit = max(max_profit, current_price - lowest_price) # Otherwise, we know that we have the lowest price and we 
                                                                            # will try to maximise the profits
            
        return max_profit