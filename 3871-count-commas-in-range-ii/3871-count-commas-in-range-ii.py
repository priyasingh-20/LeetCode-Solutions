class Solution:
    def countCommas(self, n: int) -> int:
        if n<10**3:
            return 0
        count=0
        num=1000
        while num<=n:
            count+=n-num+1
            num*=1000
        return count

