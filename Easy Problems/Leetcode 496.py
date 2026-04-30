class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i,v in enumerate(nums2):
            d[v] = i
        
        res = []
        for i in nums1:
            ind = d[i]
            x = -1
            for j in range(ind,len(nums2)):
                if nums2[j] > i:
                    x = nums2[j]
                    break
            res.append(x)
        return res