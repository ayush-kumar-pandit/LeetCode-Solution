class Solution {
public:
    int minAddToMakeValid(string s) {
        int sz = 0, op = 0;

        for(char ch: s){
            if(ch == '(') sz++;
            else if(sz > 0) sz--;
            else op++;
        }
        return op + sz;
    }
};