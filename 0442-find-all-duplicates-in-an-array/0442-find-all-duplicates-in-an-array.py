from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        counter=Counter(nums)
        
        for num,freq in counter.items():
            if freq==2:
                ans.append(num)

        return ans




        