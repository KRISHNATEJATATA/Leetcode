class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minrow=[]
        maxcol=[]
        for i in matrix:
            minrow.append(min(i))
        for column in zip(*matrix):
            maxcol.append(max(column))
        minrow=set(minrow)
        for i in maxcol:
            if i in minrow:
                return[i]