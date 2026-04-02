class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        int n = s.size();
        vector<int> ans(n,1);
        int x = 0;
        for(int i = n - 1; i >= 0; i--){
            if(s[i] == c){
                ans[i] = 0;
                x = i;
            }   
        }
        for(int i = 0; i < n; i++){
            if(ans[i] == 0){
                x = i;
                continue;
            }
            if(x - i > 0)   ans[i] = x - i;
            else    ans[i] = (x - i) * -1;
        }
        
        for(int i = n - 1; i >= 0; i--){
            if(ans[i] == 0){
                x = i;
                continue;
            }
            int ne = x - i;
            if(ans[i] < ne) continue;
            else{
                if(x - i > 0)   ans[i] = x - i;
                else    ans[i] = (x - i) * -1;
            }
        }
        return ans;
    }
};