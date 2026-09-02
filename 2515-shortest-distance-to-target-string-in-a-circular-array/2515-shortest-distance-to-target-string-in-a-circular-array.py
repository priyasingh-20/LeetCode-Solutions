class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        ans=n
        for i in range(len(words)):
            if words[i]==target:
                ans=min(ans,abs(i-startIndex),n-abs(i-startIndex))
        if ans==n:    
            return -1
        return ans
            

