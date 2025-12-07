class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if(nums.size() == 1 and nums[0] != 1) return 1;
        else if(nums.size() == 1 and nums[0] == 1) return 2;
        

        sort(nums.begin(),nums.end());
        
       

        int i = 0;
        for(int j = 0; j < nums.size(); j++){
            if(nums[j] >= 1){
                nums[i] = nums[j];
                i++;
            }
        }
        if(nums[0] != 1 and nums[1] > 1)    return 1;
        if(nums[0] == 1 and nums[1] > 2)    return 2;


        int l = 0;
        for(int m = 1; m < nums.size(); m++){
            if(nums[m] != nums[l]){
                l++;
                nums[l] = nums[m];
            }
        }

        int c = 1;
        for(int j = 0; j <= l; j++){
            if(nums[j] != c){
                return c;
            }
            c++; 
        }

        return c;
    }
};