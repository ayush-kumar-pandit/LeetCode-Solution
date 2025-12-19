class Solution {
public:
    bool isvowel(char ch){
        return  ch == 'a' or ch == 'A' or
                ch == 'e' or ch == 'E' or
                ch == 'i' or ch == 'I' or 
                ch == 'o' or ch == 'O' or
                ch == 'u' or ch == 'U';
    }
    string reverseVowels(string s) {
        int l = 0;
        int h = s.size() - 1;

        while(l < h){
            if(!isvowel(s[l]))  l++;
            
            if(!isvowel(s[h]))    h--;
            
            if(isvowel(s[l]) && isvowel(s[h])){
                char temp = s[l];
                s[l] = s[h];
                s[h] = temp;
                l++, h--; 
            }
            
        }
        return s;
    }
};