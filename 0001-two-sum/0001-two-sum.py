class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={} #an empty dict
        for i,num in enumerate(nums): #Loop through the array i = index, num = value
            complement=target-num
            if complement in seen:
                return [seen[complement],i] #output as [i,j]
            seen[num]=i #store each element of list in dict
                    