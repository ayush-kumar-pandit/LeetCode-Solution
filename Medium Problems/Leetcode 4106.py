class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res = []
        x = ""
        y = ""
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                x += s1[i]
                y += s2[i]
            elif x and y:
                res.append([x,y])
                x = ""
                y = ""
        if x and y:
            res.append([x,y])
        return res