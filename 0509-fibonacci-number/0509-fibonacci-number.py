# class Solution:
#     def fib(self, n: int) -> int:
#         a,b=0,1
#         for _ in range(n):
#             a,b=b,a+b
#         return a

class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        return self.fib(n-1)+self.fib(n-2)  ##object oriented code and used self when calling the main function