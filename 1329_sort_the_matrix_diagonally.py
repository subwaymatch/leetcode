class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat) - 1, -1, -1):
            self.sortDiagonalFrom(mat, i, 0)
            
        for j in range(1, len(mat[0])):
            self.sortDiagonalFrom(mat, 0, j)
            
        return mat
            
    def sortDiagonalFrom(self, mat: List[List[int]], startRow: int, startCol: int):
        seq = []
        i = startRow
        j = startCol
        
        while (i < len(mat)) and (j < len(mat[0])):
            seq.append(mat[i][j])
            i += 1
            j += 1
            
        seq.sort()
        
        i = startRow
        j = startCol
        idx = 0
        
        while (i < len(mat)) and (j < len(mat[0])):
            mat[i][j] = seq[idx]
            i += 1
            j += 1
            idx += 1
