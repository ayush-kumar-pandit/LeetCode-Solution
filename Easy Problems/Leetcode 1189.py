class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 5:
            return 0
        freq = {}
        for ch in text:
            if ch in 'balon':
                freq[ch] = freq.get(ch,0) + 1
        if not freq or len(freq.keys()) < 5:
            return 0
        res = []

        for key,value in freq.items():
            if key == 'l' or key == 'o':
                res.append(value // 2)
            else:
                res.append(value)
        return min(res)