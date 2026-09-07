from collections import Counter
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        counter=Counter(candyType)
        n=len(candyType)
        a=len(counter)
        if a<=n//2:
            return a
        else:
            return n//2