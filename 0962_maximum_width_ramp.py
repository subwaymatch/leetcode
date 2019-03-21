class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        bounds = {}
        rightmost = 0
        max_width = 0
        
        for i, a in enumerate(A):
            if a in bounds:
                bounds[a][0] = min(bounds[a][0], i)
                bounds[a][1] = max(bounds[a][0], i)
                
            else:
                bounds[a] = [i, i]
        
        nums = reversed(sorted(list(bounds.keys())))
        
        for num in nums:
            rightmost = max(rightmost, bounds[num][1])
            max_width = max(max_width, rightmost - bounds[num][0])
        
        return max_width
