class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        set_nums=set(nums)
        i=1
        
        while i*k in set_nums:
            i+=1   
        return i*k