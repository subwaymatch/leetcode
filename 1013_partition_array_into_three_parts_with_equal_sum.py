class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        list_sum = sum(A)
        is_divisible_by_three = list_sum % 3 == 0
        
        if not is_divisible_by_three or len(A) < 3:
            return False
        
        subarray_sum = int(list_sum / 3)
        
        part1_sum = 0
        part1_right_index = 0
        
        for i in range(len(A)):
            part1_sum = part1_sum + A[i]
            
            if part1_sum == subarray_sum:
                part1_right_index = i
                break
        
        part3_sum = 0
        
        for i in reversed(range(part1_right_index + 2, len(A))):
            part3_sum = part3_sum + A[i]
            
            if part3_sum == subarray_sum:
                return True
            
        
        return False
