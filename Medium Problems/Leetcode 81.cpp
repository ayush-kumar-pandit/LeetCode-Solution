class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        sort(nums.begin(),nums.end());
        while(low <= high){
            int mid = low + (high - low)/2;
            if(nums[mid] == target) return true;
            else if(target < nums[mid]){
                high = mid - 1;
            }
            else{
                low = mid + 1;    
            }
        }
        return false;
    }
};