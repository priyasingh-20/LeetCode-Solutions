class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        vector<char> arr(s.size());
        for(int i=0;i<s.size();i++){
            arr[indices[i]]=s[i];
        }
      
        return string(arr.begin(),arr.end());
    }
};