class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        
        res = []
        for x in range(len(heights)):
            temp = heights[:]
            m1 = float(inf)
            for i in range(x + 1, len(temp)):
                m1 = min(m1, temp[i])
                temp[i] = m1
                
            m1 = float(inf)
            for i in range(x, -1, -1):
                m1 = min(m1, temp[i])
                temp[i] = m1
            res.append(sum(temp))
                
        return max(res)