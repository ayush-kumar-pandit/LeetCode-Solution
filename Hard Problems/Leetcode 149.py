class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        res = 1
        for i in range(len(points)-1):
            slope = defaultdict(int)
            for j in range(i+1,len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                if y1 == y2:
                    slope["inf"] += 1
                    res = max(res, slope["inf"])
                else:
                    s = (x1-x2) / (y1-y2)
                    slope[s] += 1
                    res = max(res, slope[s])

        return res+1