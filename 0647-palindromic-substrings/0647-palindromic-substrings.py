class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        def expand(left, right):
            nonlocal ans
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        
        for i in range(n):
            # Odd-length palindromes
            expand(i, i)

            # Even-length palindromes
            expand(i, i + 1)

        return ans