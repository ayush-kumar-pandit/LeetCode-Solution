class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = j = 0
        n = len(nums1) - 1
        m = len(nums2) - 1
        res = []
        while i <= n and j <= m:
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0],nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] > nums2[j][0]:
                res.append([nums2[j][0],nums2[j][1]])
                j += 1
            else:
                res.append([nums1[i][0],nums1[i][1]])
                i += 1
        if i <= n:
            while i <= n:
                res.append([nums1[i][0],nums1[i][1]])
                i += 1
        else :
            while j <= m:
                res.append([nums2[j][0],nums2[j][1]])
                j += 1

        return res
