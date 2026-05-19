class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        st1 = s1.split()
        st2 = s2.split()
        freq1 = {}
        freq2 = {}
        for word in st1:
            freq1[word] = freq1.get(word, 0) + 1

        for word in st2:
            freq2[word] = freq2.get(word, 0) + 1

        res = []
        for word in freq1:
            if freq1[word] == 1 and word not in freq2:
                res.append(word)

        for word in freq2:
            if freq2[word] == 1 and word not in freq1:
                res.append(word)
        return res
