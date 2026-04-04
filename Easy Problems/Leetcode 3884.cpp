class Solution {
public:
    int firstMatchingIndex(string s) {
        int i = 0;
        int n = s.size() - 1;
        while(i <= n/2){
            if(s[i] == s[n - i])    return i;
            i++;
        }
        return -1;
    }
};