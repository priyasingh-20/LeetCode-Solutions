class Solution:
    def isPalindrome(self, x: int) -> bool:
        digit=0
        rev=0
        temp=x
        while(x>0):
            digit=x%10
            rev=rev*10+digit
            x=x//10
        return rev==temp