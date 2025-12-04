class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        sort(nums.begin(),nums.end());

        vector<int> ans;

        int temp = nums[0];
        int i = 0;
        while(i < nums.size()){
            if(nums[i] == temp){
                temp++;
                i++;
            }
            else{
                ans.push_back(temp++);
            }
        }
        return ans;
    }
};