class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        for(int i = 0, j = 1; j < nums.size(); j++, i++){
            if(nums[i] == nums[j])  return true;
        }
        return false;
    }
};