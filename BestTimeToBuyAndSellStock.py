########## Time Complexity: O(n) ########## Space Complexity: O(1) ##########
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max_price = prices[0]
        profit = 0
        
        for right in range(len(prices)):
            
            if prices[right] < min_price:
                max_price = prices[right]
                min_price = prices[right]
            
            if prices[right] > max_price:
                max_price = prices[right]

            profit = max(profit, max_price - min_price )

        return profit

            