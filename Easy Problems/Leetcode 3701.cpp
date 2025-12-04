class Solution {
public:
    int alternatingSum(vector<int>& nums) {
        if(nums.size() == 1)    return nums[0];
        int ans = 0;
        int sign = 1;
        for(int i : nums){
            if(sign == -1){
                ans = ans - i;
                sign = 1;
            }
            else{
                ans = ans + i;
                sign = -1;
            }
        }
        return ans;
    }
};