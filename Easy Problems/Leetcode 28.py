class Solution:
    def strStr(self, haystack: str, needle: str) -> int: 
        if needle not in haystack:
            return -1
        sz = len(needle)
        if 1 == sz:
            for i in range(len(haystack)):
                if needle == haystack[i]:
                    return i
        for i in range(len(haystack)):
            if haystack[i:i+sz] == needle:
                return i
            
        