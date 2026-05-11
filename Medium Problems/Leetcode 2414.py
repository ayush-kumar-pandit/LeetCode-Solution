class Solution:
    def longestContinuousSubstring(self, s: str) -> int:

        start = 0
        res = 1
        for end in range(1,len(s)):
            if ord(s[end]) != ord(s[end - 1]) + 1:
                start = end
            res = max(res,end - start + 1)

            
        return res