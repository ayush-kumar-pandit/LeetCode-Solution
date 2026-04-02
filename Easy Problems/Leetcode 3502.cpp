class Solution {
public:
    vector<int> minCosts(vector<int>& cost) {
        vector<int> ans(cost.size(),0);
        int x = cost[0];
        ans[0] = x;
        for(int i = 1; i < cost.size(); i++){
            if( cost[i] < x ){
                ans[i] = cost[i];
                x = cost[i];
            }
            else{
                ans[i] = x;
            }
        } 
        return ans;
    }
};