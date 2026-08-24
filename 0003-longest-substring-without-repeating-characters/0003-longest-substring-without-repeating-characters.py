class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = 0
        m = 0
        d = {}
        for i, v in enumerate(s):
            if v in d and st <= d[v]:
                st = d[v] + 1
            else:
                m = max(m, i - st + 1)
            d[v] = i
        return m
