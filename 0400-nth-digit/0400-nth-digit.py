class Solution:
    def findNthDigit(self, n: int) -> int:
        digits=1
        count=9
        start=1
        while n>digits*count: #increasing digit
            n-=digits*count
            digits+=1
            count*=10
            start*=10
        num=start+(n-1)//digits #find actual num
        index=(n-1)%digits #find index of num

        return int(str(num)[index])
