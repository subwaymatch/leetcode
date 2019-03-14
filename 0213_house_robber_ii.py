class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        return max(self.find_max_profit(nums[:-1]), self.find_max_profit(nums[1:]))
    
    def find_max_profit(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for idx in range(2, len(nums)):
            dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx])
        
        return dp[-1]
