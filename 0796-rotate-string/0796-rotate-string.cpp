class Solution {
public:
    bool rotateString(string s, string goal) {
        if(s.size()!=goal.size()){
            return false;
        }
        for(int i=0;i<s.size();i++){
            if(s==goal){
                return true;
            }
            s=s.substr(s.size()-1,s.size())+s.substr(0,s.size()-1);
        }
        return false;
    }
};