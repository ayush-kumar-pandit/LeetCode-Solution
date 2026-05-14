class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        idx = {}
        for i,v in enumerate(nums):
            idx[v] = i
        
        for op in operations:
            nums[idx[op[0]]] = op[1]
            idx[op[1]] = idx.get(op[0])
        return nums