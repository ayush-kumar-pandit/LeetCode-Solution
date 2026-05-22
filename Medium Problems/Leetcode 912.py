class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            l_half = arr[:mid]
            r_half = arr[mid:]
            l_half = merge_sort(l_half)
            r_half = merge_sort(r_half)
            return merge(l_half,r_half)
        
        def merge(left: List[int], right: List[int]) -> List[int]:
            i = j = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        return merge_sort(nums)