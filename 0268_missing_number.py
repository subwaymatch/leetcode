class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return self.missingNumberUsingSum(nums)
    
    def missingNumberUsingXOR(self, nums: List[int]) -> int:
        sum = 0
        
        for i in range(0, len(nums) + 1):
            sum = sum ^ i
            
        for n in nums:
            sum = sum ^ n
            
        return sum
    
    def missingNumberUsingSum(self, nums: List[int]) -> int:
        return int((len(nums) * (len(nums) + 1)) / 2 - sum(nums))
