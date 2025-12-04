class Solution {
public:
    int maximizeExpressionOfThree(vector<int>& nums) {
        sort(nums.begin(),nums.end());

        int x = nums[nums.size() - 1];
        int y = nums[nums.size() - 2];
        int z = nums[0];

        return x + y - z;
    }
};