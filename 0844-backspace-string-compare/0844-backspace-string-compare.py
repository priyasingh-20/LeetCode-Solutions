class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in range(len(s)):
            if s[i]=='#':
                if a:
                    a.pop()
            else:
                a.append(s[i])
        for i in range(len(t)):
            if t[i]=='#':
                if b:
                    b.pop()
            else:
                b.append(t[i])
        return a==b


        