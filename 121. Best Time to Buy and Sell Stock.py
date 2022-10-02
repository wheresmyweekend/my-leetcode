class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. Define pointers and profit
        l, r, profit = 0, 1, 0

        # 2. right pointer = sell, left pointer  = buy
        # If right is smaller than left, its a loss, shift right by 1, 
        # and shift left to previous right location since its the new local minimum
        # If left is smaller than right, profit is made, so shift right to check subsequent dates
        # profit variable captures the best possible profit
        while r < len(prices):
            profit = max(profit, prices[r]-prices[l])
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        return profit