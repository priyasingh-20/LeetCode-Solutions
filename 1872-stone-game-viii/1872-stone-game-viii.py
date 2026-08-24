class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        sum_stones=[0]*len(stones)
        sum_stones[0]=stones[0]

        for i in range(1,len(stones)):
            sum_stones[i]=sum_stones[i-1]+stones[i]
        ans=sum_stones[-1] #Start ans with the total sum of all stones

        for i in range(len(stones)-2,0,-1):  #We are checking prefix positions:prefix[3] prefix[2] prefix[1] #We don't use prefix[0] because the game requires taking at least 2 stones.
        
            ans=max(ans,sum_stones[i]-ans) #For each prefix, calculate the score assuming the opponent plays optimally, and keep the best score for Alice

        return ans



        