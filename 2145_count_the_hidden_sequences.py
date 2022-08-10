class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        if len(differences) == 1:
            return max(upper - lower - abs(differences[0]) + 1, 0)
        
        running_sum = 0
        running_min = 0
        running_max = 0
        
        for num in differences:
            running_sum += num
            
            if running_sum < running_min:
                running_min = running_sum
            if running_sum > running_max:
                running_max = running_sum
        
        return max(upper - lower - (running_max - running_min) + 1, 0)
