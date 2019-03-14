class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle == []:
            return 0
        
        for idx in range(1, len(triangle)):
            row = triangle[idx]
            prev_row = triangle[idx - 1]
            
            row[0] += prev_row[0]
            row[-1] += prev_row[-1]
            
        for idx in range(2, len(triangle)):
            row = triangle[idx]
            prev_row = triangle[idx - 1]
            
            for col in range(1, len(row) - 1):
                row[col] += min(prev_row[col - 1], prev_row[col])
                
        return min(triangle[-1])
