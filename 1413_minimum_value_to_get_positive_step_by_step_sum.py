class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        running_sum = 0
        running_min = 0
        
        for num in nums:
            running_sum += num
            
            if running_sum < running_min:
                running_min = running_sum
                
        return abs(running_min) + 1 if running_min < 1 else 1
