class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)
        while n:
            if int(num[-1])%2!=0:
                return num
                break
            else:
                num=num[0:n-1]
                n-=1
        return ""

        
        
        