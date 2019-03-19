class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        isIncreasing = None
        
        for idx in range(1, len(A)):
            diff = A[idx] - A[idx - 1]

            if diff == 0:
                continue
            
            elif isIncreasing is None:
                isIncreasing = True if diff > 0 else False
                continue
            
            elif (isIncreasing and diff < 0) or (not isIncreasing and diff > 0):
                return False
            
        return True
