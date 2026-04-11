class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = {}
        d2 = {}

        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = 1
            else:
                d1[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in d2:
                d2[t[i]] = 1
            else:
                d2[t[i]] += 1
       

        for i in d2:
            if i not in d1:
                return i
            if d1[i] != d2[i]:
                return i 

        
            