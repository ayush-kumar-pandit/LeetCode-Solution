class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = -1;
        int last = -1;
        int n = nums.size();
        
        if(n == 0){
            return {first,last};
        }

        for(int i = 0; i < n; i++){
            if(nums[i] == target){
                first = i;
                break;
            }
            if(nums[i] > target)
                break;
        }
        if(first != -1){
            for(int i = first; i < n; i++){
                if(nums[i] == target){
                    last = i;
                }
                if(nums[i] > target)
                    break; 
            }
        }
        return {first,last};
    }
};