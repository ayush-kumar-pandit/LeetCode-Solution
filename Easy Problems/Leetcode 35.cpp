class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        if(target <= nums[0])
                return 0;

        if(nums.size() == 1){
            if(nums[0] == target)
                return 0;
            else if(target < nums[0])
                return 0;
            return 1;
        }

        int low = 0;
        int high = nums.size() - 1;
        while(low < high){
            int mid = low + (high - low) / 2;
            if(nums[mid] == target)
                return mid;

            else if(nums[mid] > target){
                if(nums[mid-1] < target)
                    return mid;
                high = mid - 1;
            }

            else if(nums[mid] < target){
                if(nums[mid+1] >= target)
                    return mid+1;
                low = mid + 1;
            }
        }
        return high + 1;
    }
};