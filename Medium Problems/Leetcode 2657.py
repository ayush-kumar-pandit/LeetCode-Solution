class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        res = []
        com = 0
        for i in range(len(A)):
            if A[i] in seen:
                com += 1
            else:
                seen.add(A[i])
            if B[i] in seen:
                com += 1
            else:
                seen.add(B[i])
            
            res.append(com)
        return res
