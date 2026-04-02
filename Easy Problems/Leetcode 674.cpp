class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int ans = 1;
        int start = 0;
        for(int i = 0; i < nums.size() - 1; i++){
            if(nums[i] < nums[i + 1]){
                int x = i + 2 - start;
                if(x >= ans) ans = x; 
            }
            else{
                start = i + 1;
            }
        }
        return ans;
    }
};