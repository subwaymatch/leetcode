class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        max_amount = 0
        
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for idx in range(2, len(nums)):
            dp[idx] = max(dp[idx - 1], nums[idx] + dp[idx - 2])
            
            if dp[idx] > max_amount:
                max_amount = dp[idx]
                
        return max_amount
