class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        a=""
        for word in words:
            a+=word

            if a==s:
                return True
            
            if len(a)>len(s):
                return False
        
        return False