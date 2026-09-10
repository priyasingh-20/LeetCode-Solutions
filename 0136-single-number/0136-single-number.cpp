class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int Num=0;
        for(int n:nums){
            Num^=n;
        }
    return Num;    
    }
};