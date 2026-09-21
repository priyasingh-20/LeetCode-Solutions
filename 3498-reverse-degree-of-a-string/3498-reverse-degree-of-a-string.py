class Solution:
    def reverseDegree(self, s: str) -> int:
        st="abcdefghijklmnopqrstuvwxyz"
        ts=st[::-1]
        total=0
        
        for i in range(len(s)):
            total+=(ts.index(s[i])+1)*(i+1)

        return total