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
        
# class Solution:
#     def countCommas(self, n: int) -> int:
#         if n<10**3:
#             return 0
#         elif n<10**6:
#             return n-999
#         elif n<10**9:
#             return 2*(n-10**6+1)+10**6 - 1000
#         elif n<10**12:
#             return 3*(n-10**9+1)+2*(10**9-10**6)+10**6 - 1000
#         elif n < 10**15:
#             return 4*(n-10**12+1)+3*(10**12-10**9)+2*(10**9-10**6)+10**6 - 1000
#         return 5*(n - 10**15 + 1) + 4*(10**15 - 10**12) + 3*(10**12 - 10**9) + 2*(10**9 - 10**6) + 10**6 - 1000
            
            
        