class Solution:
    def findPow(self,x,n):
        if n==0:
            return 1
        a=self.findPow(x,n//2)
        if n%2==0:
            return a*a
        else:
            return a*a*x
    def myPow(self, x: float, n: int) -> float:
        if n>=0:
            return self.findPow(x,n)
        else:
            return 1/self.findPow(x,-n)
        # if n<0:
        #     x=1/x
        #     n=-n
        # ans=1
        # while n>0:
        #     if n%2==1:
        #         ans*=x
        #     x*=x
        #     n//=2
        # return ans
        