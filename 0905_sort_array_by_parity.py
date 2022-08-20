class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        
        while left < right:
            if A[left] % 2 == 0:
                left += 1
                continue
            if A[right] % 2 == 1:
                right -= 1
                continue
            
            tmp = A[left]
            A[left] = A[right]
            A[right] = tmp
            left += 1
            right -= 1
            
        return A
