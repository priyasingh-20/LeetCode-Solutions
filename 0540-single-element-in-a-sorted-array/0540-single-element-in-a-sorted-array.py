class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1

        while(left<right):
            mid=(left+right)//2

            if mid%2==1:
                mid-=1

            if nums[mid]==nums[mid+1]:
                left=mid+2
            
            else:
                right=mid
        
        return nums[left]


#Less optimal because if complexity is O(n) so we applied binary search
# from collections import Counter
# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         counter=Counter(nums)
#         for i in set(nums):
#             if counter[i]==1:
#                 return i

