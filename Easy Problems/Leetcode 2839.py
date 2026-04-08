class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        st1 = s1[0] + s1[1] + s1[2] + s1[3]
        st2 = s1[0] + s1[3] + s1[2] + s1[1]
        st3 = s1[2] + s1[1] + s1[0] + s1[3]
        st4 = s1[2] + s1[3] + s1[0] + s1[1]
        

        return st1 == s2 or st2 == s2 or st3 == s2 or st3 == s2 or st4 == s2