class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])

        if m*n!=r*c:
            return mat

        num=[]
        for row in mat:
            num.extend(row)

        ans=[]
        idx=0
        for i in range(r):
            ans.append(num[idx:idx+c])
            idx+=c

        return ans        