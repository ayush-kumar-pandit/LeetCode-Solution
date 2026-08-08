class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs=Counter(s)
        ct=Counter(t)
        ans=0
        for ch in cs:
            if cs[ch]>ct[ch]:
                ans+=cs[ch]-ct[ch]
        return ans