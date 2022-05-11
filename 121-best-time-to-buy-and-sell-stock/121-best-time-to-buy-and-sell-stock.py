# https://www.youtube.com/watch?v=eMSfBgbiEjk&ab_channel=takeUforward
'''
Here, initializing list for min and then travelling whole list, then com pare it with max element..

test2 = [3,5,0,3,1,4]
3 (low) -> 5 (profit=2) -> 0 (low) -> 3 (profit=3) -> 1 (profit=1) => 4 (profit=4)
=> profit=4

'''
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         low = prices[0]
        
#         for price in prices[1:]:
#             if price < low:
#                 low = price
#             elif (price - low) > profit:
#                 profit = price - low       
#         return profit
class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
