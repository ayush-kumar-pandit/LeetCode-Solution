class Solution:
    def equalFrequency(self, word: str) -> bool:
        def count():
            values = [x for x in freq if x > 0]
            if not values:
                return True
            return len(set(values)) == 1

        freq = [0] * 26

        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        res = count()

        if res:
            for i in range(26):
                if freq[i]:
                    freq[i] -= 1
                    if count():
                        return True

                    freq[i] += 1
            return False

        for i in range(26):
            if freq[i]:
                freq[i] -= 1

                if count():
                    return True

                freq[i] += 1

        return False
