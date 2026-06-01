class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = {}
        mag = {}
        for ch in ransomNote:
            note[ch] = note.get(ch,0) + 1
        for ch in magazine:
            mag[ch] = mag.get(ch,0) + 1
        for ch in note:
            if ch not in mag or note[ch] > mag[ch]:
                return False
            
        return True