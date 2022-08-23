class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        numSubarrays = 0
        numContiguousZeros = 0
        
        for i in range(len(nums)):
            num = nums[i]

            if num == 0:
                numContiguousZeros += 1
            
            if (num != 0) or (i == len(nums) - 1):
                numSubarrays += self.numZeroFilledSubarrays(numContiguousZeros)
                numContiguousZeros = 0
                
        return int(numSubarrays)
                
    def numZeroFilledSubarrays(self, n):
        return n * (n + 1) / 2
