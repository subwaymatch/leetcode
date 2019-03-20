class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
        
        result = []
        new_row = []
        
        for row in nums:
            for v in row:
                new_row.append(v)
                
                if len(new_row) == c:
                    result.append(new_row)
                    new_row = []
        
        return result
