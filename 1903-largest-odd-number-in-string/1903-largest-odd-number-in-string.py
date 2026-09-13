class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                return num[0:i+1]
        return ""


        # n=len(num)
        # while n:
        #     if int(num[-1])%2!=0:
        #         return num
        #         break
        #     else:
        #         num=num[0:n-1]
        #         n-=1
        # return ""

        
        
        