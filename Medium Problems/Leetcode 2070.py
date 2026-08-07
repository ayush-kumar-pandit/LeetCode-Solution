class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()

        # Prefix maximum beauty
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])

        prices = [price for price, _ in items]
        ans = []

        for q in queries:
            idx = bisect_right(prices, q) - 1
            if idx >= 0:
                ans.append(items[idx][1])
            else:
                ans.append(0)

        return ans