class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            missing_gap = nums[i] - nums[i - 1] - 1
            
            if k <= missing_gap:
                return nums[i - 1] + k
            else:
                k -= missing_gap
                
        return nums[-1] + k
