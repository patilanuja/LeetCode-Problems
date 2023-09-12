########## Time Complexity: O(n) ########## Space Complexity: O(1) ##########
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = max_price = prices[0]
#         profit = 0

#         for right in range(len(prices)):
            
#             if prices[right] < min_price:
#                 max_price = prices[right]
#                 min_price = prices[right]
            
#             if prices[right] > max_price:
#                 max_price = prices[right]

#             profit = max(profit, max_price - min_price )

#         return profit

###################################### or #########################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, max_profit = 0, 1, 0

        while right < len(prices):

            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right
            right += 1
            
        return max_profit