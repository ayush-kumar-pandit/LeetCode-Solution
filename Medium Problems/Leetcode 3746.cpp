class Solution {
public:
    int minLengthAfterRemovals(string s) {
        if(s.size() == 1) return 1;

        sort(s.begin(),s.end());
        
        int ans = 0;

        for(char ch: s){
            if(ch == 'a')   ans++;
            else ans--;
        }
        if(ans < 0)
            return (ans * -1);
        return ans;
    }
};