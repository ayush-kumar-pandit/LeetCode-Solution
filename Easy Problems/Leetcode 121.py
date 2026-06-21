class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        min_val = float("inf")
        for price in prices:
            if price <= min_val:
                min_val = price
            elif price - min_val > maximumProfit:
                maximumProfit = price - min_val
        return maximumProfit