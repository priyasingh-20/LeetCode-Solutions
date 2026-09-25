class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        a=s+s
        ans=""
        k=k%len(s)
        for i in range(len(s)):
            ans+=a[i+k]
        return ans
        