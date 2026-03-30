class Solution {
public:
    string reversePrefix(string s, int k) {
        if(k == 1)  return s;
        k--;
        for(int i = 0; i <= k; i++,k--){
            char ch = s[i];
            s[i] = s[k];
            s[k] = ch;
        }
        return s;
    }
};