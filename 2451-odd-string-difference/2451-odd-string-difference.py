class Solution:
    def oddString(self, words: List[str]) -> str:
        
        ans=[]
        for i in words:
            diff=[]
            for j in range(len(i)-1):
                diff.append(ord(i[j+1])-ord(i[j]))
            ans.append(diff)
            
        for i in range(len(ans)):
            if ans.count(ans[i])==1:
                return words[i]