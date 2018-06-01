class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: 
            return 0
        
        LCIS = 1
        current_max = 1
        
        for index, num in enumerate(nums[1:]):
            if num > nums[index]: 
                current_max += 1
                
                LCIS = max(current_max, LCIS)
            else:
                current_max = 1
                
        return LCIS
