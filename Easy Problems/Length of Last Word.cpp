class Solution {
public:
    int lengthOfLastWord(string s) {
        if (s.size() == 1 and s[0] != ' ')
            return 1;
        int count = 0;
        int i = s.size() - 1;

        while (s[i] == ' ')
            i--;

        while (i >= 0) {
            if (s[i] == ' ') {
                break;
            }
            count++;
            i--;
        }

        return count;
    }
};