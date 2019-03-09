class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(2, len(A) - 1):
            if A[i] < A[i - 1]:
                return i - 1
        
        return len(A) - 2
