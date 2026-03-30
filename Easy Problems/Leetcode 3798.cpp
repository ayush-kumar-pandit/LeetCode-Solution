class Solution {
public:
    string largestEven(string s) {
        int x = s.size() - 1;
        while(x >= 0){
            if(s[x] == '2')
                return s;
            else
                s.pop_back();
            x--;
        }
        
        return "";
    }
};