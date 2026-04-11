class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for i in sentences:
            x = i.split()
            if ans < len(x):
                ans = len(x)
        return ans