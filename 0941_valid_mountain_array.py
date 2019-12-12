class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        elif A[0] > A[1]:
            return False
        
        is_increasing = True
        prev_height = A[0]
        
        for height in A[1:]:
            if height == prev_height:
                return False
            
            elif is_increasing and height < prev_height:
                is_increasing = False
                
            elif not is_increasing and height > prev_height:
                return False
            
            prev_height = height
            
        return not is_increasing
