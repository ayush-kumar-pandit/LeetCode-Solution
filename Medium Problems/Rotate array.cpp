class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k % nums.size();
        int low = 0;
        int high = nums.size() - 1;
        while(low < high){
            int temp = nums[low];
            nums[low] = nums[high];
            nums[high] = temp;
            low++;
            high--;
        }
        low = 0;
        high = k - 1;
        while(low < high){
            int temp = nums[low];
            nums[low] = nums[high];
            nums[high] = temp;
            low++;
            high--;
        }
        low = k;
        high = nums.size() - 1;
        while(low < high){
            int temp = nums[low];
            nums[low] = nums[high];
            nums[high] = temp;
            low++;
            high--;
        }
    }
};
       