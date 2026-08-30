class Solution:
    def repeatedCharacter(self, s: str) -> str:
        lst=[] 
        for i in s:
            if i in lst:
                return i 
            else:
                lst.append(i)      