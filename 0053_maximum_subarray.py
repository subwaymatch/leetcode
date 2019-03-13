class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        curr_max = dp[0]
        
        for idx in range(1, len(nums)):
            num = nums[idx]
            
            dp[idx] = num if dp[idx - 1] <= 0 else num + dp[idx - 1]
            
            if dp[idx] > curr_max:
                curr_max = dp[idx]
        
        return curr_max
