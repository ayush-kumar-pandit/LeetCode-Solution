class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        for i in gain:
            alt.append(alt[-1] + i)
        return max(alt)