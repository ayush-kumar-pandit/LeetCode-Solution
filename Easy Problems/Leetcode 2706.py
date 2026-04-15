class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        mi = prices[0] + prices[1]
        if mi <= money:
            return money - mi
        return money