class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc = 0
        l = []
        
        for i in range(len(nums)):
            acc += nums[i]
            l.append(acc)
            
        return l
