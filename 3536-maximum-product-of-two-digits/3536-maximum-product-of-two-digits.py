class Solution:
    def maxProduct(self, n: int) -> int:
        a=list(str(n))
        a.sort(reverse=True)
        return int(a[0])*int(a[1])

        