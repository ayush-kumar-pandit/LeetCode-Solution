class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums):
            first = -1
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    first = mid
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return first

        def find_last(nums):
            last = -1

            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    last = mid
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return last
        if not nums:
            return -1, -1
        return find_first(nums), find_last(nums)
