class Solution:
    def sortEvenOdd(self, nums):
        even = sorted(nums[0::2])
        odd = sorted(nums[1::2], reverse = True)

        res = []
        e = o = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(even[e])
                e += 1
            else:
                res.append(odd[o])
                o += 1

        return res
