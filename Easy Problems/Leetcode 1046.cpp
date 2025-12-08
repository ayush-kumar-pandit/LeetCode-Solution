class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        if(stones.size() == 1)  return stones[0];
        
        while(stones.size() > 1){
            sort(stones.begin(), stones.end());
            int y = stones.back();
            stones.pop_back();

            int x = stones.back();
            stones.pop_back();

            if(x == y){
                if(stones.size() == 0)  return 0;
                continue;
            } 

            else    stones.push_back(y - x);
        }
        return stones[0];
    }
};