class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p1,p2):
            return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
            
        d = [
            dist(p1, p2),
            dist(p1, p3),
            dist(p1, p4),
            dist(p2, p3),
            dist(p2, p4),
            dist(p3, p4)
        ]
        d.sort()

        return d[0] > 0 and d[0] == d[1] == d[2] == d[3] and d[4] == d[5]