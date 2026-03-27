class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        dic = {}
        start = 0

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= start:
                start = dic[s[i]] + 1   

            dic[s[i]] = i
            m = max(m, i - start + 1)

        return m