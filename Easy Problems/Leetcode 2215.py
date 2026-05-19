class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        s1 = set(nums1)
        s2 = set(nums2)
        temp = []
        for i in s1:
            if i not in s2:
                temp.append(i)
        res.append(temp)
        temp = []
        for i in s2:
            if i not in s1:
                temp.append(i)
        res.append(temp)
        return res