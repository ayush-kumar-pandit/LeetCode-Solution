class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double ans;
        vector<int> nums;
        int i = 0, j = 0;
        while(i < nums1.size() and j < nums2.size()){
            if(nums1[i] < nums2[j]){
                nums.push_back(nums1[i]);
                i++;
            }
            else{
                nums.push_back(nums2[j]);
                j++;
            }
        }
        if(i == nums1.size()){
            while(j < nums2.size()){
                nums.push_back(nums2[j]);
                j++;
            }
        }
        else{
            while(i < nums1.size()){
                nums.push_back(nums1[i]);
                i++;
            }
        }
        if(nums.size() % 2){
            ans = nums[nums.size()/2];
        }
        else{
            int r = nums[nums.size()/2];
            int l = nums[nums.size()/2 - 1];
            ans = (r + l) / 2.0;
        }
        return ans;
    }
};