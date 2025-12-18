class Solution {
public:
    bool isPalindrome(string s) {

        string st;

        for(char ch : s){
            
            if(isalpha(ch) or isdigit(ch)){
                if(ch >= 'A' and ch <= 'Z')
                    ch += 'a' - 'A';
                st += ch;
            }

        }
        if(st.size() == 1) return true;
        if(st.size() == 2 and s[0] == st[1])  return true;

        string st2 = st;
        reverse(st2.begin(), st2.end());

        return st == st2;
    }
};