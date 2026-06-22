class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = {}
        for ch in chars:
            freq[ch] = freq.get(ch, 0) + 1
        res = 0
        for word in words:
            freq_1 = {}
            for ch in word:
                freq_1[ch] = freq_1.get(ch, 0) + 1

            for ch in word:
                if freq_1[ch] > freq.get(ch,0):
                    break
            else:
                res += len(word)
        return res