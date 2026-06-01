class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        res = []
        if len(nums1) > len(nums2):
            for i in nums2:
                freq[i] = freq.get(i, 0) + 1
            for i in nums1:
                if i in freq and freq[i]:
                    res.append(i)
                    freq[i] -= 1
        else:
            for i in nums1:
                freq[i] = freq.get(i, 0) + 1
            for i in nums2:
                if i in freq and freq[i]:
                    res.append(i)
                    freq[i] -= 1
            
        return res