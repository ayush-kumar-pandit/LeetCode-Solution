class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        res = ""
        while freq:
            maxx = max(freq.values())
            for ch in list(freq.keys()):
                if freq[ch] == maxx:
                    res += ch * maxx
                    del freq[ch]
        return res