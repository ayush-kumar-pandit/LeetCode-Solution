class Solution {
public:
    int absDifference(vector<int>& nums, int k) {
        if(nums.size() == 1)    return 0;

        sort(nums.begin(), nums.end());
        int x = 0;
        int len = nums.size() - 1;
        for(int i = len; i >= len - k + 1; i--){
            x += nums[i];
        }
        int y = 0;
        for(int i = 0; i < k; i++){
            y += nums[i];
        }
        return x - y;
    }
};