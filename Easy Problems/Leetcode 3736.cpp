class Solution {
public:
    int minMoves(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int count = 0;
        int sz = nums.size() - 1;
        for(int i = 0; i <= sz; i++){
            while(nums[i] != nums[sz]){
                nums[i] +=1;
                count++;
            }
        }
        return count;
    }
};